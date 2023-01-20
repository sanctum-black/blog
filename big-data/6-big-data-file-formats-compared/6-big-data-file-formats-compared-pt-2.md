# 6 Big Data File Formats Compared, Pt. 2
In the first part of this 3-article series, we introduced the concepts of **columnar file formats** & **row-based file formats**. We also defined **serialization** and **deserialization**, and provided an overview of six relevant Big Data file formats. Finally, we went over some examples involving the writing of objects to these file formats using Python. 

In this section, we will focus on **reading** the files we created.

---

## Table of Contents
1. Preparing the files
2. Reading with Python
	1. csv
	2. txt
	3. Feather
	4. Parquet
	5. Avro
	6. Pickle
5. Conclusions
6. References

---

## 1. Preparing the files
On our last session we generated a total of 12 files:

| File Name | Format | Method Used |
| ----- | ----- | ----- |
| `01_dataset_method_1.csv` | CSV | `numpy.tofile()` |
| `02_dataset_method_2.csv` | CSV | `numpy.savetext()` |
| `03_dataset_method_3.csv` | CSV | `pandas.DataFrame.to_csv()` |
| `04_dataset_method_1.txt` | TXT | `numpy.savetext()` |
| `05_dataset_method_2.txt` | TXT | `pandas.DataFrame.to_csv()` |
| `06_dataset_method_1.feather` | Feather | `pandas.DataFrame.to_feather()` |
| `07_dataset_method_2.parquet` | Parquet | `pandas.DataFrame.to_parquet()` |
| `08_dataset_method_2.parquet` | Parquet | `pandas.DataFrame.to_parquet()` |
| `09_dataset_method_3.parquet` | Parquet | `pandas.DataFrame.to_parquet()` |
| `10_dataset_method_1.avro` | Avro | `fastavro` |
| `11_dataset_method_1.pickle` | Pickle | `.pickle.dump()` |
| `12_dataset_method_2.pickle` | Pickle | `.pickle.dumps()` |

We will use these outputs to continue with the reading section.

