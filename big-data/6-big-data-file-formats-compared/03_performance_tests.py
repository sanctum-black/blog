# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:48:18 2023

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

# In this file, we will review different performance metrics for writing &
# reading in different file formats.

# -------------------------------
# -------------------------------
# Preparing the data set
# -------------------------------
# -------------------------------

# Import all required modules beforehand
import csv
import numpy as np
import pandas as pd
from fastavro import reader, writer, parse_schema
import pickle
import time
import os
import shutil
from pathlib import Path

# # Load csv file as pandas.DataFrame object
# df = pd.read_csv('datasets/charts.csv')

# # Get the head of the object
# df_head = df.head()

# # Get the shape of the object
# df.shape

# # Singe we have nan values, we will remove them
# df = df.dropna()

# # Check the current data types and see if casting is required
# df.dtypes

# # Cast to required data types
# # Date is currently a string. We will cast it to Pandas DateTime in integer format
# # since Avro does not support original DateTime
# df['date'] = pd.to_datetime(df['date'])
# df['date'] = df['date'].apply(lambda x: x.value)

# # streams will be casted to integer type
# df['streams'] = df['streams'].astype('int')

# -------------------------------
# -------------------------------
# Writing performance tests
# -------------------------------
# -------------------------------


df = pd.read_csv('datasets/charts_head.csv')
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].apply(lambda x: x.value)
df['streams'] = df['streams'].astype('int')


