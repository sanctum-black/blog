# -------------------------------------------------------
## Created on Sat Apr 15 19:23:00 2023
## @author: Pablo Aguirre
## GitHub: https://github.com/pabloagn
## Website: https://pabloagn.com
## Contact: https://pabloagn.com/contact
## Part of Blog: probability-distributions-explained
# -------------------------------------------------------


# -------------------------------------------------------
# Install packages
# -------------------------------------------------------

# install.packages('extrafont')
# install.packages('ggplot2')

# -------------------------------------------------------
# Load packages
# -------------------------------------------------------

library(extrafont)
library(ggplot2)
library(glue)

# -------------------------------------------------------
# Set plot parameters
# -------------------------------------------------------

# Import fonts
font_import(paths = "C:/Users/Pablo/AppData/Local/MICROSOFT/Windows/Fonts")

# Register fonts for Windows bitmap output
loadfonts(device="win")

# Set font parameters
my_font <- "Cardo"
size_title <- 18
size_labels <- 16
size_axis <- 13
margin_x <- margin(t = 20)
margin_y <- margin(r = 30)
title_just <- 0.5
title_padding <- margin(10, 0, 10, 0)
color_font_main <- "#1A1A1A"
color_font_light <- "#4A4A4A"
color_panel_bg <- "#ebebeb"
color_plot_bg <- "#F2F2F2"

# Set chart parameters
point_size = 2

# Set export parameters
article_code = "B015A032"

# -------------------------------------------------------
# CDF - Discrete Uniform
# -------------------------------------------------------

# Define the possible outcomes
x <- 1:6

# Define the probabilities of each outcome
fx <- rep(1/6, 6)

# Calculate the cumulative probabilities
Fx <- cumsum(fx)

# Create the data frame
df <- data.frame(x = x, Fx = Fx)

# Create the CDF plot
p_tp <- ggplot(df, aes(x = x, y = Fx)) +
  geom_step() +
  geom_point(size = point_size) +
  labs(title = "CDF of a 6-sided dice roll",
       x = "Outcome",
       y = "Cumulative Probability") +
  theme(plot.title = element_text(family = my_font, size = size_title, hjust = title_just, margin = title_padding, color = color_font_main),
        axis.title.x = element_text(family = my_font, size = size_labels, margin = margin_x, color = color_font_main),
        axis.title.y = element_text(family = my_font, size = size_labels, margin = margin_y, color = color_font_main),
        axis.text = element_text(family = my_font, size = size_axis, color = color_font_light),
        panel.background = element_rect(fill = color_panel_bg, colour = NA),
        plot.background = element_rect(fill = "transparent", colour = NA)) +
  scale_y_continuous(limits = c(0, 1)) +
  scale_x_continuous(breaks = x)

p_bg <- ggplot(df, aes(x = x, y = Fx)) +
  geom_step() +
  geom_point(size = point_size) +
  labs(title = "CDF of a 6-sided dice roll",
       x = "Outcome",
       y = "Cumulative Probability") +
  theme(plot.title = element_text(family = my_font, size = size_title, hjust = title_just, margin = title_padding, color = color_font_main),
        axis.title.x = element_text(family = my_font, size = size_labels, margin = margin_x, color = color_font_main),
        axis.title.y = element_text(family = my_font, size = size_labels, margin = margin_y, color = color_font_main),
        axis.text = element_text(family = my_font, size = size_axis, color = color_font_light),
        panel.background = element_rect(fill = color_panel_bg, colour = NA),
        plot.background = element_rect(fill = color_plot_bg, colour = NA)) +
  scale_y_continuous(limits = c(0, 1)) +
  scale_x_continuous(breaks = x)

# Save plots to png file
ggsave(glue("outputs/{article_code}_plot1_tp.png"), plot = p_tp, width = 6, height = 4, dpi = 300)
ggsave(glue("outputs/{article_code}_plot1_bg.png"), plot = p_bg, width = 6, height = 4, dpi = 300)

# -------------------------------------------------------
# Bernoulli Distribution - Bernoulli Trials
# -------------------------------------------------------

# Set the success probability and number of trials
p <- 0.5
n <- 1000000

# Simulate a Bernoulli trial with n trials and success probability p
outcome <- rbinom(n, size = 1, prob = p)

# Print the outcome of the n trials
print(outcome)

# Calculate percentage of successes and failures
num_successes <- sum(outcome)
num_failures <- n - num_successes

perc_successes <- num_successes / n
perc_failures <- num_failures / n

# Print percentages
cat("Success Percentage: ",
    perc_successes,
    "\nFailure Percentage: ",
    perc_failures)


# Set the success probability
p <- 0.5

# Create a data frame with the possible outcomes and their probabilities
data <- data.frame(outcome = c(0, 1), probability = dbinom(c(0, 1), size = 1, prob = p))

# Plot the PMF using ggplot2
p2_tp <- ggplot(data, aes(x = outcome, y = probability)) +
  geom_col(fill = color_font_main, width = 0.5) +
  scale_x_continuous(breaks = c(0, 1), labels = c("0", "1")) +
  labs(title = glue("Bernoulli Distribution with p = {p}"),
       x = "Outcome",
       y = "Probability") +
  theme(plot.title = element_text(family = my_font, size = size_title, hjust = title_just, margin = title_padding, color = color_font_main),
        axis.title.x = element_text(family = my_font, size = size_labels, margin = margin_x, color = color_font_main),
        axis.title.y = element_text(family = my_font, size = size_labels, margin = margin_y, color = color_font_main),
        axis.text = element_text(family = my_font, size = size_axis, color = color_font_light),
        panel.background = element_rect(fill = color_panel_bg, colour = NA),
        plot.background = element_rect(fill = "transparent", colour = NA)) +
  scale_y_continuous(limits = c(0, 1))

p2_bg <- ggplot(data, aes(x = outcome, y = probability)) +
  geom_col(fill = color_font_main, width = 0.5) +
  scale_x_continuous(breaks = c(0, 1), labels = c("0", "1")) +
  labs(title = glue("Bernoulli Distribution with p = {p}"),
       x = "Outcome",
       y = "Probability") +
  theme(plot.title = element_text(family = my_font, size = size_title, hjust = title_just, margin = title_padding, color = color_font_main),
        axis.title.x = element_text(family = my_font, size = size_labels, margin = margin_x, color = color_font_main),
        axis.title.y = element_text(family = my_font, size = size_labels, margin = margin_y, color = color_font_main),
        axis.text = element_text(family = my_font, size = size_axis, color = color_font_light),
        panel.background = element_rect(fill = color_panel_bg, colour = NA),
        plot.background = element_rect(fill = color_plot_bg, colour = NA)) +
  scale_y_continuous(limits = c(0, 1))

ggsave(glue("outputs/{article_code}_plot2_tp.png"), plot = p2_tp, width = 6, height = 4, dpi = 300)
ggsave(glue("outputs/{article_code}_plot2_bg.png"), plot = p2_bg, width = 6, height = 4, dpi = 300)

# -------------------------------------------------------
# Binomial Distribution
# -------------------------------------------------------


