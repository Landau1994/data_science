"""重绘 ISLR 6.6 的一维目标函数；仅验证 y1=3、lambda=2 这一组输入。"""

from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    root = Path(__file__).resolve().parents[2]
    destination = root / "附件" / "习题图" / "ISLR-6.6-一维岭回归与Lasso.png"
    destination.parent.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.sans-serif": ["Microsoft YaHei", "SimHei", "DejaVu Sans"],
        "axes.unicode_minus": False,
        "font.size": 11,
    })
    response, penalty = 3.0, 2.0
    coefficients = np.linspace(-2.0, 6.0, 4001)
    objectives = [
        (response - coefficients) ** 2 + penalty * coefficients ** 2,
        (response - coefficients) ** 2 + penalty * np.abs(coefficients),
    ]
    expected_minima = [response / (1 + penalty), max(response - penalty / 2, 0)]
    formulas = [r"$(3-\beta_1)^2+2\beta_1^2$", r"$(3-\beta_1)^2+2|\beta_1|$"]
    titles = ["岭回归目标：式 (6.12)", "Lasso 目标：式 (6.13)"]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), layout="constrained")
    checks = []
    for axis, values, minimum, formula, title in zip(
        axes, objectives, expected_minima, formulas, titles
    ):
        selected_index = int(np.argmin(values))
        grid_minimum = float(coefficients[selected_index])
        assert abs(grid_minimum - minimum) < 1e-12
        objective_at_minimum = float(values[selected_index])
        axis.plot(coefficients, values, color="#215b91", linewidth=2, label=formula)
        axis.axvline(0, color="#b1b1b1", linewidth=0.8)
        axis.axvline(minimum, color="#ce6b22", linestyle="--", linewidth=1.2)
        axis.scatter([minimum], [objective_at_minimum], color="#ce6b22", s=40, zorder=4)
        axis.annotate(
            f"最小点 ({minimum:g}, {objective_at_minimum:g})",
            (minimum, objective_at_minimum), xytext=(12, 18), textcoords="offset points",
            color="#814210",
        )
        axis.set(title=title, xlabel=r"$\beta_1$", ylabel="目标函数值", xlim=(-2, 6))
        axis.grid(alpha=0.2)
        axis.legend(loc="upper center", frameon=False)
        checks.append({"analytic_coefficient": minimum, "grid_coefficient": grid_minimum,
                       "objective_value": objective_at_minimum})
    fig.suptitle(r"ISLR 6.6：$y_1=3,\ \lambda=2$（无截距，$X=I$）", fontsize=14)
    fig.savefig(destination, dpi=180, facecolor="white")
    plt.close(fig)
    print(json.dumps({
        "python_input": {"y1": response, "lambda": penalty, "beta_interval": [-2, 6],
                         "grid_points": len(coefficients), "randomness": "none"},
        "versions": {"numpy": np.__version__, "matplotlib": matplotlib.__version__},
        "checks": checks, "output": str(destination),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
