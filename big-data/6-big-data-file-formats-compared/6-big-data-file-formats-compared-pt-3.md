# 6 Big Data File Formats Compared, Pt. 3
Over the last 2 articles of this series, we have discussed different Big Data file formats and their overall characteristics. We have also performed writing & reading examples using different Python modules & methods.

In this section, we will focus on making a side-by-side comparison of the performance of the formats reviewed. We will evaluate writing times, reading times and file sizes.

We will then conclude this series by reviewing specific use-cases for each one of the formats, as well as discuss some recommendations.

This section will be lengthier than the previous ones and will involve more code. We'll be using Python scripts which can be found in the [Blog Article Repo](https://github.com/pabloaguirrenck/blog/tree/master/big-data/6-big-data-file-formats-compared).

---

## Table of Contents
- [Importing the required modules](#importing-the-required-modules)
- [Defining plot parameters](#defining-plot-parameters)
- [Preparing the data set](#preparing-the-data-set)
- [Experiment design](#experiment-design)
- [Performance tests](#performance-tests)
	- [Parameter definition](#1-parameter-definition)
	- [Writing performance tests](#2-writing-performance-tests)
	- [Reading performance tests](#3-reading-performance-tests)
	- [Analysis](#4-analysis)
		- [Writing performance analysis](#41-writing-performance-analysis)
		- [Reading performance analysis](#42-reading-performance-analysis)
		- [File size analysis](#43-file-size-analysis)
- [Performance results](#performance-results)
	- [Plotting the results](#1-plotting-the-results)
		- [Bar chart for file sizes](#11-bar-chart-for-file-sizes)
		- [Boxplot for writing times](#12-boxplot-for-writing-times)
		- [Boxplot for reading times](#13-boxplot-for-reading-times)
	- [Exporting the results in a tabular format](#2-exporting-the-results-in-a-tabular-format)
- [Side-by-side comparison](#side-by-side-comparison)
- [Use cases](#use-cases)
- [Conclusions](#conclusions)
- [References](#references)

---

## Importing the required modules
For this section, we will be using the following Python libraries and modules:

##### **Code**
```Python
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
```

---

## Defining plot parameters
Since we'll be plotting our experimental results, we will need to define our plot parameters beforehand:

##### **Code**
```Python
# Before anything else, delete the Matplotlib
# font cache directory if it exists, to ensure
# custom font proper loading
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
```

---

## Preparing the data set
In order to reduce noise in our performance measurements, for this section we will employ a slightly larger file. We will be using the `Spotify Charts` data set (`2.48 GB`) published by `DHRUVIL DAVE`, which you can download from [Kaggle](https://www.kaggle.com/datasets/dhruvildave/spotify-charts).

We can start by reading the data set as a `pandas.DataFrame` object:

##### **Code**
```Python
# Load csv file as pandas.DataFrame object
df = pd.read_csv('datasets/charts.csv')
```

This should take a couple of minutes, depending on the specifications of each machine.

Upon concluding, we should end up with a `pandas.DataFrame` object `df` with the following shape:

##### **Code**
```Python
# Get the shape of the object
df.shape
```

##### **Output**
```
(26173514, 9)
```

Meaning 26,173,514 rows by 9 columns.

Next, we will need to do some preprocessing before beginning with the tests:

##### **Code**
```Python
# Singe we have nan values, we will remove them
df = df.dropna()

# Check the current data types and see if casting is required
df.dtypes

# Cast to required data types
# Date is currently a string. We will cast it to Pandas DateTime in integer format.
# since Avro does not support original DateTime
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].apply(lambda x: x.value)

# Streams will be casted to integer type
df['streams'] = df['streams'].astype('int')
```

The reason we converted our `date` field to an `int` `datetime64` data type, is because the `fastavro` library does not currently support `str` `datetime64` objects.

Since we will be defining a schema for this file format, a conventional `datetime64` data type would raise a `TypeError`.

Lastly, we will create two new directories:

- The first one for storing all of our written files.
- The second one for storing all of our performance test results.

##### **Code**
```PowerShell
mkdir performance_tests
mkdir performance_results
```

Now, we're ready to start designing our experiment.

---

## Experiment design
For both writing & reading performance tests, we will be using a collection of measurements per file format. This is always good practice in experimental design, and will help us calculate a complete set of descriptive statistics.

Our experiment for the **writing process** will consist of the following steps:
1. Define the variables to measure.
2. Set the number of trials as a control variable.
3. Begin with the first trial, measuring variables of interest.
5. Store measurements.
7. Repeat for the other file formats.
8. Consolidate results and perform a statistical description.
9. Delete all written files except one to read in next experiment.

Our experiment for the **reading process** will consist of the following steps:
1. Define the variables to measure.
2. Set the number of trials as a control variable.
3. Begin with the first trial, measuring variables of interest.
5. Store measurements.
6. Clear memory
7. Repeat for the other file formats.
8. Consolidate results and perform a statistical description.

---

## Performance tests

### 1. Parameter definition
We will start by defining our experiment parameters:

##### **Code**
```Python
# Define number of trials n
n = 20

# Define performance tests output path
path = 'performance_tests/'
```

### 2. Writing performance tests
We will start by defining our `writingPerformance()` function, which will accept the following parameters :

- `n` : `int`
	- Number of trials.
- `path` : `str`
	- Path for result writing.
- `df` : `pandas.DataFrame`
	- DataFrame Object containing data set.

Upon calling, it will return the following:
- `measured_vars_w` : `dict`
	- Execution time for each file format, with `n` number of trials.

Once we have the expected inputs and outputs, the idea is to perform the following:
1. Declare a `pandas.core.series.Series` for each of the file formats, where we will store writing times. This would result in 8 objects in total.
2. Declare an empty dictionary `measured_vars_w`, used to store key-value pairs of file format-Pandas series of measurements.
3. Define a `for` loop to iterate over the number of trials `n`.
4. Define a writing method for each file format.
5. Set a `start` timer variable before writing execution using the `time.time()` method. This will be our initial time marker.
6. Set an `end` timer variable after writing execution using the `time.time()` method. This will be our final time marker.
7. Calculate the `exec_time` for each loop, by calculating the difference between `end` and `start` variables.
8. Append the `exec_time` to our corresponding `pandas.core.series.Series` object.
9. Upon loop completion, assign a key-value pair to our `measured_vars_w` dictionary corresponding to the file format along with its measured execution times.
10. Remove all generated files except one using the `os.remove` method.
11. Repeat for all remaining file formats.

We can translate our pseudocode into code:

##### **Code**
```Python
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

    # Declare a dictionary for storing all lists
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
        
    # Define series title
    wtime_pickle.name = 'Writing Time [s]'
        
    # Add measurements to dictionary
    measured_vars_w['08_Pickle'] = wtime_pickle.reset_index(drop = True)
        
    # Remove all files from dir except one
    for trial in range(n - 1):
        os.remove(path + 'Pickle' + '_' + str(trial) + '.pickle')

    return measured_vars_w
```

### 3. Reading performance tests
Similar to the writing performance tests section, we will start by defining our `readingPerformance()` function, which will accept the following parameters :

- `n` : `int`
	- Number of trials.
- `path` : `str`
	- Path for result writing.
- `df` : `pandas.DataFrame`
	- DataFrame Object containing data set.

Upon calling, it will return the following:
- `measured_vars_r` : `dict`
	- Execution time for each file format, with `n` number of trials.

Once we have the expected inputs and outputs, the idea is to perform the following:
1. Declare a `pandas.core.series.Series` for each of the file formats, where we will store writing times. This would result in 8 objects in total.
2. Declare an empty dictionary `measured_vars_w`, used to store key-value pairs of file format-Pandas series of measurements.
3. Define a `for` loop to iterate over the number of trials `n`.
4. Define a reading method for each file format.
5. Set a `start` timer variable before writing execution using the `time.time()` method. This will be our initial time marker.
6. Set an `end` timer variable after writing execution using the `time.time()` method. This will be our final time marker.
7. Calculate the `exec_time` for each loop, by calculating the difference between `end` and `start` variables.
8. Append the `exec_time` to our corresponding `pandas.core.series.Series` object.
9. Delete the read object from memory.
10. Upon loop completion, assign a key-value pair to our `measured_vars_w` dictionary corresponding to the file format along with its measured execution times.
11. Repeat for all remaining file formats.

We can translate our pseudocode into code:

##### **Code**
```Python
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

    # Declare a dictionary for storing all lists
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
        with open('outputs/10_dataset_method_1.avro', 'rb') as fo:
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
        with open('outputs/11_dataset_method_1.pickle', 'rb') as file:
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
```


### 4. Analysis
Once we have both the `writingPerformance()` and `readingPerformance()` functions declared, we can define an `analysis()` function which will accept the following parameters :

- `n` : `int`
	- Number of trials.
- `path` : `str`
	- Path for result writing.
- `df` : `pandas.DataFrame`
	- DataFrame Object containing data set.

Upon calling, it will return the following:
- `measured_vars_w` : `dict`
	- Writing time of each file format, with `n` number of trials.
     
- `measured_vars_r` : `dict`
	- Reading time of each file format, with `n` number of trials.
	
- `stat_dw` : `dict`
	- Statistical description of measured writing times for all formats.
	
- `stat_dr` : `dict`
	- Statistical description of measured reading times for all formats. 
	
- `size_d` : `dict`
	- Output size description of measured times for all formats.

Once we have the expected inputs and outputs, the idea is to perform the following:

#### 4.1 **Writing Performance Analysis**
1. Define a list `tests` containing the names of each file format. We will use this object as iterable.
2. Call the `writingPerformance()` function and assign it to a `measured_vars_w` object.
3. Define an empty dictionary `stat_dw` for saving the statistical descriptions for the writing test.
4. Iterate over the `tests` object, indexing the `measured_vars_w` dictionary on each loop, and calculating its statistical description.
5. Assign a key-value pair on each loop, consisting of the file format name as key, and the statistical description object as value.

#### 4.2 **Reading Performance Analysis**
1. Call the `readingPerformance()` function and assign it to a `measured_vars_r` object.
2. Define an empty dictionary `stat_dr` for saving the statistical descriptions for the reading test.
3. Iterate over the `tests` object, indexing the `measured_vars_r` dictionary on each loop, and calculating its statistical description.
4. Assign a key-value pair on each loop, consisting of the file format name as key, and the statistical description object as value.

#### 4.3 **File Size Analysis**
1. Declare an empty dictionary `size_d` for storing the file size values.
2. For each file, calculate its size using the `os.path.getsize` method.
3. For each folder (parquet partitions), calculate its size using the `f.stat().st_size` method recursively.
4. Convert file sizes:
	1. The `os.path.getsize` method returns the file size in bytes, so we will need to divide the result by `1024` in order to get `MB` units. 
	2. The `f.stat().st_size` method returns the folder size in bytes, so we will need to divide the result by `1024` in order to get `MB` units.

We can translate our pseudocode into code:

##### **Code**
```Python
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
```

We can then call our `analysis()` function and assign the outputs to 5 different objects:

##### **Code**
```Python
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
```

##### **Output**
```
<class 'dict'>
8
<class 'dict'>
8
<class 'dict'>
8
<class 'dict'>
8
<class 'dict'>
8
```

The shapes of our objects match the output requirements, as we have 8 tested file formats.

---

## Performance results
Now, we have everything we need to make sense of the data that we generated.

In this example, the quantity of data is not too extense, since we only have 8 file formats and 20 measurements per format. Regardless, it is always a good practice to visualize the results in a plot as a first step, especially when dealing with large datasets.

### 1. Plotting the results
We'll proceed with some visualization techniques appropriate for the results we have.

#### 1.1 Bar chart for file sizes
A bar chart is a simple way to quickly visualize data. We can generate a bar chart using the `matplotlib.pyplot` module:

##### **Code**
```Python
# Create figure
plt.figure('File Sizes Bar Chart')

# Plot the file sizes
plt.bar(size_d.keys(), size_d.values(), color = color_main)

# Enable grid
plt.grid(True, zorder=0)

# Set xlabel and ylabel
plt.xlabel('File Format', fontsize=label_font_size, labelpad=text_padding)
plt.ylabel('File Size  [MB]', fontsize=label_font_size, labelpad=text_padding)

# Remove bottom and top separators
sns.despine(bottom=True)

# Add plot title
plt.title('File/Folder Sizes in Megabytes', fontsize=title_font_size, pad=text_padding)

# Optional: Save the figure as a png image
plt.savefig('performance_results/' + 'file_sizes_bar_chart.png', format = 'png', dpi = 300, transparent = True)

# Close the figure
plt.close()
```

If we save the figure directly and then close it, the image will be saved in the path we specify and will not display on our IDE.

##### **Output**
![alt text](https://raw.githubusercontent.com/pabloaguirrenck/blog/master/big-data/6-big-data-file-formats-compared/performance_results/file_sizes_bar_chart_bg.png "File Size Bar Chart")
_Figure 1.1: Bar Chart denoting File/Folder size in MB for each file format_

#### 1.2 Boxplot for writing times
A boxplot is a visualization method widely used in Data Science & statistical analysis. Its purpose is to describe the distribution of experimental measurements including useful visual information about the set.

A detailed discussion of the boxplot components is out of the scope of this article. That will be covered in another blog post.

We can generate a boxplot using the `matplotlib.pyplot` module:

##### **Code**
```Python
# Create figure
plt.figure('Writing Times Histogram')

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
```

##### **Output**
![alt text](https://raw.githubusercontent.com/pabloaguirrenck/blog/master/big-data/6-big-data-file-formats-compared/performance_results/writing_time_scattered_boxplots_bg.png "Writing Time Box Plot")
_Figure 1.2: Boxplot denoting the distribution of 20 trials of writing times for each file format_

#### 1.3 Boxplot for reading times
We can perform a similar treatment to our reading time results:

##### **Code**
```Python
# Create figure
plt.figure('Reading Times Histogram')

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
```

##### **Output**
![alt text](https://raw.githubusercontent.com/pabloaguirrenck/blog/master/big-data/6-big-data-file-formats-compared/performance_results/reading_time_scattered_boxplots_bg.png "Reading Time Box Plot")
_Figure 1.3: Boxplot denoting the distribution of 20 trials of reading times for each file format_

### 2. Exporting the results in a tabular format
We can also write our results to an Excel file. This is useful whenever we want to share or store information that took a fair amount of time to generate (*imagine running the whole performance test just to get the results back*).

An Excel file is also a very friendly tabular file format that everyone understands, and that anyone can use to make further analysis such as pivoting or calculating statistical measures (*mean, min, max, stdev, among others*).

For this part, we will be writing two `.xlsx` files, one for writing results and one for reading results. Each file will have 8 tabs, each consisting of the file format, and the writing and reading times in seconds respectively: 

##### **Code**
```Python
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

# Call function on writing results
results_to_excel(measured_vars_w, path_w)

# Define file for reading results
path_r = 'performance_results/' + 'measured_vars_r.xlsx'

# Call function on reading results
results_to_excel(measured_vars_r, path_r)
```

---

## Side-by-side comparison

##### **Results**
| **Format** | **Size** | **Writing Time** | **Writing Method** | **Reading Time** | **Reading Method** |
| --- | --- | --- | --- | --- | --- |
| `.csv` | 20MB | 20s | `to_csv()` | 20s | 20kb |
| `.txt` | 20MB | 20s | `to_csv()` | 20s | 20kb |
| `.feather` | 20MB | 20s | `to_feather()` | 20s | 20kb |
| `.parquet` | 20MB | 20s | `to_parquet()` (`NP`) | 20s | 20kb |
| `.parquet` | 20MB | 20s | `to_parquet()` (`SP`) | 20s | 20kb |
| `.parquet` | 20MB | 20s | `to_parquet()` (`MP`) | 20s | 20kb |
| `.avro` | 20MB | 20s | 20s | 20s | 20kb |
| `.pickle` | 20MB | 20s | `pickle.dump()` | 20s | 20kb |


_Figure 2: Chart containing File/Folder sizes, average writing times and average reading times from 20 measurements, including method used for each case_

_Note: Keep in mind that this values vary across systems. CPU processing power, RAM capacity and other variables directly affect reading & writing times_.

We can see that file sizes for...
We can also see that the writing times for...
Finally, we can see that the reading times for...

---

## Use Cases
From the results obtained on the previous section, we can see that...

Although the `.pickle` file format performs well, it is not recommended since it's platform specific. Also, malicious code can be injected easily...

---

## Conclusions
In summary, not all tabular file formats are good for every application. Each of them were created with a purpose in mind, and are better or worse at some applications than the others.

Serialized formats for example, present several advantages over non-serialized formats, but the inverse also happens: serialized formats may lose stability across versions, and usually consume more processing resources when serializing/deserializing objects.

Before implementing a format, specially in a production environment, it's important to make a detailed assessment of which formats are going to be used and how the encoding is to be handled. Also, when working with other collaborators,  setting a strict standard for data formatting & handling is of vital importance.

## References
https://www.geeksforgeeks.org/working-csv-files-python/