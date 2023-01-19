# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 19:23:00 2023

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



# -------------------------------
# 1. Reading files with Python
# -------------------------------

# -------------------------------
# 1.1 csv

# I. Reading csv files using csv.reader()

# Import csv module
import csv

# Open filename as csv.reader object
with open(filename, 'r') as csvfile:

	# Use csv.reader() method to convert object to iterable
    csvreader = csv.reader(csvfile)
    
    # Print first column values by iterating through rows in csvreader object
    for row in csvreader:
        print(row[0])


# II. Reading csv files using pandas.read_csv()

# Import Pandas module
import pandas as pd

# Read filename and save as pandas dataframe object df
df = pd.read_csv(filename)

# Get the first 5 elements
df.head()


# III. Reading csv files using numpy.loadfromtxt()



# IV. Reading csv files using csv.reader()


# -------------------------------
# 1.1 txt


# -------------------------------
# 1.1 JSON


# -------------------------------
# 1.1 Feather


# -------------------------------
# 1.1 Parquet


# -------------------------------
# 1.1 Avro


# -------------------------------
# 1.1 XML



