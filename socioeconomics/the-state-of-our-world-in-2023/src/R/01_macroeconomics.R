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
# 1. Macroeconomics
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------------------------
library(readr)
library(readxl)
library(writexl)
library(openxlsx)
library(dplyr)
library(tidyr)
library(data.table)
library(stringr)
library(lubridate)
library(car)
library(broom)
library(ggplot2)
library(ggalt)
library(RColorBrewer)
library(extrafont)
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

# ------------------------------------------------------------------------------
# GDP
# ------------------------------------------------------------------------------

# Includes the following indexes:
# - GDP Nominal
# - GDP PPP
# - GDP Per Capita PPP
# - GDP Growth Rate
# - GDP Per Capita Growth Rate

# Load data
df_gdp_nominal <- read_csv(file.path(rDir, "GDP_Nominal/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_6011335.csv"), show_col_types = FALSE)
df_gdp_ppp <- read_csv(file.path(rDir, "GDP_PPP/API_NY.GDP.MKTP.PP.CD_DS2_en_csv_v2_5996066.csv"), show_col_types = FALSE)
df_gdp_pc <- read_csv(file.path(rDir, "GDP_Per_Capita/API_NY.GDP.PCAP.PP.CD_DS2_en_csv_v2_6011310.csv"), show_col_types = FALSE)
df_gdp_gr <- read_csv(file.path(rDir, "GDP_Growth/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_5994650.csv"), show_col_types = FALSE)
df_gdp_pc_gr <- read_csv(file.path(rDir, "GDP_Per_Capita_Growth/API_NY.GDP.PCAP.KD.ZG_DS2_en_csv_v2_5994795.csv"), show_col_types = FALSE)

# Concatenate frames
df_gdp_all <- bind_rows(df_gdp_nominal, df_gdp_ppp, df_gdp_pc, df_gdp_gr, df_gdp_pc_gr)

# Remove Country Name since we don't need it
df_gdp_all <- df_gdp_all[, !names(df_gdp_all) %in% "Country Name"]









# EOF