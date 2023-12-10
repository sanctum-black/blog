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
# Country Hierarchy
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
library(stringr)
library(lubridate)

# ------------------------------------------------------------------------------
# Define Global Variables & Parameters
# ------------------------------------------------------------------------------
# Directories
rDir <- "data/raw/"
utilDir <- file.path(rDir, "Utilities")

# Country List
# ------------------------------------------------------------------------------

# Load country list
df_countries <- read.csv(file.path(utilDir, "Country_Codes.csv"))
colnames(df_countries)

# Change column names
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
    "region_numeric_code" = "region.code",
    "sub_region_numeric_code" = "sub.region.code",
    "intermediate_region_code" = "intermediate.region.code"
  )

# Create simple country codes df
df_countries <- df_countries %>%
  select(country_name,
         iso3166_1_alpha_3,
         iso3166_1_numeric_code,
         region,
         region_numeric_code,
         sub_region,
         sub_region_numeric_code)

# International Organizations
# ------------------------------------------------------------------------------

# Get the name of all Excel sheets
sheet_names <- excel_sheets(file.path(utilDir, "International_Organizations.xlsx"))

# Iterate over each sheet
for(sheet in sheet_names) {
  # Read the sheet
  sheet_data <- read_excel(file.path(utilDir, "International_Organizations.xlsx"), sheet = sheet)
  # Check if countries in df_countries are present in the sheet
  df_countries[[sheet]] <- df_countries$iso3166_1_alpha_3 %in% sheet_data$country_code
}

# Check head
colnames(df_countries)

# Country Classification by Income
# ------------------------------------------------------------------------------

# Load country classification data
df_country_classification <- read_excel(file.path(utilDir, "Country_Development_Classifications.xlsx"))

# Replace unexisting values with NaN
df_country_classification <- df_country_classification %>%
  mutate_all(~na_if(., ".."))

# We'll only use the 2022 classification since most of the metrics will be from 2022
df_country_classification <- df_country_classification[, c("iso3166_1_alpha_3", "2022")] %>%
  rename("country_classification_2022" = "2022")

# Left merge dataframes
df_countries <- merge(df_countries,
                      df_country_classification,
                      by="iso3166_1_alpha_3",
                      all.x = TRUE)

# Write to csv file
# ------------------------------------------------------------------------------
write.csv(df_countries, file.path(utilDir, "Countries_Baseline.csv"), row.names = FALSE)

# EOF