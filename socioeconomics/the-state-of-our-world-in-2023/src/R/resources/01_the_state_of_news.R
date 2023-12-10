# BOF

# ------------------------------------------------------------------------------
# Created on Sat Nov 25 18:46:10 2023
# @author: Pablo Aguirre
# GitHub: https://github.com/pabloagn
# Website: https://pabloagn.com
# Contact: https://pabloagn.com/contact
# Part of Blog Article: the-state-of-our-world-in-2023-pt-1
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# The State of the News Today
# ------------------------------------------------------------------------------

# Load libraries
library(readr)
library(readxl)
library(dplyr)
library(tidyr)
library(data.table)
library(lubridate)
library(ggplot2)
library(ggalt)
library(RColorBrewer)
library(viridis)

# ------------------------------------------------------------------------------
# Define Global Variables & Parameters
# ------------------------------------------------------------------------------
# Directories
rDir <- "data/raw/"
w_FigDir <- "outputs/figures"
utilDir <- file.path(rDir, "Utilities")

# Plotting
color_black <- "#1a1a1a"
color_white <- "#f2f2f2"
color_gray <- "gray"

# Set up scheme as Viridis, with n colors
color_scheme <- viridis::viridis(3)

theme_set(theme_gray(base_size = 14) +
            theme(
              text = element_text(family = "Work Sans"),
              axis.text = element_text(color = color_black),
              plot.title = element_text(face = "plain", hjust = 0.5), # Reduced boldness of the title
              panel.background = element_rect(fill = "gray90"),
              panel.grid.major = element_line(color = "white"),
              panel.grid.minor = element_line(color = "white")
            ))

# Create visualizations
# ------------------------------------------------------------------------------

# Percentage who trust information in the news media
# in general versus news on each platform in each country.

# Load data
df_trust_news <- read.csv(file.path(rDir, "State_Of_The_News/data-2Sb0I.csv"))

# Rename cols
df_trust_news <- df_trust_news %>% rename(
  platform = Object.of.trust,
  general_news = News.in.general,
  platform_news = News.on.the.platform
)

# Set country as factor (keep order)
df_trust_news$country <- factor(df_trust_news$country, levels = rev(sort(unique(df_trust_news$country))))

# Create the dumbbell plot
trust_news <- ggplot(df_trust_news, aes(y = country, x = general_news, xend = platform_news, group = country)) +
  geom_dumbbell(
    size = 3,
    color = color_gray,
    colour_x = color_scheme[1],
    colour_xend = color_scheme[2]
  ) +
  geom_text(aes(label = sprintf("%.0f%%", general_news), x = ifelse(general_news > platform_news, general_news + 3, general_news - 3)), hjust = 0.5, vjust = 0.5, color = color_scheme[1]) +
  geom_text(aes(label = sprintf("%.0f%%", platform_news), x = ifelse(platform_news > general_news, platform_news + 3, platform_news - 3)), hjust = 0.5, vjust = 0.5, color = color_scheme[2]) +
  facet_wrap(~`platform`, scales = "free_y", ncol = 1) +
  scale_x_continuous(labels = scales::label_percent(scale = 1)) +
  labs(
    title = "Comparison of Trust in News: General vs Platform",
    x = "Trust Level (%)",
    y = "Country"
  )

# Save the plot
ggsave(file.path(w_FigDir, "dumbbell_plot.png"),
       plot = trust_news,
       width = 10,
       height = 10,
       dpi = 300
)

# EOF