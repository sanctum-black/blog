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
# Importing the required modules
# -------------------------------
# -------------------------------

# Import all required modules beforehand

# File manipulation modules
import pandas as pd
from fastavro import reader, writer, parse_schema
import pickle
import openpyxl

# Performance measurement modules
import time

# System utility modules
import os
import shutil
from pathlib import Path

# Plotting modules
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# -------------------------------
# Defining plot parameters
# -------------------------------
# -------------------------------

# Before anything else, delete the Matplotlib
# font cache directory if it exists, to ensure
# custom font propper loading
try:
    shutil.rmtree(matplotlib.get_cachedir())
except FileNotFoundError:
    pass

# Define main color as hex
color_main = '#1a1a1a'

# Define title & label padding
text_padding = 18

# Define font sizes
title_font_size = 17
label_font_size = 14

# Define rc params
plt.rcParams['figure.figsize'] = [14.0, 7.0]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['grid.color'] = 'k'
plt.rcParams['grid.linestyle'] = ':'
plt.rcParams['grid.linewidth'] = 0.5
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Lora']

# -------------------------------
# -------------------------------
# Preparing the dataset
# -------------------------------
# -------------------------------

# Load csv file as pandas.DataFrame object
df = pd.read_csv('datasets/charts.csv')

# Get the head of the object
df_head = df.head()

# Get the shape of the object
df.shape

# Singe we have nan values, we will remove them
df = df.dropna()

# Check the current data types and see if casting is required
df.dtypes

# Cast to required data types
# Date is currently a string. We will cast it to Pandas DateTime in integer format
# since Avro does not support original DateTime
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].apply(lambda x: x.value)

# Streams will be casted to integer type
df['streams'] = df['streams'].astype('int')

# Finally, reset index since .feather does not support
# serializing a non-default index
df = df.reset_index(drop = True)

# -------------------------------
# -------------------------------
# Performance tests
# -------------------------------
# -------------------------------

# Define number of trials n
n = 20

# Define performance tests output path
path = 'performance_tests/'