Files can be found on the blog article repo [`outputs`](https://github.com/pabloaguirrenck/blog/tree/master/big-data/6-big-data-file-formats-compared/outputs) folder.
Python scripts can also be found in the [blog article repo](https://github.com/pabloaguirrenck/blog/tree/master/big-data/6-big-data-file-formats-compared).

### 1.1 Non-serialized formats
As opposed to the serialized formats, **non-serialized** formats do not convert the object into a stream of bytes. We will explain serialization formats in more detail further on. The most common non-serialization formats are csv & txt files.

#### 1.1.1 csv
**Comma-separated values** (*csv*) is a delimited text file format that typically uses a comma to separate values, and although more delimiters can be used, it's not standard practice. It is the most popular format for storing & reading tabular data since its fast, easy to write & read, its supported by practically all programs & libraries involving data processing and forces a flat & simple schema.

As popular as it is, csv also has some disadvantages such as large file sizes, slow parsing time, poor support from Apache Spark, missing data handling, limited encoding formats, special handling required with nested data, basic data-support only, poor support of special characters, no defined schema, and the use of commas as delimiters; if our data entries have commas, we will have to enclose the entry in quotes, otherwise they will be treated as delimiters.

These disadvantages make csv files suboptimal when working with big data. 

A typical csv file will have a `.csv` extension, and will look like the example below:

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

#### 1.1.2 txt
**Text document file** (*txt*) is a plain-text format structured as a sequence of lines of text. It is also an extremely popular format used for storing & reading tabular data because of its simplicity & versatility; a txt file can be formatted as delimited, free form, fixed width, jagged right, and so on.

A typical txt file will have a `.txt` extension, and will look like the example below *(depending on the delimiter used, it will vary. In this example we use tab delimiters which is the convention)*:

```
Name   Age   Occupation   Country   State   City
Joe   20   Student   United States   Kansas   Kansas City
Chloe   37   Detective   United States   California   Los Angeles
Dan   39   Detective   United States   California   Los Angeles
...
```

### 1.2 Serialized formats
Here is where things start getting more interesting; we introduce a concept called **serialization**.

This refers to the process of converting a data object into a series of bytes that save the state of the object in an easily transmittable form. The inverse process is called **deserialization**, and consists of reverting the object back to its original form.

Serialization has multiple advantages when it comes to big data handling & processing:
- Facilitates the transportation of data across network, and avoids compatibility issues.
- Enables us to save the exact current state of the object, transfer it, and replicate it in a new location.
- The serialization process can be customized depending on the specific needs, and the serialized data can also be encrypted.

There are multiple data-serialization formats available. In this section, we'll mention 5 which are widely used in data processing.

#### 1.2.1 Feather
**Feather** is a portable, lightweight, columnar, serialized file format based on Apache arrow. It uses the Arrow IPC format internally to store & organize data. Feather supports two compression libraries, the default being `LZ4` (included in the `pyarrow` library), and is available for Python & R programming languages.

In general, `.feather` files are mostly recommended for short-term storage since stability between binary versions is not guaranteed.

A typical Feather file will have a `.feather` extension. Since it is a serialized format, we cannot see the contents of a `.feather` file by simply using a text editor.

#### 1.2.2 Parquet
**Parquet** is an open source, columnar, serialized data file format created by Apache, and designed for efficient data storage & retrieval. As with `.feather` files, it supports data compression and encoding schemes, and is optimized for handling data in bulk. 

Unlike `.feather` files, `.parquet` files are suited for long-term storage, since the binary versions are much more stable and constitute the gold-standard for large data set columnar format storage.

A typical Parquet file will have a `.parquet` extension. Since it is a serialized format, we cannot see the contents of a `.parquet` file by simply using a text editor, but if we use partitioning, we are actually able to see the folder structure (*partition scheme*) created. A single-partitioned `.parquet` system would look similar to the example below:

```
main.parquet
├─── Col1=Col1_Value1
│    ├─── *.parquet
└─── Col1=Col1_Value2
     └─── *.parquet
```

#### 1.2.3 Avro
**Avro** is a widely used, row-based, serialized storage format for Hadoop. It uses serialization for the actual data, and the JSON format to store the data schema, making the data easily readable by other platforms.

The main difference of Avro vs. Feather & Parquet formats, is that Avro uses a row-based structure, whereas the last 2 use a column-based (*columnar*) format.

A typical Avro file will have a `.avro` extension. Since it is a serialized format, we cannot see the contents of an `.avro` file by simply using a text editor.

#### 1.2.4 Pickle
**Pickle** is a language-specific, serialized file format used to store Python objects. Its usage is sometimes discouraged since it is not a universal file format, and other languages might present difficulties when parsing it. On the other hand, it presents us with the opportunity to write virtually any Python object to disk preserving its structure: tuples, lists, arrays, dictionaries, nested objects, class instances & DataFrames, among others, are supported.

A typical Pickle file will have a `.pickle` extension, though other extensions such as `.pck`, `.pcl` and `.db` are also supported. Since it is a serialized format, we cannot see the contents of a `.pickle` file by simply using a text editor.

## 2. Creating a Data Set
For this section, we will be creating an array containing strings & numbers, using the `NumPy` module. Keep in mind that we will be using this same object throughout the entire section.

**Code**

```Python
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
```

**Output**

```
Name	 Age	Occupation	Country	        State	     City
Joe	     20	    Student	    United States	Kansas	     Kansas City
Chloe	 37	    Detective	United States	California	 Los Angeles
Dan	     39	    Detective	United States	California	 Los Angeles
```

Once we have out data set as a `numpy.ndarray` object `arr`, we can proceed with the writing.

## 3. Writing With Python

### 3.1 CSV
There are five main methods for writing a `csv` file using Python, although we'll only be covering three:

#### I. **Using `numpy.tofile()`**
This method takes a `NumPy Array` object as input, and writes a `csv` file in return. Additionally, it is very simple and accepts only two additional parameters:
- `fid` : An open file object, or a string containing a filename.
- `sep` :  Separator between array items for text output. If empty, a binary file is written, equivalent to `file.write(a.tobytes())`.
- `str` : Format string for text file output.

This method is not recommended because it lacks flexibility, and even tough we generated a two-dimensional array, the output is a single-lined `csv` file.

**Code**

```Python
# Export data to csv using numpy.tofile() method
arr.tofile('dataset_method_1.csv', sep = ',')
```

**Output**

```
'Name','Age','Occupation','Country','State','City','Joe','20','Student',...
```

#### II. **Using `numpy.savetext()`**
This method takes a `NumPy Array` object as input, and writes a `csv` file in return. It accepts a total of eight parameters. We will stick with the most relevant:
- `fname` : Filename or file handle.
- `X` : Data to be saved to a text file.
- `fmt` : A single format `(%10.5f)`, a sequence of formats, or a multi-format string.
- `delimiter` : String or character separating columns.
- `newline` : String or character separating lines.
- `header` : String that will be written at the beginning of the file.

In contrast to the previous method, `numpy.savetext()` is more versatile, and lets us output a multi-line `csv` file by using the `newline` parameter.

The catch to this method is being careful in the `fmt` parameter we specify. If we leave it empty or we specify the incorrect format, we'll most probably get a `TypeError` in return. 

Also, we need to be careful & remember which `newline` parameter we use. For this example, we'll stick to a newline `\n`.

**Code**

```Python
# Export data to csv using numpy.savetext() method
np.savetxt('dataset_method_2.csv', arr, fmt = '%s', delimiter = ',', newline = '\n')
```

**Output**

```
Name	 Age	Occupation	Country	        State	     City
Joe	     20	    Student	    United States	Kansas	     Kansas City
Chloe	 37	    Detective	United States	California	 Los Angeles
Dan	     39	    Detective	United States	California	 Los Angeles
```

#### III. **Using `pandas.DataFrame.to_csv()`**
By far the most common technique when working with tabular data, but we leave it at the end since this method requires a different object as input.

The `pandas.DataFrame.to_csv()` method accepts a `pandas.DataFrame` object, and writes a `csv` file in return. It accepts a total of 21 parameters. We will stick with the most relevant:
- `path_or_buf` : String or path object.
- `sep` : String of length 1. Field delimiter for the output file.
- `header` : Write out the column names.
- `index` : Write row names (index).

**Code**

```Python
# Import pandas module
import pandas as pd

# Convert our array to a pandas.DataFrame object
# Extract data & columns separately
df = pd.DataFrame(data = arr[1:], columns = arr[:1][0])

# Export data to csv using pandas.DataFrame.to_csv() method
df.to_csv('dataset_method_3.csv', index = False)
```

**Output**

```
Name	 Age	Occupation	Country	        State	     City
Joe	     20	    Student	    United States	Kansas	     Kansas City
Chloe	 37	    Detective	United States	California	 Los Angeles
Dan	     39	    Detective	United States	California	 Los Angeles
```

### 3.2 TXT
There are two main methods for writing a `txt` file using Python, both of which we've already seen:

#### I. **Using `numpy.savetext()`**
The syntax is the same as with a `csv` file; we will only change some parameters:
- We will change the `fname` extension.
- We will remove the current delimiter (`,`), and substitute with a tab delimiter (`'\t'`). If we do not specify the delimiter parameter, our `txt` file will be written with a single space delimiter. This is bad practice and will probably lead to problems when parsing the file if we have entries with single spaces included.

Everything else can stay as is.

We will use the `numpy.ndarray` object `arr` we created in the previous section.

**Code**

```Python
# Export data to csv using numpy.savetext() method
np.savetxt('dataset_method_1.txt', arr, fmt = '%s', delimiter = '\t', newline = '\n')
```

**Output**

```
Name	 Age	Occupation	Country	        State	     City
Joe	     20	    Student	    United States	Kansas	     Kansas City
Chloe	 37	    Detective	United States	California	 Los Angeles
Dan	     39	    Detective	United States	California	 Los Angeles
```


#### II. **Using `pandas.DataFrame.to_csv()`**
This method, again, is the prefered one since it has a fair ammount of parameters we can fine-tune. The syntax is the same as with a `csv` file; we will only change some parameters:
- If we ommit the `sep` parameter, our file will be writen as comma-separated. As stated before, the convention for `txt` files is to use tab delimiters, so we'll change that.

We will use the `pandas.DataFrame` object `df` we created in the previous section.

**Code**

```Python
# Export data to csv using pandas.DataFrame.to_csv() method
df.to_csv('dataset_method_3.csv', index = False)
```

**Output**

```
Name	 Age	Occupation	Country	        State	     City
Joe	     20	    Student	    United States	Kansas	     Kansas City
Chloe	 37	    Detective	United States	California	 Los Angeles
Dan	     39	    Detective	United States	California	 Los Angeles
```

### 3.3 Feather
We can use the `pandas.DataFrame.to_feather()` method. To use this method, we will need to install an additional library called `pyarrow`:

```Python
pip install pyarrow
```

#### I. **Using `pandas.DataFrame.to_feather()`**
This method accepts a `pandas.DataFrame` object, and writes a `feather` file in return. It accepts a total of 5 parameters, including the additional `kwargs`:
- `path` : String or path object.
- `kwargs` : Additional keywords passed:
	- `compression`
	- `compression_level`
	- `chunksize`
	- `version`

We will use the `pandas.DataFrame` object `df` we created in the previous section.

**Code**

```Python
# Export data to feather using pandas.DataFrame.to_feather() method
df.to_feather('dataset_method_1.feather')
```

**Output**
Since `feather` files are binary, we won't be able to see the actual contents of a `feather` file directly by using a text editor.

### 3.4 Parquet
We can use the `pandas.DataFrame.to_parquet()` method. Same as with the `pandas.DataFrame.to_feather()` module, to use this method, we will need to install an additional module called `pyarrow`.

Since we already have it, we'll go straight to writing.

#### I. **Using `pandas.DataFrame.to_parquet()` without partitioning**
This method accepts a `pandas.DataFrame` object, and writes a `parquet` file in return. It accepts a total of 5 parameters, including the additional `kwargs`:
- `path` : String or path object.
- `engine` : Parquet library to use. If ‘auto’, then the option `io.parquet.engine` is used.
- `compression` : Name of the compression to use.
- `index` : If True, include the dataframe’s index(es) in the file output.
- `partition_cols` : Column names by which to partition the dataset.
- `kwargs` : Additional keywords passed.

We will use the `pandas.DataFrame` object `df` we created in the previous section.

As mentioned earlier, we can write `parquet` files partitioned or without partitioning. If we would like to write an unpartitioned `parquet` file, we can do so by leaving the `partition_cols` parameter unspecified:

**Code**

```Python
# Using pandas.DataFrame.to_parquet() without partitioning
df.to_parquet('dataset_method_1.parquet')
```

**Output**
Since `parquet` files are binary, we won't be able to see the actual contents of a `parquet` file directly by using a text editor.

#### II. **Using `pandas.DataFrame.to_parquet()` with a single partition**
In contrast, if we would like to write a partitioned `parquet` file, we can do so by specifying the column names by which to partition the dataset, using the `partition_cols` parameter. In this example, we will partition only by `State`.

**Code**

```Python
# Using pandas.DataFrame.to_parquet() with partitioning
df.to_parquet('dataset_method_2.parquet', partition_cols = 'State')
```

**Output**
As before, `parquet` files are binary, but we can take a look at the different partitions:

```
dataset_method_2.parquet
├─── State=California
│    ├─── *.parquet
└─── State=Kansas
     └─── *.parquet
```

#### III. **Using `pandas.DataFrame.to_parquet()` with multiple partitions**
We can also pass a list of columns if we want an output which is partitioned multiple times. Each partition will be nested inside its parent partition.

**Code**

```Python
# Using pandas.DataFrame.to_parquet() with partitioning
df.to_parquet('dataset_method_3.parquet', partition_cols = ['State', 'City'])
```

**Output**
As before, `parquet` files are binary, but we can take a look at the different partitions:

```
dataset_method_3.parquet
├─── State=California
│    ├─── City=Los Angeles
│    │    └─── *.parquet
└─── State=Kansas
     └─── City=Kansas City
          └─── *.parquet
```

### 3.5 Avro
`avro` files are less straightforward when working with `pandas` since there is no default support. Also, as mentioned earlier, we need to define a schema in order to write `.avro` files.

There are two main libraries for manipulating `.avro` files in Python. We will stick with the later, since the first one is significantly slower:
- `avro` 
- `fastavro`

#### I. **Using `fastavro` Python file handler**

Before anything else, we will need to install the required library:

**Code**

```Python
pip install fastavro 
```

We can then import the required modules from the `fastavro` library:

**Code**

```Python
# Import fastavro modules
from fastavro import writer, parse_schema
```

We must also cast the `Age` column of our DataFrame `df` to `int`. Otherwise, when defining our schema and writing our file, we will receive an error:

**Code**

```Python
# Cast age to int type
df['Age'] = df['Age'].astype('int')

# Verify casting
df.dtypes
```

**Output**

```
Name          object
Age            int32
Occupation    object
Country       object
State         object
City          object
dtype: object
```

The next step will consist of defining our schema in a JSON-like format, and then parsing it using the `parse_schema()` method:

**Code**

```Python

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
```

- The `type` parameter is set to `record`. A `record` is a complex Avro type which supports the following parameters:
	- The `name` parameter provides the name of the `record`.
	- The `namespace` parameter provides a `name` qualification.
	- The `doc` parameter provides documentation to the user of our schema.
	- The `fields` parameter provides the data types for each column.

The `parse_schema()` method returns a dictionary consisting of 6 entries:  

**Output**

```
__fastavro_parsed   bool
__named_schemas     dict
doc                 str
fields              list
name                str
type                str
```

- `__fastavro_parsed` confirms we have a `fastavro` parsed schema.
- `__named_schemas` contains `doc`, `fields`, `name` & `type`.
- `doc` contains our brief documentation.
- `fields` contains a dictionary with column - data type associations
- `name` contains our record name.
- `type` denotes that this is a `record`.

Once we have generated our schema, we can then convert our `pandas.DataFrame` object to a list of records:

**Code**

```Python
# Convert pd.DataFrame to records (list of dictionaries)
records = df.to_dict('records')
```

The `df.to_dict()` method returns a Python list containing 3 dictionaries (*one per row*) each with column - entry pairs.   

**Output**

```
dict     {'Name': 'Joe', 'Age': 20, 'Occupation': 'Student'...}
dict     {'Name': 'Chloe', 'Age': 37, 'Occupation': 'Detective'...}
dict     {'Name': 'Dan', 'Age': 39, 'Occupation': 'Detective'...}
```

Finally, we can write our list of records to an `.avro` file using the Python file handler:

```Python
# Write to Avro file
with open('dataset_method_1.avro', 'wb') as out:
    writer(out, parsed_schema, records)
```

The `wb` parameter denotes we're writing a binary file.

### 3.6 Pickle
We can use the built-in `pickle` library for writing `.pickle` files. This library provides two different serialization methods:
- `pickle.dump()` : The open file version.
- `pickle.dumps()` : The byte string version.

#### I. **Writing a `.pickle` file as an open file**

We will start by importing the `pickle` library:

**Code**

```Python
# Import pickle library
import pickle
```

We will then use the `pickle.dump()` method to convert our previously generated list of dictionaries named `records`, into a `pickle` open file:

**Code**

```Python
# Define a pickle object
my_pickled_object = pickle.dump(records)

# Check the data type
type(my_pickled_object)
```

**Output**

```
bytes
```

We will finally write our string of bytes as a `.pickle` file in memory using the Python file handler:

**Code**

```Python
# Write byte string to disk
with open('dataset_method_1.pickle','wb') as out:
    out.write(my_pickled_object)
```


#### II. **Writing a `.pickle` file as a byte string**

We will now convert our previously generated list of dictionaries named `records`, into a `pickle` byte string:

**Code**

```Python
# Define a pickle object
my_pickled_object = pickle.dumps(records)

# Check the data type
type(my_pickled_object)
```

**Output**

```
bytes
```

We will finally write our string of bytes as a `.pickle` file in memory using the Python file handler:

**Code**

```Python
# Write byte string to disk
with open('dataset_method_1.pickle','wb') as out:
    out.write(my_pickled_object)
```





















## 4. Reading With Python

### 4.1 CSV
We will start by declaring a filename variable containing the data set name we're going to work with:

```Python
# Declare filename variable 
filename = 'datasets/Chernobyl_ Chemical_Radiation.csv'
```

There are four main methods for reading a `csv` file using Python:

#### I. **Using `csv` `reader()`**
The `reader()` method belongs to the `csv` module, and can be used to read any `csv` file with the use of a `handler`. There are multiple methods we can use once we have our file as a `csvreader` iterable object, but that is out of the scope of this article, so we'll stick to the basics.

**Code**

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

**Code**

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

**Code**


**Output**

#### IV. **Using `NumPy` `genfromtxt()`**

**Code**


**Output**

### 4.2 TXT
### 4.3 Feather
### 4.4 Parquet
### 4.5 Avro
### 4.6 Pickle


## 5. Use Cases


## 6. Side-by-Side Comparison & Performance Tests
For this section, we will employ a slightly larger file. We will be using the `Spotify Charts` data set (`2.48 GB`) published by `DHRUVIL DAVE`, which you can download from [Kaggle](https://www.kaggle.com/datasets/dhruvildave/spotify-charts).

**Code**

```Python
print("Hello")
```

**Results**
| Format | Size | Read Time | Read Method | Write Time | Write Method |
| --- | --- | --- | --- | --- | --- |
| `.csv` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.txt` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.feather` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.parquet` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.avro` | 20kb | 20kb | 20kb | 20kb | 20kb |
| `.pickle` | 20kb | 20kb | 20kb | 20kb | 20kb |

_Note: Keep in mind that this values vary across systems. CPU processing power, RAM capacity and other variables directly affect reading & writing times_.

## 6. Conclusions
In summary, not all tabular file formats are good for every application. Each of them were created with a purpose in mind, and are better or worse at some applications than the others.

Serialized formats for example, present several advantages over non-serialized formats, but the inverse also happens: serialized formats may lose stability across versions, and usually consume more processing resources when serializing/deserializing objects.

Before implementing a format, specially in a production environment, it's important to make a detailed assessment of which formats are going to be used and how the encoding is to be handled. Also, when working with other collaborators,  setting a strict standard for data formatting & handling is of vital importance.

## 7. References
https://www.geeksforgeeks.org/working-csv-files-python/
https://www.geeksforgeeks.org/how-to-read-csv-files-with-numpy/
https://earthly.dev/blog/csv-python/
https://forum.xojo.com/t/differences-between-csv-and-txt/38813/3
https://stackoverflow.com/questions/14620125/difference-between-a-csv-and-a-txt-file
https://en.wikipedia.org/wiki/Text_file#Data_storage
https://softwareengineering.stackexchange.com/questions/47838/why-do-we-keep-using-csv
https://docs.python.org/3/library/csv.html
https://www.weirdgeek.com/2018/12/common-file-formats-used-in-data-science/
https://data.gov.ie/edpelearning/en/module9/#/id/co-01
https://towardsdatascience.com/big-data-file-formats-explained-dfaabe9e8b33
https://arrow.apache.org/docs/python/api/formats.html
https://www.w3schools.com/js/js_json_datatypes.asp
https://avro.apache.org/docs/1.8.2/spec.html#schema_record
https://docs.informatica.com/data-quality-and-governance/data-quality/10-5/developer-tool-guide/appendix-a--data-type-reference/complex-file-and-transformation-data-types/avro-data-types-and-transformation-data-types.html
https://pythonnumericalmethods.berkeley.edu/notebooks/chapter11.03-Pickle-Files.html
https://towardsdatascience.com/csv-files-for-storage-absolutely-not-use-apache-avro-instead-7b7296149326