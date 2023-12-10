# ------------------------------------------------------------------------------
# Created on Sat Nov 25 18:46:10 2023
# @author: Pablo Aguirre
# GitHub: https://github.com/pabloagn
# Website: https://pabloagn.com
# Contact: https://pabloagn.com/contact
# Part of Blog Article: the-state-of-our-world-in-2023
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Install & import libraries
# ------------------------------------------------------------------------------

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
                       "ggplot2",
                       "ggalt",
                       "RColorBrewer",
                       "extrafont",
                       "viridis")

for (package in required_packages) {
  # We will check if the package is loaded (hence installed)
  if (!require(package, character.only = TRUE)) {
    install.packages(package)
  }
}

# Snapshot the environment with renv
renv::snapshot()