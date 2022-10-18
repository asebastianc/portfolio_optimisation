library(eaf)

setwd(".")

A1 <- read_datasets(file.path("../../results/alg1", "alg1_results_format.xz"))
A2 <- read_datasets(file.path("../../results/alg2", "alg2_results_format.xz"))

pdf("../../figures/A1.pdf")
eafplot(A1, xlab = "objective 1", ylab = "objective 2")
invisible(dev.off())

pdf("../../figures/A2.pdf")
eafplot(A2, xlab = "objective 1", ylab = "objective 2")
invisible(dev.off())

pdf("../../figures/A1_vs_A2.pdf")
eafdiffplot(A1, A2, type = "point", title.left = "Algorithm 1", title.right = "Algorithm 2")
invisible(dev.off())