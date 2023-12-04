# ------------------------------------------------------------------------------
# Economic Overview
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Created on Sat Nov 25 18:46:10 2023
# @author: Pablo Aguirre
# GitHub: https://github.com/pabloagn
# Website: https://pabloagn.com
# Contact: https://pabloagn.com/contact
# Part of Blog Article: the-state-of-our-world-in-2023-pt-1
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Install & import libraries
# ------------------------------------------------------------------------------

# Required packages:

# Reading & writing
# readr
# readxr
# arrow
# writexl
# openxlsx

# Data manipulation
# dplyr
# tidyr
# data.table
# stringr
# lubridate

# Statistical Analysis
# car
# broom

# Data visualization
# ggplot2

# Define packages to install
required_packages <- c("readr",
                       "readxl",
                       "arrow",
                       "writexl",
                       "openxlsx",
                       "dplyr",
                       "tidyr",
                       "data.table",
                       "stringr",
                       "lubridate",
                       "car",
                       "broom",
                       "ggplot2")

for (package in required_packages) {
  # We will check if the package is loaded (hence installed)
  if (!require(package, character.only = TRUE)) {
    install.packages(package)
    library(package, character.only = TRUE)
  }
}

# ------------------------------------------------------------------------------
# Define Variables
# ------------------------------------------------------------------------------
rDir <- "inputs"
utilDir <- file.path(rDir, "Utilities")

# ------------------------------------------------------------------------------
# 0. Preparations
# ------------------------------------------------------------------------------

# Rules:
  # All column names go in snake_case
  # All dataframe names go in snake_case, prepended by df

# Country List
# ------------------------------------------------------------------------------

# Load country list
df_countries <- read.csv(file.path(utilDir, "Country_Codes.csv"))
colnames(df_countries)

# Change column names (using chain operator)
# https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
df_countries <- df_countries %>%
  rename(
    "country_name" = "name",
    "iso3166_1_alpha_2" = "alpha.2",
    "iso3166_1_alpha_3" = "alpha.3",
    "iso3166_1_numeric_code" = "country.code",
    "iso3166_2_subdiv" = "iso_3166.2",
    "sub_region" = "sub.region",
    "intermediate_region" = "intermediate.region",
    "region_code" = "region.code",
    "sub_region_code" = "sub.region.code",
    "intermediate_region_code" = "intermediate.region.code"
  )

# Create simple country codes df
df_country_codes <- df_countries %>% select(country_name, iso3166_1_alpha_2, iso3166_1_alpha_3)

# International Organizations
# ------------------------------------------------------------------------------

# Get the name of all Excel sheets
sheet_names <- excel_sheets(file.path(utilDir, "International_Organizations.xlsx"))

# Iterate over each sheet
for(sheet in sheet_names) {
  # Read the sheet
  sheet_data <- read_excel(file.path(utilDir, "International_Organizations.xlsx"), sheet = sheet)
  # Check if countries in df_countries are present in the sheet
  df_countries[[sheet]] <- df_countries$country_name %in% sheet_data$country_name
}

# Country Classification by Income
# ------------------------------------------------------------------------------

# Load country classification data
df_country_classification <- read_excel(file.path(utilDir, "Country_Development_Classifications.xlsx"))

# Replace inexisting values with NaN
df_country_classification <- df_country_classification %>%
  mutate_all(~na_if(., ".."))

# ------------------------------------------------------------------------------
# 1. Macroeconomics
# ------------------------------------------------------------------------------

# GDP
# ------------------------------------------------------------------------------

# Includes the following idexes:
# - GDP Nominal
# - GDP PPP
# - GDP Per Capita PPP
# - GDP Growth Rate
# - GDP Per Capita Growth Rate

# Load data
df_gdp_nominal <- read_csv(file.path(rDir,"GDP_Nominal/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_6011335.csv"), show_col_types = FALSE)
df_gdp_ppp <- read_csv(file.path(rDir, "GDP_PPP/API_NY.GDP.MKTP.PP.CD_DS2_en_csv_v2_5996066.csv"), show_col_types = FALSE)
df_gdp_pc <- read_csv(file.path(rDir, "GDP_Per_Capita/API_NY.GDP.PCAP.PP.CD_DS2_en_csv_v2_6011310.csv"), show_col_types = FALSE)
df_gdp_gr <- read_csv(file.path(rDir, "GDP_Growth/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_5994650.csv"), show_col_types = FALSE)
df_gdp_pc_gr <- read_csv(file.path(rDir, "GDP_Per_Capita_Growth/API_NY.GDP.PCAP.KD.ZG_DS2_en_csv_v2_5994795.csv"), show_col_types = FALSE)

# Concatenate frames
df_gdp_all <- bind_rows(df_gdp_nominal, df_gdp_ppp, df_gdp_pc, df_gdp_gr, df_gdp_pc_gr)

# Remove Country Name since we don't need it
df_gdp_all <- df_gdp_all[,!names(df_gdp_all) %in% "Country Name"]










