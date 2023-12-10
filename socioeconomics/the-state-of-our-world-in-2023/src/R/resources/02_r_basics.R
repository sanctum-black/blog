# ------------------------------------------------------------------------------
# Created on Sat Nov 25 18:46:10 2023
# @author: Pablo Aguirre
# GitHub: https://github.com/pabloagn
# Website: https://pabloagn.com
# Contact: https://pabloagn.com/contact
# Part of Blog Article: the-state-of-our-world-in-2023-pt-1
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# R Basics
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

# Define directories
rDir <- "data/raw/"
wDir <- "outputs"

# Define global params
min_year <- 1990
max_year <- 2022

# Data reading
# ------------------------------------------------------------------------------

# Load data using read.csv (Dataframe)
df_csv_dataframe <- read.csv(file.path(rDir,
                                       "GDP_Per_Capita",
                                       "API_NY.GDP.PCAP.PP.CD_DS2_en_csv_v2_6011310.csv"))

# Check object type
class(df_csv_dataframe)

# Load data using fread (data.table)
df_csv_datatable <- fread(file.path(rDir,
                                    "GDP_Per_Capita",
                                    "API_NY.GDP.PCAP.PP.CD_DS2_en_csv_v2_6011310.csv"),
                          header=TRUE)

# Check object type
class(df_csv_datatable)

# Load data using read_excel (Dataframe)
df_xlsx_dataframe <- read_excel(file.path(rDir,
                                          "Drug-Related_Crimes",
                                          "10.1._Drug_related_crimes.xlsx"),
                                sheet="Formal contact")

# Check object type
class(df_xlsx_dataframe)

# Transform data.frame to data.table from excel-read file
df_xlsx_datatable <- as.data.table(df_xlsx_dataframe)

# Check object type
class(df_xlsx_datatable)

# Data transformation for data.frame objects
# ------------------------------------------------------------------------------

# Check column names
colnames(df_csv_dataframe)

# Check object dimensions
dim(df_csv_dataframe)

# Number of cols
ncol(df_csv_dataframe)

# Number of rows
nrow(df_csv_dataframe)

# Check data types
sapply(df_csv_dataframe, typeof)

# Check data types using data.frame object
data_types <- data.frame(
  Column = names(df_csv_dataframe),
  Type = sapply(df_csv_dataframe, typeof)
  )

data_types

# Define base columns
base_cols <- c("Country.Name", "Country.Code", "Indicator.Name", "Indicator.Code")

# Create range of periods under study (using chars)
period_range <- as.character(seq(min_year, max_year, by=1))

# Prepend X
period_range <- paste0("X", period_range)

# Create col vector
df_cols <- c(base_cols, period_range)

# Subset by valid periods
df_csv_dataframe <- df_csv_dataframe[, df_cols]

# Filter by subset of countries
country_codes <- c("SGP", "UKR", "NOR", "MEX")
df_csv_dataframe <- df_csv_dataframe[df_csv_dataframe$Country.Code %in% country_codes,]

# Chain operations
singapore_average <- df_csv_dataframe %>%
  filter(Country.Code == "SGP") %>%
  select(X2020, X2021) %>%
  pivot_longer(cols = everything()) %>%
  summarize(Mean = mean(value))

sprintf("Average for Singapore metric is: %s.", singapore_average)

# Data transformation for data.table objects
# ------------------------------------------------------------------------------

# Select columns
country_codes <- c("MEX", "ARG", "BRA")
df_csv_datatable <- df_csv_datatable[df_csv_datatable$`Country Code` %in% country_codes,]

# Perform operations:
#   Get metrics for a specific year
#   Calculate the average
target_year <- "2010"
mean_metric <- mean(df_csv_datatable[,get(target_year)])
collapsed_countries <- paste(country_codes, collapse=', ')
sprintf("Average metric for %s is: %s.", collapsed_countries, mean_metric)

# Visualizations
# ------------------------------------------------------------------------------

# Reshape object to longer for better manipulation
df_long <- df_csv_dataframe %>%
  pivot_longer(cols = starts_with('X'),
               names_to = "Year",
               values_to = "Metric",
               names_prefix = "X")

# Cast years to integers
df_long$Year <- as.numeric(df_long$Year)

# Check head
head(df_long)

# Get indicator title
df_indicator <- unique(df_long$Indicator.Name)[1]

# A simple time series
ggplot(data = df_long,
       mapping = aes(x = Year, y = Metric, color = Country.Name)) +
  geom_line() +
  theme_gray() +
  labs(title = df_indicator,
       x = "Year",
       y = "USD (PPP)",
       color = "Country")