# Declare a function for performing writing experiments
def writingPerformance(n, path, df):
    '''
    Parameters
    ----------
    n : int
        Number of trials.
    path : str
        Path for result writing.
    
    df : pandas.DataFrame
        DataFrame Objectn containing data set.

    Returns
    -------
    measured_vars : dict
        Execution time for each file format, with n number of trials.

    '''
    
    # Declare pd.Series() for storing the measured variables for each file format
    wtime_csv = pd.Series([], dtype='float64')
    wtime_txt = pd.Series([], dtype='float64')
    wtime_feather = pd.Series([], dtype='float64')
    wtime_parquet_NP = pd.Series([], dtype='float64')
    wtime_parquet_SP = pd.Series([], dtype='float64')
    wtime_parquet_MP = pd.Series([], dtype='float64')
    wtime_avro = pd.Series([], dtype='float64')
    wtime_pickle = pd.Series([], dtype='float64')

    # Declare a dictionary for storing all lists
    measured_vars_w = {}
    
    # -------------------------------
    # 1. CSV
    # -------------------------------
    for trial in range(n):
        
        print(f'CSV trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_csv(path + 'CSV' + '_' + str(trial) + '.csv')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_csv = pd.concat([pd.Series([exec_time]), wtime_csv])
        wtime_csv.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_w['01_CSV'] = wtime_csv
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'CSV' + '_' + str(trial) + '.csv')
    
    # -------------------------------
    # 2. TXT
    # -------------------------------
    for trial in range(n):
        
        print(f'TXT trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_csv(path + 'TXT' + '_' + str(trial) + '.txt', sep = '\t')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_txt = pd.concat([pd.Series([exec_time]), wtime_txt])
        wtime_txt.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_w['02_TXT'] = wtime_txt
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'TXT' + '_' + str(trial) + '.txt')
        
    # -------------------------------
    # 3. Feather
    # -------------------------------
    for trial in range(n):
        
        print(f'Feather trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_feather(path + 'Feather' + '_' + str(trial) + '.feather')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_feather = pd.concat([pd.Series([exec_time]), wtime_feather])
        wtime_feather.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_w['03_Feather'] = wtime_feather
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Feather' + '_' + str(trial) + '.feather')

    # -------------------------------
    # 4. Parquet non-partitioned
    # -------------------------------
    for trial in range(n):
        
        print(f'Parquet NP trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_parquet(path + 'Parquet_NP' + '_' + str(trial) + '.parquet')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_parquet_NP = pd.concat([pd.Series([exec_time]), wtime_parquet_NP])
        wtime_parquet_NP.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_w['04_Parquet_NP'] = wtime_parquet_NP
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Parquet_NP' + '_' + str(trial) + '.parquet')

    # -------------------------------
    # 5. Parquet single-partitioned
    # -------------------------------
    for trial in range(n):
        
        print(f'Parquet SP trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_parquet(path + 'Parquet_SP' + '_' + str(trial) + '.parquet', partition_cols = ['region'])
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_parquet_SP = pd.concat([pd.Series([exec_time]), wtime_parquet_SP])
        wtime_parquet_SP.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_w['05_Parquet_SP'] = wtime_parquet_SP
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        shutil.rmtree(path + 'Parquet_SP' + '_' + str(trial) + '.parquet')

    # -------------------------------
    # 6. Parquet multi-partitioned
    # -------------------------------
    for trial in range(n):
        
        print(f'Parquet MP trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_parquet(path + 'Parquet_MP' + '_' + str(trial) + '.parquet', partition_cols = ['region', 'trend'])
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_parquet_MP = pd.concat([pd.Series([exec_time]), wtime_parquet_MP])
        wtime_parquet_MP.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_w['06_Parquet_MP'] = wtime_parquet_MP
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        shutil.rmtree(path + 'Parquet_MP' + '_' + str(trial) + '.parquet')

    # -------------------------------
    # 7. Avro
    # -------------------------------
    # Define the schema
    schema = {
        'type': 'record',
        'name': 'performance_comp',
        'namespace': 'performance_comp',
        'doc': 'This schema consists of 2 int types, 1 datetime type and 6 string types',
        'fields': [
            {'name': 'title', 'type': 'string'},
            {'name': 'rank', 'type': 'int'},
            {'name': 'date', 'type': 'long'},
            {'name': 'artist', 'type': 'string'},
            {'name': 'url', 'type': 'string'},
            {'name': 'region', 'type': 'string'},
            {'name': 'chart', 'type': 'string'},
            {'name': 'trend', 'type': 'string'},
            {'name': 'streams', 'type': 'int'}
        ]
    }
    
    # Parse the schema
    parsed_schema = parse_schema(schema)

    # Convert pd.DataFrame to records (list of dictionaries)
    records = df.to_dict('records')
    
    # Write to Avro file
    for trial in range(n):
        
        print(f'Avro trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        with open(path + 'Avro' + '_' + str(trial) + '.avro', 'wb') as file:
            writer(file, parsed_schema, records)

        file.close()
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_avro = pd.concat([pd.Series([exec_time]), wtime_avro])
        wtime_avro.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_w['07_Avro'] = wtime_avro
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Avro' + '_' + str(trial) + '.avro')
    

    # -------------------------------
    # 8. Pickle open file
    # -------------------------------
    for trial in range(n):
        
        print(f'Pickle trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_feather(path + 'Pickle' + '_' + str(trial) + '.pickle')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_pickle = pd.concat([pd.Series([exec_time]), wtime_pickle])
        wtime_pickle.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_w['08_Pickle'] = wtime_pickle
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Pickle' + '_' + str(trial) + '.pickle')

    return measured_vars_w

# Declare a function for performing writing experiments
def readingPerformance(n, path, df):
    '''
    Parameters
    ----------
    n : int
        Number of trials.
    path : str
        Path for result writing.
    
    df : pandas.DataFrame
        DataFrame Objectn containing data set.

    Returns
    -------
    measured_vars : dict
        Execution time for each file format, with n number of trials.

    '''
    
    # Declare pd.Series() for storing the measured variables for each file format
    rtime_csv = pd.Series([], dtype='float64')
    rtime_txt = pd.Series([], dtype='float64')
    rtime_feather = pd.Series([], dtype='float64')
    rtime_parquet_NP = pd.Series([], dtype='float64')
    rtime_parquet_SP = pd.Series([], dtype='float64')
    rtime_parquet_MP = pd.Series([], dtype='float64')
    rtime_avro = pd.Series([], dtype='float64')
    rtime_pickle = pd.Series([], dtype='float64')

    # Declare a dictionary for storing all lists
    measured_vars_r = {}
    
    # -------------------------------
    # 1. CSV
    # -------------------------------
    for trial in range(n):
        
        print(f'CSV trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_csv(path + 'CSV' + '_' + str(trial) + '.csv')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_csv = pd.concat([pd.Series([exec_time]), rtime_csv])
        rtime_csv.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_r['01_CSV'] = rtime_csv
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'CSV' + '_' + str(trial) + '.csv')
    
    # -------------------------------
    # 2. TXT
    # -------------------------------
    for trial in range(n):
        
        print(f'TXT trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_csv(path + 'TXT' + '_' + str(trial) + '.txt', sep = '\t')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_txt = pd.concat([pd.Series([exec_time]), rtime_txt])
        rtime_txt.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_r['02_TXT'] = rtime_txt
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'TXT' + '_' + str(trial) + '.txt')
        
    # -------------------------------
    # 3. Feather
    # -------------------------------
    for trial in range(n):
        
        print(f'Feather trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_feather(path + 'Feather' + '_' + str(trial) + '.feather')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_feather = pd.concat([pd.Series([exec_time]), rtime_feather])
        rtime_feather.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_r['03_Feather'] = rtime_feather
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Feather' + '_' + str(trial) + '.feather')

    # -------------------------------
    # 4. Parquet non-partitioned
    # -------------------------------
    for trial in range(n):
        
        print(f'Parquet NP trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_parquet(path + 'Parquet_NP' + '_' + str(trial) + '.parquet')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_parquet_NP = pd.concat([pd.Series([exec_time]), rtime_parquet_NP])
        rtime_parquet_NP.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_r['04_Parquet_NP'] = rtime_parquet_NP
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Parquet_NP' + '_' + str(trial) + '.parquet')

    # -------------------------------
    # 5. Parquet single-partitioned
    # -------------------------------
    for trial in range(n):
        
        print(f'Parquet SP trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_parquet(path + 'Parquet_SP' + '_' + str(trial) + '.parquet', partition_cols = ['region'])
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_parquet_SP = pd.concat([pd.Series([exec_time]), rtime_parquet_SP])
        rtime_parquet_SP.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_r['05_Parquet_SP'] = rtime_parquet_SP
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        shutil.rmtree(path + 'Parquet_SP' + '_' + str(trial) + '.parquet')

    # -------------------------------
    # 6. Parquet multi-partitioned
    # -------------------------------
    for trial in range(n):
        
        print(f'Parquet MP trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_parquet(path + 'Parquet_MP' + '_' + str(trial) + '.parquet', partition_cols = ['region', 'trend'])
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_parquet_MP = pd.concat([pd.Series([exec_time]), rtime_parquet_MP])
        rtime_parquet_MP.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_r['06_Parquet_MP'] = rtime_parquet_MP
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        shutil.rmtree(path + 'Parquet_MP' + '_' + str(trial) + '.parquet')

    # -------------------------------
    # 7. Avro
    # -------------------------------
    # Define the schema
    schema = {
        'type': 'record',
        'name': 'performance_comp',
        'namespace': 'performance_comp',
        'doc': 'This schema consists of 2 int types, 1 datetime type and 6 string types',
        'fields': [
            {'name': 'title', 'type': 'string'},
            {'name': 'rank', 'type': 'int'},
            {'name': 'date', 'type': 'long'},
            {'name': 'artist', 'type': 'string'},
            {'name': 'url', 'type': 'string'},
            {'name': 'region', 'type': 'string'},
            {'name': 'chart', 'type': 'string'},
            {'name': 'trend', 'type': 'string'},
            {'name': 'streams', 'type': 'int'}
        ]
    }
    
    # Parse the schema
    parsed_schema = parse_schema(schema)

    # Convert pd.DataFrame to records (list of dictionaries)
    records = df.to_dict('records')
    
    # Write to Avro file
    for trial in range(n):
        
        print(f'Avro trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        with open(path + 'Avro' + '_' + str(trial) + '.avro', 'wb') as file:
            writer(file, parsed_schema, records)

        file.close()
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_avro = pd.concat([pd.Series([exec_time]), rtime_avro])
        rtime_avro.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_r['07_Avro'] = rtime_avro
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Avro' + '_' + str(trial) + '.avro')
    

    # -------------------------------
    # 8. Pickle open file
    # -------------------------------
    for trial in range(n):
        
        print(f'Pickle trial {trial} of {n} started...')
        # Start timer
        start = time.time()
        
        # Write to file
        df.to_feather(path + 'Pickle' + '_' + str(trial) + '.pickle')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_pickle = pd.concat([pd.Series([exec_time]), rtime_pickle])
        rtime_pickle.reset_index(drop = True)
        
        # Add measurements to dictionary
        measured_vars_r['08_Pickle'] = rtime_pickle
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Pickle' + '_' + str(trial) + '.pickle')

    return measured_vars_r

def analysis(n, path, df):
    '''
    Parameters
    ----------
    n : int
        Number of trials.
    path : str
        Path for result writing.
    
    df : pandas.DataFrame
        DataFrame Objectn containing data set.

    Returns
    -------
    measured_vars_w : dict
        Writing time of each file format, with n number of trials.
     
    measured_vars_r : dict
        Reading time of each file format, with n number of trials.
        
    stat_dw : dict
        Statistical description of measured writing times for all formats.
        
    stat_dr : dict
        Statistical description of measured reading times for all formats. 
        
    size_d : dict
        Output size description of measured times for all formats.
    '''
    
    # Define all tests for including in statistical description
    tests = ['01_CSV',
             '02_TXT',
             '03_Feather',
             '04_Parquet_NP',
             '05_Parquet_SP',
             '06_Parquet_MP',
             '07_Avro',
             '08_Pickle']
    
    # -------------------------------
    # Writing Analysis
    # -------------------------------
    
    # Perform writing experiment and get measured_vars_w dictionary
    measured_vars_w = writingPerformance(n, path, df)
    
    # Define statistical results dict
    stat_dw = {}
    
    # Statistical Description
    
    # Extract each set of values, describe them and save them in a new dict
    for i in tests:
        stat_v = measured_vars_w[i].describe()
        stat_dw[i] = stat_v
    
    # -------------------------------
    # Reading Analysis
    # -------------------------------
    
    # Perform reading experiment and get measured_vars_r dictionary
    measured_vars_r = readingPerformance(n, path, df)
    
    # Define statistical results dict
    stat_dr = {}
    
    # Statistical Description
    
    # Extract each set of values, describe them and save them in a new dict
    for i in tests:
        stat_v = measured_vars_r[i].describe()
        stat_dr[i] = stat_v
    
    # -------------------------------
    # File Size Analysis
    # -------------------------------
    
    # Define size results dict
    size_d = {}
    
    # Calculate file sizes
    size_d['01_CSV'] = os.path.getsize(path + 'CSV' + '_' + str(n-1) + '.csv') / (1024)
    size_d['02_TXT'] = os.path.getsize(path + 'TXT' + '_' + str(n-1) + '.txt') / (1024)
    size_d['03_Feather'] = os.path.getsize(path + 'Feather' + '_' + str(n-1) + '.feather') / (1024)
    size_d['04_Parquet_NP'] = os.path.getsize(path + 'Parquet_NP' + '_' + str(n-1) + '.parquet') / (1024)
    size_d['07_Avro'] = os.path.getsize(path + 'Avro' + '_' + str(n-1) + '.avro') / (1024)
    size_d['08_Pickle'] = os.path.getsize(path + 'Pickle' + '_' + str(n-1) + '.pickle') / (1024)
    
    # Calculate dir sizes
    path_Parquet_SP = Path(path + 'Parquet_SP_19.parquet')
    size_d['05_Parquet_SP'] = sum(f.stat().st_size for f in path_Parquet_SP.glob('**/*') if f.is_file()) / (1024)
    
    path_Parquet_MP = Path(path + 'Parquet_MP_19.parquet')
    size_d['06_Parquet_MP'] = sum(f.stat().st_size for f in path_Parquet_MP.glob('**/*') if f.is_file()) / (1024)
        

        
    
    # Return a dictionary including the actual measured time values of all methods
    # Return a dictionary including the statistical description of all methods
    return measured_vars_w, measured_vars_r, stat_dw, stat_dr, size_d


# Define performance tests output path
path = 'performance_tests/'

# Define n number of trials
n = 20

# Call analysis function
measured_vars_w, measured_vars_r, stat_dw, stat_dr, size_d = analysis(n, path, df)

# I'm only missing reading time calculation and final charts



    