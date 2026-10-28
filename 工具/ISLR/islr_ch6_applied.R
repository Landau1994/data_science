# ISLR 第二版第 6 章 6.8、6.9、6.11 的独立分析方案。
# 2026-10-25 已在 WSL R 4.3.1 实际运行；结果与运行时代码快照另行保存。
# 用法：Rscript 工具/ISLR/islr_ch6_applied.R 6.8 <输出目录>
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2L || !args[1] %in% c("6.8", "6.9", "6.11")) {
  stop("需要两个参数：题号（6.8、6.9 或 6.11）和输出目录。")
}
question <- args[1]
out <- args[2]
needed <- if (question == "6.8") c("leaps", "glmnet") else c("ISLR2", "glmnet", "pls")
for (pkg in needed) {
  if (!requireNamespace(pkg, quietly = TRUE)) stop(paste("请先安装 R 包：", pkg))
}
if (dir.exists(out) && length(list.files(out, all.files = TRUE, no.. = TRUE)) > 0L) {
  stop("输出目录必须为空；请为本次运行指定新目录。")
}
dir.create(out, recursive = TRUE, showWarnings = FALSE)
out <- normalizePath(out, mustWork = TRUE)
RNGkind("Mersenne-Twister", "Inversion", "Rejection")
seed <- 20261025L
set.seed(seed)
writeLines(c(paste("题号：", question), paste("随机种子：", seed),
             "结果仅支持本次数据、划分、参数网格和软件环境。",
             "固定随机种子不保证不同平台逐位一致。"), file.path(out, "run-info.txt"))
capture.output(sessionInfo(), file = file.path(out, "session-info.txt"))
write.csv(data.frame(package = needed, version = vapply(needed, function(p) {
  as.character(utils::packageVersion(p))
}, character(1))), file.path(out, "package-versions.csv"), row.names = FALSE)

save_object <- function(x, name) saveRDS(x, file.path(out, paste0(name, ".rds")))
save_table <- function(x, name) write.csv(x, file.path(out, paste0(name, ".csv")), row.names = FALSE)
make_folds <- function(n, k = 5L) sample(rep(seq_len(k), length.out = n))
lambda_grid <- 10^seq(5, -4, length.out = 100L)

