# 7 Different Tabular File Formats Compared
A **tabular file format** is used to store data in a tabular way, that is, in a row / column format. Columns are typically identified by headers, which consist of the first row of the file. Tabular formats play a key role in data processing, and most of the Data Analysis modules out there accept them.

There are multiple formats tailored for specific applications, and can be classified as text files or binary files. A binary file is designed to be read by computers; we are not able to open a binary file and read its content by simply using a text editor. In contrast, a text file can be directly opened with a text editor.

In this article, we will discuss 7 popular tabular file formats, explain what they are for, go over some examples, and make some performance comparisons.

## Table of Contents
1. Overview
	1. `csv`
	2. `txt`
	3. `JSON`
	4. `Feather`
	5. `Parquet`
	6. `Avro`
	7. `XML`
2. Reading With Python
	1. `csv`
	2. `txt`
	3. `JSON`
	4. `Feather`
	5. `Parquet`
	6. `Avro`
	7. `XML`
3. Writing With Python
	1. `csv`
	2. `txt`
	3. `JSON`
	4. `Feather`
	5. `Parquet`
	6. `Avro`
	7. `XML`
4. Use Cases
5. Side-by-Side Comparison & Performance Tests
6. Conclusions
7. References

## 1. Overview

### 1.1 `csv`
**Comma-separated values** (`csv`) is a delimited text file format that typically uses a comma to separate values, and although more delimiters can be used, it's not standard practice. It is the most popular format for storing & reading tabular data since its fast, easy to write & read, its supported by practically all programs & libraries involving data processing and forces a flat & simple schema.

As popular as it is, `csv` also has some disadvantages such as large file sizes, missing data handling, basic data-support only, poor support of special characters, no distinction between string and numeric values, no data type information, and the use of commas in the actual entries; if our data entries have commas, we will have to enclose the entry in quotes, otherwise they will be treated as separators.

A typical `csv` file will have a `.csv` extension, and will look like the example below:

```
Name,Age,Occupation,Country,State,City
Joe,20,Student,United States,Kansas,Kansas City
Chloe,37,Detective,United States,California,Los Angeles
Dan,39,Detective,United States,California,Los Angeles
...
```

Some considerations:
- The header is denoted as the first row of our document. 
- Each entry is followed by a comma, but without blank spaces.
- Entries can have blank spaces, and will be treated accordingly when parsing.
- Even though we can use text as well as numeric values, a CSV file will not store information regarding data types.

### 1.2 `txt`
**Text document file** (`txt`) is a plain-text format structured as a sequence of lines of text. It is also an extremely popular format used for storing & reading tabular data because of its simplycity & versatility; a `txt` file can be formatted as delimited, free form, fixed width, jagged right, and so on.

A typical `txt` file will have a `.txt` extension, and will look like the example below *(depending on the delimtier used, it will vary. In this example we use tab delimiters)*:

```
Name   Age   Occupation   Country   State   City
Joe   20   Student   United States   Kansas   Kansas City
Chloe   37   Detective   United States   California   Los Angeles
Dan   39   Detective   United States   California   Los Angeles
...
```


### 1.3 `JSON`
Unlike the previous data storage formats, **JavaScript Object Notation** (`JSON`) is a data exchange format. It was originally developed for JavaScript, but is currently supported by many programming languages & applications. Two main advantages over other formats, are its capacity to create deep nesting and hierarchy due to its syntax, and its flexibility regarding data types. `JSON` accepts the following:

- Strings
- Numbers
- Objects (`JSON` object)
- Arrays
- Booleans
- `null`



### 1.4 Feather
### 1.5 Parquet
### 1.6 Avro
### 1.7 XML