# -------------------------------
# Writing performance tests
# -------------------------------

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
        DataFrame Object containing data set.

    Returns
    -------
    measured_vars_w : dict
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

    # Declare a dictionary for storing all series
    measured_vars_w = {}
    
    # -------------------------------
    # 1. CSV
    # -------------------------------
    for trial in range(n):
        
        # Start trial
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
        
    # Define series title
    wtime_csv.name = 'Writing Time [s]'
    
    # Add measurements to dictionary
    measured_vars_w['01_CSV'] = wtime_csv.reset_index(drop = True)
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'CSV' + '_' + str(trial) + '.csv')
    
    # -------------------------------
    # 2. TXT
    # -------------------------------
    for trial in range(n):
        
        # Start trial
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
    
    # Define series title
    wtime_txt.name = 'Writing Time [s]'
    
    # Add measurements to dictionary
    measured_vars_w['02_TXT'] = wtime_txt.reset_index(drop = True)
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'TXT' + '_' + str(trial) + '.txt')
        
    # -------------------------------
    # 3. Feather
    # -------------------------------
    for trial in range(n):
        
        # Start trial
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
        
    # Define series title
    wtime_feather.name = 'Writing Time [s]'
        
    # Add measurements to dictionary
    measured_vars_w['03_Feather'] = wtime_feather.reset_index(drop = True)
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Feather' + '_' + str(trial) + '.feather')

    # -------------------------------
    # 4. Parquet non-partitioned
    # -------------------------------
    for trial in range(n):
        
        # Start trial
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
        
    # Define series title
    wtime_parquet_NP.name = 'Writing Time [s]'
        
    # Add measurements to dictionary
    measured_vars_w['04_Parquet_NP'] = wtime_parquet_NP.reset_index(drop = True)
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Parquet_NP' + '_' + str(trial) + '.parquet')

    # -------------------------------
    # 5. Parquet single-partitioned
    # -------------------------------
    for trial in range(n):
        
        # Start trial
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
        
    # Define series title
    wtime_parquet_SP.name = 'Writing Time [s]'
        
    # Add measurements to dictionary
    measured_vars_w['05_Parquet_SP'] = wtime_parquet_SP.reset_index(drop = True)
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        shutil.rmtree(path + 'Parquet_SP' + '_' + str(trial) + '.parquet')

    # -------------------------------
    # 6. Parquet multi-partitioned
    # -------------------------------
    for trial in range(n):
        
        # Start trial
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
        
    # Define series title
    wtime_parquet_MP.name = 'Writing Time [s]'
        
    # Add measurements to dictionary
    measured_vars_w['06_Parquet_MP'] = wtime_parquet_MP.reset_index(drop = True)
        
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
    
    for trial in range(n):
        
        # Start trial
        print(f'Avro trial {trial} of {n} started...')
        
        # Start timer
        start = time.time()
        
        # Write to Avro file
        with open(path + 'Avro' + '_' + str(trial) + '.avro', 'wb') as file:
            writer(file, parsed_schema, records)

        file.close()
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_avro = pd.concat([pd.Series([exec_time]), wtime_avro])
        
    # Define series title
    wtime_avro.name = 'Writing Time [s]'
        
    # Add measurements to dictionary
    measured_vars_w['07_Avro'] = wtime_avro.reset_index(drop = True)
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Avro' + '_' + str(trial) + '.avro')
    

    # -------------------------------
    # 8. Pickle open file
    # -------------------------------
    for trial in range(n):
        
        # Start trial
        print(f'Pickle trial {trial} of {n} started...')
        
        # Convert pd.DataFrame to records (list of dictionaries)
        records = df.to_dict('records')
        
        # Start timer
        start = time.time()
        
        file = open(path + 'Pickle' + '_' + str(trial) + '.pickle', 'wb')

        # Write open file to disk
        pickle.dump(records, file)

        file.close()
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        wtime_pickle = pd.concat([pd.Series([exec_time]), wtime_pickle])
        
    # Define series title
    wtime_pickle.name = 'Writing Time [s]'
        
    # Add measurements to dictionary
    measured_vars_w['08_Pickle'] = wtime_pickle.reset_index(drop = True)
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Pickle' + '_' + str(trial) + '.pickle')

    return measured_vars_w

# -------------------------------
# Reading performance tests
# -------------------------------