if (question == "6.8") {
  n <- 100L
  x <- rnorm(n)
  epsilon <- rnorm(n)
  polynomial <- sapply(1:10, function(j) x^j)
  colnames(polynomial) <- paste0("X", 1:10)
  foldid <- make_folds(n)
  save_table(data.frame(row = seq_len(n), fold = foldid), "folds")
  save_object(list(x = x, epsilon = epsilon, predictors = polynomial,
                   beta_cubic = c(1, 2, -1, 0.5), beta_seventh = c(1, 1)), "data-and-parameters")

  fit_case <- function(y, label) {
    dat <- data.frame(Y = y, polynomial)
    for (method in c("exhaustive", "forward", "backward")) {
      fit <- leaps::regsubsets(Y ~ ., data = dat, nvmax = 10, method = method)
      s <- summary(fit)
      sizes <- seq_along(s$cp)
      score <- data.frame(size = sizes, cp = s$cp, bic = s$bic, adjusted_r2 = s$adjr2)
      save_table(score, paste(label, method, "scores", sep = "-"))
      chosen <- c(Cp = which.min(s$cp), BIC = which.min(s$bic), adjusted_R2 = which.max(s$adjr2))
      save_table(data.frame(criterion = names(chosen), size = as.integer(chosen)),
                 paste(label, method, "selected", sep = "-"))
      for (criterion in names(chosen)) {
        b <- coef(fit, chosen[[criterion]])
        save_table(data.frame(term = names(b), coefficient = as.numeric(b)),
                   paste(label, method, criterion, "coefficients", sep = "-"))
      }
      png(file.path(out, paste0(label, "-", method, "-criteria.png")), width = 1350, height = 450)
      par(mfrow = c(1, 3))
      for (metric in c("cp", "bic", "adjusted_r2")) {
        plot(score$size, score[[metric]], type = "b", xlab = "Model size", ylab = metric)
      }
      dev.off()
    }
    # cv.glmnet 在每个训练折内估计标准化参数；所有情况复用同一折号。
    cv <- glmnet::cv.glmnet(polynomial, y, alpha = 1, foldid = foldid,
                            lambda = lambda_grid, standardize = TRUE, type.measure = "mse")
    b <- as.matrix(coef(cv, s = "lambda.min"))
    save_table(data.frame(term = rownames(b), coefficient = as.numeric(b)), paste0(label, "-lasso-coefficients"))
    save_table(data.frame(lambda = cv$lambda, cv_mse = cv$cvm, cv_se = cv$cvsd), paste0(label, "-lasso-cv"))
    save_table(data.frame(lambda_min = cv$lambda.min, lambda_1se = cv$lambda.1se,
                         nonzero_slopes = sum(b[-1, 1] != 0)), paste0(label, "-lasso-selected"))
    png(file.path(out, paste0(label, "-lasso-cv.png")), width = 900, height = 650)
    plot(cv)
    dev.off()
    save_object(cv, paste0(label, "-lasso-fit"))
  }
  fit_case(1 + 2*x - x^2 + 0.5*x^3 + epsilon, "cubic")
  # (f) 保留同一 X 和噪声，明确只改变响应的信号结构。
  fit_case(1 + x^7 + epsilon, "seventh")
} else {
  env <- new.env(parent = emptyenv())
  dataset <- if (question == "6.9") "College" else "Boston"
  utils::data(list = dataset, package = "ISLR2", envir = env)
  dat <- env[[dataset]]
  response <- if (question == "6.9") "Apps" else "crim"
  save_object(dat, "source-data")
  # 固定数据模式：类别列仅展开成虚拟变量，不在全数据上估计中心、尺度或主成分。
  formula <- reformulate(setdiff(names(dat), response))
  x <- model.matrix(formula, data = dat)[, -1, drop = FALSE]
  y <- dat[[response]]
  train <- sort(sample(seq_len(nrow(dat)), floor(0.7*nrow(dat))))
  test <- setdiff(seq_len(nrow(dat)), train)
  xt <- x[train, , drop = FALSE]
  yt <- y[train]
  xv <- x[test, , drop = FALSE]
  yv <- y[test]
  foldid <- make_folds(length(train))
  save_table(data.frame(row = seq_len(nrow(dat)), id = rownames(dat),
                        partition = ifelse(seq_len(nrow(dat)) %in% train, "train", "test")), "split")
  save_table(data.frame(row = train, fold = foldid), "folds")
  save_table(data.frame(lambda = lambda_grid), "lambda-grid")

  methods <- if (question == "6.9") c("ols", "ridge", "lasso", "pcr", "pls") else c("ols", "ridge", "lasso", "pcr")
  records <- list()
  component_fit <- function(a, b, m, method) {
    d <- data.frame(Y = b, a, check.names = FALSE)
    fitfun <- if (method == "pcr") pls::pcr else pls::plsr
    fitfun(Y ~ ., data = d, ncomp = m, scale = TRUE, validation = "none")
  }
  component_predict <- function(fit, a, m) {
    as.numeric(predict(fit, newdata = data.frame(a, check.names = FALSE), ncomp = m))
  }
  for (method in methods) {
    if (method == "ols") {
      cvpred <- rep(NA_real_, length(yt))
      for (k in sort(unique(foldid))) {
        a <- foldid != k
        fit <- lm(Y ~ ., data = data.frame(Y = yt[a], xt[a, , drop = FALSE]))
        cvpred[!a] <- predict(fit, newdata = data.frame(xt[!a, , drop = FALSE]))
      }
      cv_mse <- mean((yt - cvpred)^2)
      fit <- lm(Y ~ ., data = data.frame(Y = yt, xt))
      pred <- as.numeric(predict(fit, newdata = data.frame(xv)))
      coefficients <- coef(fit)
      selected <- "unpenalized"
    } else if (method %in% c("ridge", "lasso")) {
      alpha <- if (method == "ridge") 0 else 1
      fit <- glmnet::cv.glmnet(xt, yt, alpha = alpha, foldid = foldid,
                               lambda = lambda_grid, standardize = TRUE, type.measure = "mse",
                               grouped = FALSE)
      selected <- as.character(fit$lambda.min)
      cv_mse <- min(fit$cvm)
      pred <- as.numeric(predict(fit, newx = xv, s = "lambda.min"))
      b <- as.matrix(coef(fit, s = "lambda.min"))
      coefficients <- setNames(as.numeric(b), rownames(b))
      save_table(data.frame(lambda = fit$lambda, cv_mse = fit$cvm, cv_se = fit$cvsd), paste0(method, "-cv"))
    } else {
      # 对每个 M 手工做相同的折划分；缩放、PCR/PLS 方向都只从各训练折学习。
      max_m <- min(ncol(xt),
                   min(vapply(unique(foldid), function(k) sum(foldid != k), integer(1))) - 1L)
      candidates <- 0:max_m
      cvpred <- matrix(NA_real_, nrow = length(yt), ncol = length(candidates))
      for (k in sort(unique(foldid))) {
        a <- foldid != k
        cvpred[!a, 1] <- mean(yt[a])
        fold_fit <- component_fit(xt[a, , drop = FALSE], yt[a], max_m, method)
        for (m in 1:max_m) cvpred[!a, m + 1L] <- component_predict(fold_fit, xt[!a, , drop = FALSE], m)
      }
      scores <- colMeans((cvpred - yt)^2)
      # M 从小到大排列，并列时选择更少的成分。
      m <- candidates[which.min(scores)]
      selected <- as.character(m)
      cv_mse <- min(scores)
      save_table(data.frame(M = candidates, cv_mse = scores), paste0(method, "-cv"))
      if (m == 0L) {
        fit <- list(intercept = mean(yt))
        pred <- rep(mean(yt), length(yv))
        coefficients <- c("(Intercept)" = mean(yt), setNames(rep(0, ncol(xt)), colnames(xt)))
      } else {
        fit <- component_fit(xt, yt, m, method)
        pred <- component_predict(fit, xv, m)
        b <- coef(fit, ncomp = m, intercept = TRUE)
        coefficients <- setNames(as.numeric(b), dimnames(b)[[1]])
      }
    }
    records[[method]] <- data.frame(method = method, tuning = selected, cv_mse = cv_mse,
                                    test_mse = mean((yv - pred)^2),
                                    nonzero_slopes = sum(abs(coefficients[-1]) > 1e-10))
    save_table(data.frame(term = names(coefficients), coefficient = coefficients), paste0(method, "-coefficients"))
    save_table(data.frame(row = test, observed = yv, predicted = pred), paste0(method, "-test-predictions"))
    save_object(fit, paste0(method, "-fit"))
  }
  comparison <- do.call(rbind, records)
  rownames(comparison) <- NULL
  save_table(comparison, "comparison")
  winner <- comparison$method[which.min(comparison$cv_mse)]
  writeLines(c(paste("按训练集交叉验证预先选择：", winner),
               "comparison.csv 的测试误差只用于评价，不用于改选方法或调整网格。",
               "若最优 lambda 位于网格边界，应记录局限；扩展网格属于新的探索性运行。",
               "PCR/PLS 的非零原变量系数数量不等于成分数 M；M=0 是截距基线。"),
             file.path(out, "selection.txt"))
}
files <- list.files(out, full.names = TRUE)
files <- files[basename(files) != "output-hashes.csv"]
save_table(data.frame(file = basename(files), md5 = unname(tools::md5sum(files))), "output-hashes")
message("分析完成。输出目录：", out)
