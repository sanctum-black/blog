# 6 Big Data File Formats Compared, Pt. 3
Over the last 2 articles of this series, we have discussed... 

In this section, we will focus on making a side-by-side comparison of the formats reviewed, as well as making performance tests for writing times, reading times and CPU processing resources...

We will then conclude this series by reviewing specific use-cases for each one of the formats involved, as well as discuss some recommendations...

---

## Table of Contents
- Preparing the data set
- Experiment design
- Writing performance tests
- Reading performance tests
- Overall performance results
- Use Cases
- Conclusions
- References

---

## Preparing the data set
In order to reduce noise in our performance measurements, for this section we will employ a slightly larger file. We will be using the `Spotify Charts` data set (`2.48 GB`) published by `DHRUVIL DAVE`, which you can download from [Kaggle](https://www.kaggle.com/datasets/dhruvildave/spotify-charts).

We can start by importing all the required modules:

##### **Code**
```Python
import csv
import numpy as np
import pandas as pd
from fastavro import reader, writer, parse_schema
import pickle
import time
import os
```

Then, we can read the data set as a `pandas.DataFrame` object:

##### **Code**
```Python
# Load csv file as pandas.DataFrame object
df = pd.read_csv('datasets/charts.csv')
```

This should take a couple of minutes, depending on the specifications of your machine.

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

Lastly, we will create a new directory where we will store all of our written files:

##### **Code**
```PowerShell
mkdir performance_tests
```

Now, we're ready to start designing our experiment.

---

## Experiment design
For both writing & reading performance tests, we will be using a collection of measurements per file format. This is always good practice in experimental design, and will help us calculate a complete set of descriptive statistics.

Our experiment for the writing process will consist of the following steps:
1. Define the variables to measure.
2. Set the number of trials as a control variable.
3. Begin with the first trial, measuring variables of interest.
5. Store measurements.
6. Repeat for the other file formats.
7. Repeat steps 2 through 6, changing the control variable (*number of trials*).
8. Consolidate results and perform a statistical description.

Our experiment for the reading process will consist of the following steps:
1. Define the variables to measure.
2. Set the number of trials as a control variable.
3. Begin with the first trial, measuring variables of interest.
5. Store measurements.
6. Clear memory
7. Repeat for the other file formats.
8. Repeat steps 2 through 6, changing the control variable (*number of trials*).
9. Consolidate results and perform a statistical description.

---

## Writing performance tests
We will start by defining a set of control variables:

##### **Code**
```Python
# Define n number of trials
n3 = 20
```

We will then declare a function that will accept 

---

## Side-by-Side Comparison & Performance Tests


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

---

## Use Cases

---


## Conclusions
In summary, not all tabular file formats are good for every application. Each of them were created with a purpose in mind, and are better or worse at some applications than the others.

Serialized formats for example, present several advantages over non-serialized formats, but the inverse also happens: serialized formats may lose stability across versions, and usually consume more processing resources when serializing/deserializing objects.

Before implementing a format, specially in a production environment, it's important to make a detailed assessment of which formats are going to be used and how the encoding is to be handled. Also, when working with other collaborators,  setting a strict standard for data formatting & handling is of vital importance.

## References
https://www.geeksforgeeks.org/working-csv-files-python/