# Declare a function for performing reading experiments
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
    measured_vars_r : dict
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

    # Declare a dictionary for storing all series
    measured_vars_r = {}
    
    # -------------------------------
    # 1. CSV
    # -------------------------------
    for trial in range(n):
        
        # Start trial
        print(f'CSV trial {trial} of {n} started...')
        
        # Start timer
        start = time.time()
        
        # Read from file
        df = pd.read_csv(path + 'CSV' + '_' + str(n-1) + '.csv')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_csv = pd.concat([pd.Series([exec_time]), rtime_csv])
        
        # Delete file from memory
        del df
        
    # Define series title
    rtime_csv.name = 'Reading Time [s]'
        
    # Add measurements to dictionary
    measured_vars_r['01_CSV'] = rtime_csv.reset_index(drop = True)
    
    # -------------------------------
    # 2. TXT
    # -------------------------------
    for trial in range(n):
        
        # Start trial
        print(f'TXT trial {trial} of {n} started...')
        
        # Start timer
        start = time.time()
        
        # Read from file
        df = pd.read_csv(path + 'TXT' + '_' + str(n-1) + '.txt', sep = '\t')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_txt = pd.concat([pd.Series([exec_time]), rtime_txt])
        
        # Delete file from memory
        del df
            
    # Define series title
    rtime_txt.name = 'Reading Time [s]'
            
    # Add measurements to dictionary
    measured_vars_r['02_TXT'] = rtime_txt.reset_index(drop = True)
        
    # -------------------------------
    # 3. Feather
    # -------------------------------
    for trial in range(n):
        
        # Start trial
        print(f'Feather trial {trial} of {n} started...')
        
        # Start timer
        start = time.time()
        
        # Read from file
        df = pd.read_feather(path + 'Feather' + '_' + str(n-1) + '.feather')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_feather = pd.concat([pd.Series([exec_time]), rtime_feather])
        
        # Delete file from memory
        del df
            
    # Define series title
    rtime_feather.name = 'Reading Time [s]'
            
    # Add measurements to dictionary
    measured_vars_r['03_Feather'] = rtime_feather.reset_index(drop = True)

    # -------------------------------
    # 4. Parquet non-partitioned
    # -------------------------------
    for trial in range(n):
        
        # Start trial
        print(f'Parquet NP trial {trial} of {n} started...')
        
        # Start timer
        start = time.time()
        
        # Read from file
        df = pd.read_parquet(path + 'Parquet_NP' + '_' + str(n-1) + '.parquet')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_parquet_NP = pd.concat([pd.Series([exec_time]), rtime_parquet_NP])
        
        # Delete file from memory
        del df
            
    # Define series title
    rtime_parquet_NP.name = 'Reading Time [s]'
            
    # Add measurements to dictionary
    measured_vars_r['04_Parquet_NP'] = rtime_parquet_NP.reset_index(drop = True)

    # -------------------------------
    # 5. Parquet single-partitioned
    # -------------------------------
    for trial in range(n):
        
        # Start trial
        print(f'Parquet SP trial {trial} of {n} started...')
        
        # Start timer
        start = time.time()
        
        # Read from file
        df = pd.read_parquet(path + 'Parquet_SP' + '_' + str(n-1) + '.parquet')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_parquet_SP = pd.concat([pd.Series([exec_time]), rtime_parquet_SP])
        
        # Delete file from memory
        del df
            
    # Define series title
    rtime_parquet_SP.name = 'Reading Time [s]'
            
    # Add measurements to dictionary
    measured_vars_r['05_Parquet_SP'] = rtime_parquet_SP.reset_index(drop = True)

    # -------------------------------
    # 6. Parquet multi-partitioned
    # -------------------------------
    for trial in range(n):
        
        # Start trial
        print(f'Parquet MP trial {trial} of {n} started...')
        
        # Start timer
        start = time.time()
        
        # Read from file
        df = pd.read_parquet(path + 'Parquet_MP' + '_' + str(n-1) + '.parquet')
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_parquet_MP = pd.concat([pd.Series([exec_time]), rtime_parquet_MP])
        
        # Delete file from memory
        del df
            
    # Define series title
    rtime_parquet_MP.name = 'Reading Time [s]'
            
    # Add measurements to dictionary
    measured_vars_r['06_Parquet_MP'] = rtime_parquet_MP.reset_index(drop = True)

    # -------------------------------
    # 7. Avro
    # -------------------------------
    
    for trial in range(n):
        
        # Start trial
        print(f'Avro trial {trial} of {n} started...')
        
        # Define list of dictionaries
        lod = []
        
        # Start timer
        start = time.time()
        
        # Read from Avro file
        with open(path + 'Avro' + '_' + str(n-1) + '.avro', 'rb') as fo:
            avro_reader = reader(fo)
            
            for record in avro_reader:
                lod.append(record)

        # Close the BufferedReader object
        fo.close()

        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_avro = pd.concat([pd.Series([exec_time]), rtime_avro])
        
        # Delete file from memory
        del lod
            
    # Define series title
    rtime_avro.name = 'Reading Time [s]'
            
    # Add measurements to dictionary
    measured_vars_r['07_Avro'] = rtime_avro.reset_index(drop = True)
    
    # -------------------------------
    # 8. Pickle open file
    # -------------------------------
    for trial in range(n):
        
        # Start trial
        print(f'Pickle trial {trial} of {n} started...')
        
        # Start timer
        start = time.time()
        
        # Read from file
        with open(path + 'Pickle' + '_' + str(n-1) + '.pickle', 'rb') as file:
            my_pickled_object = pickle.load(file)

        # Close the BufferedReader object
        file.close()
        
        # End timer
        end = time.time()
        
        # Calculate execution time
        exec_time = end - start
        
        # Append time to series
        rtime_pickle = pd.concat([pd.Series([exec_time]), rtime_pickle])
        
        # Delete file from memory
        del my_pickled_object
             
    # Define series title
    rtime_pickle.name = 'Reading Time [s]'
           
    # Add measurements to dictionary
    measured_vars_r['08_Pickle'] = rtime_pickle.reset_index(drop = True)

    return measured_vars_r

