"""DS001 11.5: scalar batch normalization; no third-party dependency."""
from math import sqrt

def forward(z, gamma=1.0, delta=0.0, epsilon=1e-4):
    if not z or epsilon <= 0:
        raise ValueError("nonempty batch and positive epsilon required")
    n = len(z)
    mean = sum(z) / n
    centered = [x - mean for x in z]
    variance = sum(c*c for c in centered) / n
    std = sqrt(variance + epsilon)
    inv = 1.0 / std
    normalized = [c * inv for c in centered]
    y = [gamma*t + delta for t in normalized]
    return y, (centered, std, inv, normalized, gamma)

def backward(upstream, cache):
    centered, std, inv, normalized, gamma = cache
    n = len(centered)
    if len(upstream) != n:
        raise ValueError("gradient and batch shapes differ")
    d7 = [gamma*u for u in upstream]
    d2 = [a*inv for a in d7]
    d6 = sum(a*c for a, c in zip(d7, centered))
    d5 = -d6/(std*std)
    d4 = d5/(2*std)
    d3 = d4/n
    d2 = [a + 2*c*d3 for a, c in zip(d2, centered)]
    mean_d2 = sum(d2)/n
    dz = [a - mean_d2 for a in d2]
    dgamma = sum(u*t for u, t in zip(upstream, normalized))
    ddelta = sum(upstream)
    return dz, dgamma, ddelta

def check():
    z = [-2.0, -0.4, 0.3, 1.7, 2.2]
    gamma, delta, eps, step = 1.3, -0.2, 1e-4, 1e-5
    y, cache = forward(z, gamma, delta, eps)
    centered, std, inv, normalized, _ = cache
    n = len(z)
    max_jac_error = 0.0
    for j in range(n):
        plus, minus = z[:], z[:]
        plus[j] += step
        minus[j] -= step
        yp, _ = forward(plus, gamma, delta, eps)
        ym, _ = forward(minus, gamma, delta, eps)
        for i in range(n):
            exact = gamma*inv*((1 if i == j else 0) - 1/n
                    - centered[i]*centered[j]/(n*std*std))
            numeric = (yp[i]-ym[i])/(2*step)
            max_jac_error = max(max_jac_error, abs(exact-numeric))
    upstream = [1, -2, 0.4, 0.1, 0.7]
    dz, dg, dd = backward(upstream, cache)
    max_reverse_error = 0.0
    for j in range(n):
        plus, minus = z[:], z[:]
        plus[j] += step
        minus[j] -= step
        yp, _ = forward(plus, gamma, delta, eps)
        ym, _ = forward(minus, gamma, delta, eps)
        numeric = sum(u*(a-b)/(2*step) for u,a,b in zip(upstream,yp,ym))
        max_reverse_error = max(max_reverse_error,abs(dz[j]-numeric))
    print("25 Jacobian entries max absolute error:", format(max_jac_error, ".6g"))
    print("reverse-mode input gradient max absolute error:", format(max_reverse_error, ".6g"))
    print("parameter gradients:", dg, dd)
    assert max_jac_error < 1e-8 and max_reverse_error < 1e-8

if __name__ == "__main__":
    check()
