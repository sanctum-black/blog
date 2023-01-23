# 6 Big Data File Formats Compared, Pt. 3
Over the last 2 articles of this series, we have discussed... 

In this section, we will focus on making a side-by-side comparison of the formats reviewed, as well as making performance tests for writing times, reading times and CPU processing resources...

We will then conclude this series by reviewing specific use-cases for each one of the formats involved, as well as discuss some recommendations...

---

## Table of Contents
- Side-by-Side Comparison & Performance Tests
- Use Cases
- Conclusions
- References

---

## Side-by-Side Comparison & Performance Tests
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

---

## Use Cases

---


## Conclusions
In summary, not all tabular file formats are good for every application. Each of them were created with a purpose in mind, and are better or worse at some applications than the others.

Serialized formats for example, present several advantages over non-serialized formats, but the inverse also happens: serialized formats may lose stability across versions, and usually consume more processing resources when serializing/deserializing objects.

Before implementing a format, specially in a production environment, it's important to make a detailed assessment of which formats are going to be used and how the encoding is to be handled. Also, when working with other collaborators,  setting a strict standard for data formatting & handling is of vital importance.

## References
https://www.geeksforgeeks.org/working-csv-files-python/