# -------------------------------
# Analysis
# -------------------------------

# Declare a function for performing results analysis
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
        Statistical description of measured file/folder sizes for all formats. 
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
    
    # Statistical Description for Writing
    
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
    
    # Statistical Description for Reading
    
    # Extract each set of values, describe them and save them in a new dict
    for i in tests:
        stat_v = measured_vars_r[i].describe()
        stat_dr[i] = stat_v
    
    # -------------------------------
    # File Size Analysis
    # -------------------------------
    
    # Define size results dict
    size_d = {}
    
    # Calculate file & dir sizes
    size_d['01_CSV'] = os.path.getsize(path + 'CSV' + '_' + str(n-1) + '.csv') / (1024**2)
    size_d['02_TXT'] = os.path.getsize(path + 'TXT' + '_' + str(n-1) + '.txt') / (1024**2)
    size_d['03_Feather'] = os.path.getsize(path + 'Feather' + '_' + str(n-1) + '.feather') / (1024**2)
    size_d['04_Parquet_NP'] = os.path.getsize(path + 'Parquet_NP' + '_' + str(n-1) + '.parquet') / (1024**2)
    path_Parquet_SP = Path(path + 'Parquet_SP_19.parquet')
    size_d['05_Parquet_SP'] = sum(f.stat().st_size for f in path_Parquet_SP.glob('**/*') if f.is_file()) / (1024**2)
    path_Parquet_MP = Path(path + 'Parquet_MP_19.parquet')
    size_d['06_Parquet_MP'] = sum(f.stat().st_size for f in path_Parquet_MP.glob('**/*') if f.is_file()) / (1024**2)
    size_d['07_Avro'] = os.path.getsize(path + 'Avro' + '_' + str(n-1) + '.avro') / (1024**2)
    size_d['08_Pickle'] = os.path.getsize(path + 'Pickle' + '_' + str(n-1) + '.pickle') / (1024**2)
    
    # Return a dictionary including the actual measured time values of all methods
    # Return a dictionary including the statistical description of all methods
    return measured_vars_w, measured_vars_r, stat_dw, stat_dr, size_d

# -------------------------------
# -------------------------------
# Calling Analysis function
# -------------------------------
# -------------------------------

# Call analysis function
measured_vars_w, measured_vars_r, stat_dw, stat_dr, size_d = analysis(n, path, df)

# Print the type and shape of each object
print(type(measured_vars_w))
print(len(measured_vars_w))

print(type(measured_vars_r))
print(len(measured_vars_r))

print(type(stat_dw))
print(len(stat_dw))

print(type(stat_dr))
print(len(stat_dr))

print(type(size_d))
print(len(size_d))

# -------------------------------
# -------------------------------
# Plotting the results
# -------------------------------
# -------------------------------

# -------------------------------
# File sizes
# -------------------------------

# Create figure
plt.figure('File Sizes Bar Chart')

# Plot the file sizes
plt.bar(size_d.keys(), size_d.values(), color = color_main)

# Enable grid
plt.grid(True, zorder=0)