## 2. Reading With Python
For this section, we will be using the public `Chernobyl Chemical Radiation Country Data` data set (`102 KB`) published by `BARIS DINCER`, which you can download from [Kaggle](https://www.kaggle.com/datasets/brsdincer/chernobyl-chemical-radiation-csv-country-data).

The data set has 2051 rows & 9 columns.

Since our data set is in a `csv` format, we will need to do some previous work in order to get all of the formats that we require as actual files. Don't worry, we'll cover the writing process in more detail later on. You can just copy-paste & run this fragment alone, or get the different formats directly from my repo.

```Python
# Declare filename variable (use your respective directory)
filename = 'datasets/Chernobyl_ Chemical_Radiation.csv'

# Import file as Pandas DataFrame
df = pd.read_csv(filename)

# Export df in all of the formats required

```

### 2.1 CSV
We will start by declaring a filename variable containing the data set name we're going to work with:

```Python
# Declare filename variable 
filename = 'datasets/Chernobyl_ Chemical_Radiation.csv'
```

There are four main methods for reading a `csv` file using Python:

#### I. **Using `csv` `reader()`**
The `reader()` method belongs to the `csv` module, and can be used to read any `csv` file with the use of a `handler`. There are multiple methods we can use once we have our file as a `csvreader` iterable object, but that is out of the scope of this article, so we'll stick to the basics.

**Example**
```Python
# Import csv module
import csv

# Open filename as csv.reader object
with open(filename, 'r') as csvfile:

	# Use csv.reader() method to convert object to iterable
    csvreader = csv.reader(csvfile)
    
    # Print first column values by iterating through rows in csvreader object
    for row in csvreader:
        print(row[0])
```

**Output**
```
FI
FI
FI
FI
FI
FI
FI
...
```

**Explanation**
- First, we import the `csv` module.
- Second, we open the file associated with the `filename` in read-mode `'r'`. We get a `file` object in return.
- Third, we use the `csv.reader()` method to convert the `file` object to an iterable `csv.reader` object.
- Finally, we iterate over the rows in our `csvreader` object, index the first element, and print the result. 

#### II. **Using `Pandas` `read_csv()`**
If we're using `Pandas dataframes`, this is the best and most straight-forward choice. It automatically reads the `csv` file and loads it into a `Pandas dataframe` object.

**Example**
```Python
# Import Pandas module
import pandas as pd

# Read filename and save as pandas dataframe object df
df = pd.read_csv(filename)

# Get the first 5 elements of the dataframe
df.head()
```

**Output**
```
  PAYS  Code Location  ...  I_131_(Bq/m3)  Cs_134_(Bq/m3) Cs_137_(Bq/m3)
0   SE     1    RISOE  ...              1               0           0.24
1   SE     1    RISOE  ...         0.0046         0.00054        0.00098
2   SE     1    RISOE  ...         0.0147          0.0043         0.0074
3   SE     1    RISOE  ...        0.00061               0        0.00009
4   SE     1    RISOE  ...        0.00075          0.0001        0.00028
```

**Explanation**
- First, we import the `pandas` module.
- Second, we read the file associated with the `filename`. We get a `pandas.core.frame.DataFrame` object in return. If left unspecified, this method will automatically set the first row as header.
- Third, we extract the first 5 rows by using the `DataFrame.head()` method.

#### III. **Using `NumPy` `loadfromtxt()`**

**Example**


**Output**

#### IV. **Using `NumPy` `genfromtxt()`**

**Example**


**Output**

### 2.2 TXT
### 2.3 JSON
### 2.4 Feather
### 2.5 Parquet
### 2.6 Avro
### 2.7 XML


## 3. Writing With Python

### 3.1 CSV
### 3.2 TXT
### 3.3 JSON
### 3.4 Feather
### 3.5 Parquet
### 3.6 Avro
### 3.7 XML


## 4. Use Cases


## 5. Side-by-Side Comparison & Performance Tests
For this section, we will employ a slightly larger file. We will be using the `Spotify Charts` data set (`2.48 GB`) published by `DHRUVIL DAVE`, which you can download from [Kaggle](https://www.kaggle.com/datasets/dhruvildave/spotify-charts).

**Code**

**Results**
| Format | Size | Read Time | Read Method | Write Time | Write Method |
| --- | --- | --- | --- | --- | --- |
| `.csv` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.txt` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.json` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.feather` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.parquet` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.avro` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.xml` | 20kb | 20kb | 20kb | 20kb | 20kb |

_Note: Keep in mind that this values vary across systems. CPU processing power, RAM capacity and other variables directly affect reading & writing times_ 



## 6. Conclusions
So, in summary, not all tabular file formats are good for every application. Each of them were created with a purpose in mind, and are better or worse at some things than the others.
- `csv`
	- Aaa
	- Aaa
	- Aaa

- `csv`
	- Aaa
	- Aaa
	- Aaa
-  `csv`
	- Aaa
	- Aaa
	- Aaa

## 7. References


