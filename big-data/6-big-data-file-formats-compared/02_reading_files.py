# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 19:23:00 2023

@author: Pablo Aguirre

GitHub: https://github.com/pabloaguirrenck
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact

Part of Blog Article: 6-big-data-file-formats-compared
"""

# -------------------------------
# -------------------------------
# Introduction
# -------------------------------
# -------------------------------

# In this file, we will review different methods for reading different
# file formats using Python.

# -------------------------------
# -------------------------------
# Reading files with Python
# -------------------------------
# -------------------------------

# Importing all required modules beforehand
import csv
import numpy as np
import pandas as pd
from fastavro import reader
import pickle

# -------------------------------
# 1. CSV
# -------------------------------

# 1.1 Using the csv.reader() method
# -------------------------------

# Declare an empty list object
lol = []

# Define the file handler, and open in read mode
with open("outputs/02_dataset_method_2.csv", 'r') as file:
  csvreader = csv.reader(file)
  # Iterate over rows and append to list
  for row in csvreader:
      lol.append(row)
      
# Close the Text Wrapper object
file.close()

# Build a numpy.ndarray object from a list of lists
arr = np.array(lol)

# Build a pandas.DataFrame object from numpy.ndarray object
df = pd.DataFrame(arr[1:], columns = arr[0])

# 1.2 Using the pandas.read_csv() method
# -------------------------------

# Read the csv file and import to pandas.DataFrame object
df = pd.read_csv("outputs/02_dataset_method_2.csv")

# -------------------------------
# 2. TXT
# -------------------------------

# 2.1 Using the built-in Python file handler
# -------------------------------

# Declare an empty list object
lol = []

# Define the file handler, and open in read mode
with open("outputs/04_dataset_method_1.txt", 'r') as file:
    # Read the entire content and split with newlines
    content = file.read().split('\n')
    
    # For every newline, split in tab delimitors
    for entry in content:
        entry = entry.split('\t')
        # Append each splitted entry in list of lists
        lol.append(entry)

# Close the TextIOWrapper object
file.close()

# Return the results 
lol

# Remove last entry using inplace method .pop()
lol.pop()

# Convert list of lists to 
arr = np.array(lol)

# Convert arr to pandas.DataFrame object
df = pd.DataFrame(arr[1:], columns = arr[0])

# 2.2 Using the pandas.DataFrame.read_csv() method
# -------------------------------

# Read the txt file and import to pandas.DataFrame object
df = pd.read_csv("outputs/04_dataset_method_1.txt", sep = '\t')

# -------------------------------
# 3. Feather
# -------------------------------

# 3.1 Using pandas.DataFrame.read_feather() method
# -------------------------------

# Read the .feather file and import to pandas.DataFrame object
df = pd.read_feather("outputs/06_dataset_method_1.feather")

# -------------------------------
# 4. Parquet
# -------------------------------

# 4.1 Using pandas.read_parquet() method for non-partitioned files
# -------------------------------

# Read the parquet non-partitioned file and import to pandas.DataFrame object
df = pd.read_parquet("outputs/07_dataset_method_1.parquet")

# 4.2 Using pandas.read_parquet() for single and multi-partitioned files
# -------------------------------

# Read the parquet single-partitioned file and import to pandas.DataFrame object
df = pd.read_parquet("outputs/08_dataset_method_2.parquet")

# Read the parquet multi-partitioned file and import to pandas.DataFrame object
df = pd.read_parquet("outputs/09_dataset_method_3.parquet")


# -------------------------------
# 5. Avro
# -------------------------------

# 5.1 Using the fastavro reader method
# -------------------------------

# Declare an empty list of dictionaries
lod = []

# Use the Python file handler along with the fastavro reader method
with open('outputs/10_dataset_method_1.avro', 'rb') as fo:
    avro_reader = reader(fo)
    for record in avro_reader:
        lod.append(record)

# Close the BufferedReader object
fo.close()

# Convert list of dictionaries to DataFrame
df = pd.DataFrame.from_dict(lod)

# -------------------------------
# 6. Pickle
# -------------------------------

# 6.1 Using .pickle.load() to read from an open file
# -------------------------------

# Use the Python file handler
with open('outputs/11_dataset_method_1.pickle', 'rb') as file:
    my_pickled_object = pickle.load(file)

# Close the BufferedReader object
file.close()


