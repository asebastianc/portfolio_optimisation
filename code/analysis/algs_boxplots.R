library(tidyverse)
library(gridExtra)
library(ggpubr)

setwd(".")
alg1 <- read.csv("../../results/alg1/alg1_data_test.csv")
alg2 <- read.csv("../../results/alg2/alg2_data_test.csv")

alg1$Algorithm <- "Algorithm 1"
alg2$Algorithm <- "Algorithm 2"

df <- bind_rows(alg1, alg2)

return_plot <- ggplot(df, aes(Algorithm, Return)) + geom_boxplot(outlier.alpha = 0.1,
                                                  outlier.colour = "red",
                                                  outlier.shape = 4,
                                                  outlier.size = 0.5)
return_plot <- return_plot + xlab(element_blank())
return_plot <- return_plot + geom_line(data = tibble(x = c(1, 2), y = c(4*10^8, 4*10^8)),
                                       aes(x = x, y = y))

return_plot <- return_plot + geom_line(data = tibble(x = c(1, 1), y = c(4*10^8, 3.9*10^8)),
                                       aes(x = x, y = y))

return_plot <- return_plot + geom_line(data = tibble(x = c(2, 2), y = c(4*10^8, 3.9*10^8)),
                                       aes(x = x, y = y))

return_plot <- return_plot + geom_text(x = 1.5, y = 4.2*10^8, label = "p < 0.01", size = 3, face = "plain", family = "") + theme_bw()

return_plot <- return_plot +
  theme(panel.grid.major.x = element_blank()) +
  theme(panel.grid.major.y = element_line(linetype = 2, size = 0.4), panel.grid.minor.y = element_blank()) +
  theme(axis.text.x = element_text(colour = "black"), axis.text.y = element_text(colour = "black"))

risk_plot <- ggplot(df, aes(Algorithm, Risk)) + geom_boxplot(outlier.alpha = 0.1,
                                                outlier.colour = "red",
                                                outlier.shape = 4,
                                                outlier.size = 0.5) + scale_y_continuous(limits = c(0, 100000000)) + theme_bw() +
                                                theme(panel.grid.major.x = element_blank()) + theme(panel.grid.major.y = element_line(linetype = 2, size = 0.4),
                                                                                                    panel.grid.minor.y = element_blank()) +
  theme(axis.text.x = element_text(colour = "black"), axis.text.y = element_text(colour = "black"))

risk_plot <- risk_plot + xlab(element_blank())

risk_plot <- risk_plot + geom_line(data = tibble(x = c(1, 2), y = c(1*10^8, 1*10^8)),
                                   aes(x = x, y = y))

risk_plot <- risk_plot + geom_line(data = tibble(x = c(1, 1), y = c(1*10^8, 9.9*10^7)),
                                   aes(x = x, y = y))

risk_plot <- risk_plot + geom_line(data = tibble(x = c(2, 2), y = c(1*10^8, 9.9*10^7)),
                                   aes(x = x, y = y))

risk_plot <- risk_plot + geom_text(x = 1.5, y = 1.025*10^8, label = "p < 0.01", size = 3, face = "plain", family = "") + theme_bw()

risk_plot <- risk_plot +
  theme(panel.grid.major.x = element_blank()) +
  theme(panel.grid.major.y = element_line(linetype = 2, size = 0.4), panel.grid.minor.y = element_blank()) +
  theme(axis.text.x = element_text(colour = "black"), axis.text.y = element_text(colour = "black"))

pdf("../../figures/boxplot.pdf", width = 10, height = 4)
grid.arrange(return_plot, risk_plot, ncol = 2)
dev.off()