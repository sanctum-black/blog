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
# 1. Introduction
# -------------------------------

# In this file, we will review different methods for writing to different
# fiel formats using Python.

# -------------------------------
# 2. Creating an array of mixed data types
# -------------------------------

# Import NumPy module
import numpy as np

# Define headers
headers = ['Name', 'Age', 'Occupation', 'Country', 'State', 'City']

# Define rows
entry_1 = ['Joe', 20, 'Student', 'United States', 'Kansas', 'Kansas City']
entry_2 = ['Chloe', 37, 'Detective', 'United States', 'California', 'Los Angeles']
entry_3 = ['Dan', 39, 'Detective', 'United States', 'California', 'Los Angeles']

# Create array
arr = np.asarray([headers, entry_1, entry_2, entry_3])

# -------------------------------
# 3. Writing files with Python.
# -------------------------------

# -------------------------------
# 3.1 CSV
# -------------------------------

# 1. Using the numpy.tofile() method
# -------------------------------

# Export data to csv using numpy.tofile() method
arr.tofile('outputs/01_dataset_method_1.csv', sep = ',')


# 2. Using the numpy.savetext() method
# -------------------------------

# Export data to csv using numpy.savetext() method
np.savetxt('outputs/02_dataset_method_2.csv', arr, fmt = '%s', delimiter = ',', newline = '\n')


# 3. Using the pandas.DataFrame.to_csv() method
# -------------------------------

# Import pandas module
import pandas as pd

# Convert our array to a pandas.DataFrame object
# Extract data & columns separately
df = pd.DataFrame(data = arr[1:], columns = arr[:1][0])

# Export data to csv using pandas.DataFrame.to_csv() method
df.to_csv('outputs/03_dataset_method_3.csv', index = False)

# -------------------------------
# 3.2 TXT
# -------------------------------

# 1. Using the numpy.savetext() method
# -------------------------------

# Export data to txt using numpy.savetext() method
np.savetxt('outputs/04_dataset_method_1.txt', arr, fmt = '%s', delimiter = '\t', newline = '\n')

# 2. Using the pandas.DataFrame.to_csv() method
# -------------------------------

# Export data to txt using pandas.DataFrame.to_csv() method
df.to_csv('outputs/05_dataset_method_2.txt', sep = '\t', index = False)

# -------------------------------
# 3.3 Feather
# -------------------------------

# 1. Using pandas.DataFrame.to_feather() method
# -------------------------------

# Export data to feather using pandas.DataFrame.to_feather() method
df.to_feather('outputs/06_dataset_method_1.feather')

# -------------------------------
# 3.4 Parquet
# -------------------------------

# 1. Using pandas.DataFrame.to_parquet() without partitioning
# -------------------------------

# Use pandas.DataFrame.to_parquet() without partitioning
df.to_parquet('outputs/07_dataset_method_1.parquet')

# 2. Using pandas.DataFrame.to_parquet() with single partitioning
# -------------------------------

# Use pandas.DataFrame.to_parquet() with single partitioning
df.to_parquet('outputs/08_dataset_method_2.parquet', partition_cols = 'State')

# 3. Using pandas.DataFrame.to_parquet() with multiple partitioning
# -------------------------------

# Use pandas.DataFrame.to_parquet() with multi-partitioning
df.to_parquet('outputs/09_dataset_method_3.parquet', partition_cols = ['State', 'City'])


# -------------------------------
# 3.5 Avro
# -------------------------------

# 1. Using the fastavro module
# -------------------------------

# Import fastavro modules
from fastavro import writer, parse_schema

# Cast age to int type
df['Age'] = df['Age'].astype('int')

# Verify casting
df.dtypes

# Define the schema
schema = {
    'type': 'record',
    'name': 'dataset',
    'namespace': 'dataset',
    'doc': 'This schema consists of 1 int type and 7 string types',
    'fields': [
        {'name': 'Name', 'type': 'string'},
        {'name': 'Age', 'type': 'int'},
        {'name': 'Occupation', 'type': 'string'},
        {'name': 'Country', 'type': 'string'},
        {'name': 'State', 'type': 'string'},
        {'name': 'City', 'type': 'string'}
    ]
}

# Parse the schema
parsed_schema = parse_schema(schema)

# Convert pd.DataFrame to records (list of dictionaries)
records = df.to_dict('records')

# Write to Avro file
with open('outputs/10_dataset_method_1.avro', 'wb') as out:
    writer(out, parsed_schema, records)


# -------------------------------
# 2.6 Pickle
# -------------------------------

# 1. Using .pickle.dump() to write as an open file
# -------------------------------

# Import pickle library
import pickle

# Open a file to store the data
file = open('outputs/11_dataset_method_1.pickle', 'wb')

# Write open file to disk
pickle.dump(records, file)


# 2. Using .pickle.dumps() to write as a byte string
# -------------------------------

# Define a pickle object
my_pickled_object = pickle.dumps(records)

# Check the pickle object data type
type(my_pickled_object)

# Write byte string to disk
with open('outputs/12_dataset_method_2.pickle','wb') as out:
    out.write(my_pickled_object)

