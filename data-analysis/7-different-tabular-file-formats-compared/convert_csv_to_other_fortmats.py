# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:54:22 2023

@author: Pablo Aguirre

GitHub: https://github.com/pabloaguirrenck

Part of Blog Article: 7-different-tabular-file-formats-compared
"""

# -------------------------------
# Defining dataset path
# -------------------------------

filename = 'Chernobyl_ Chemical_Radiation.csv'

# -------------------------------
# Generating all other formats from DataFrame
# -------------------------------

# We have our dataset in csv format, but we want to
# have all other formats as well

# Import Pandas module
import pandas as pd

# Read filename and save as pandas dataframe object df
df = pd.read_csv(filename)

# I. Convert to 

