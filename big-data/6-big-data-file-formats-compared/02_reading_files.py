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
# 1. Creating an arraw of mixed data types
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
# 2. Writing files with Python.
# -------------------------------

# -------------------------------
# 2.1 csv
# -------------------------------

# 1. Using the numpy.tofile() method
# -------------------------------

# Export data to csv using numpy.tofile() method
arr.tofile('dataset_method_1.csv', sep = ',')


# 2. Using the numpy.savetext() method
# -------------------------------

# Export data to csv using numpy.savetext() method
np.savetxt('dataset_method_2.csv', arr, fmt = '%s', delimiter = ',', newline = '\n')


# 3. Using the pandas.DataFrame.to_csv() method
# -------------------------------

# Import pandas module
import pandas as pd

# Convert our array to a pandas.DataFrame object
# Extract data & columns separately
df = pd.DataFrame(data = arr[1:], columns = arr[:1][0])

# Export data to csv using pandas.DataFrame.to_csv() method
df.to_csv('dataset_method_3.csv', index = False)


# -------------------------------
# 2.2 txt
# -------------------------------

# 2. Using the numpy.savetext() method
# -------------------------------

# Export data to txt using numpy.savetext() method
np.savetxt('dataset_method_1.txt', arr, fmt = '%s', delimiter = '\t', newline = '\n')


# 3. Using the pandas.DataFrame.to_csv() method
# -------------------------------

# Convert our array to a pandas.DataFrame object
# Extract data & columns separately
df = pd.DataFrame(data = arr[1:], columns = arr[:1][0])

# Export data to txt using pandas.DataFrame.to_csv() method
df.to_csv('dataset_method_2.txt', sep = '\t', index = False)


# -------------------------------
# 2.3 Feather
# -------------------------------

# Export data to feather using pandas.DataFrame.to_feather() method
df.to_feather('dataset_method_1.feather')


# -------------------------------
# 2.4 Parquet
# -------------------------------

# Use pandas.DataFrame.to_parquet() without partitioning
df.to_parquet('dataset_method_1.parquet')

# Use pandas.DataFrame.to_parquet() with single partitioning
df.to_parquet('dataset_method_2.parquet', partition_cols = 'State')

# Use pandas.DataFrame.to_parquet() with multi-partitioning
df.to_parquet('dataset_method_3.parquet', partition_cols = ['State', 'City'])


# -------------------------------
# 2.5 Avro
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
with open('dataset_method_1.avro', 'wb') as out:
    writer(out, parsed_schema, records)


# -------------------------------
# 2.6 Pickle
# -------------------------------

# 1. Writing a .pickle file as an open file
# -------------------------------

# Import pickle library
import pickle

# Open a file to store the data
file = open('dataset_method_1.pickle', 'wb')

# Write open file to disk
pickle.dump(records, file)


# 2. Writing a .pickle file as a byte string
# -------------------------------

# Define a pickle object
my_pickled_object = pickle.dumps(records)

# Check the pickle object data type
type(my_pickled_object)

# Write byte string to disk
with open('dataset_method_2.pickle','wb') as out:
    out.write(my_pickled_object)






























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