# Set xlabel and ylabel
plt.xlabel('File Format', fontsize=label_font_size, labelpad=text_padding)
plt.ylabel('File Size [MB]', fontsize=label_font_size, labelpad=text_padding)

# Remove bottom and top separators
sns.despine(bottom=True)

# Add plot title
plt.title('File/Folder Sizes in Megabytes', fontsize=title_font_size, pad=text_padding)

# Optional: Save the figure as a png image
plt.savefig('performance_results/' + 'file_sizes_bar_chart_tp.png', format = 'png', dpi = 300, transparent = True)
plt.savefig('performance_results/' + 'file_sizes_bar_chart_bg.png', format = 'png', dpi = 300, transparent = False)

# Close the figure
plt.close()

# -------------------------------
# Writing Times
# -------------------------------

# Create figure
plt.figure('Writing Times Boxplot')

# Plot the writing times
plt.boxplot(measured_vars_w.values(),
            labels = measured_vars_w.keys(),
            showmeans=True)

# Enable grid
plt.grid(True, zorder=0)

# Set xlabel and ylabel
plt.xlabel("File Format", fontsize=label_font_size, labelpad=text_padding)
plt.ylabel("Writing Time [s]", fontsize=label_font_size, labelpad=text_padding)

# Remove bottom and top separators
sns.despine(bottom=True)

# Add plot title
plt.title('Writing Time in Seconds', fontsize=title_font_size, pad=text_padding)

# Optional: Save the figure as a png image
plt.savefig('performance_results/' + 'writing_time_scattered_boxplots_tp.png', format = 'png', dpi = 300, transparent = True)
plt.savefig('performance_results/' + 'writing_time_scattered_boxplots_bg.png', format = 'png', dpi = 300, transparent = False)

# Close the figure
plt.close()

# -------------------------------
# Reading Times
# -------------------------------

# Create figure
plt.figure('Reading Times Boxplot')

# Plot the writing times
plt.boxplot(measured_vars_r.values(),
            labels = measured_vars_r.keys(),
            showmeans=True)

# Enable grid
plt.grid(True, zorder=0)

# Set xlabel and ylabel
plt.xlabel("File Format", fontsize=label_font_size, labelpad=text_padding)
plt.ylabel("Reading Time [s]", fontsize=label_font_size, labelpad=text_padding)

# Remove bottom and top separators
sns.despine(bottom=True)

# Add plot title
plt.title('Reading Time in Seconds', fontsize=title_font_size, pad=text_padding)

# Optional: Save the figure as a png image
plt.savefig('performance_results/' + 'reading_time_scattered_boxplots_tp.png', format = 'png', dpi = 300, transparent = True)
plt.savefig('performance_results/' + 'reading_time_scattered_boxplots_bg.png', format = 'png', dpi = 300, transparent = False)

# Close the figure
plt.close()

# -------------------------------
# -------------------------------
# Exporting the results in tabular format
# -------------------------------
# -------------------------------

# Define function to export results to Excel file
def results_to_excel(dseries_dict, path):
    """Write dictionary of dataframes to separate sheets, within 
        1 file."""
    writer = pd.ExcelWriter(path, engine='openpyxl')

    for tab_name, dseries in dseries_dict.items():
        dseries.to_excel(writer, sheet_name=tab_name)

    writer.close()

# Define file for writing results
path_w = 'performance_results/' + 'measured_vars_w.xlsx'
path_dw = 'performance_results/' + 'stat_dw.xlsx'

# Call function on writing results
results_to_excel(measured_vars_w, path_w)
results_to_excel(stat_dw, path_dw)

# Define file for reading results
path_r = 'performance_results/' + 'measured_vars_r.xlsx'
path_dr = 'performance_results/' + 'stat_dr.xlsx'

# Call function on reading results
results_to_excel(measured_vars_r, path_r)
results_to_excel(stat_dr, path_dr)
