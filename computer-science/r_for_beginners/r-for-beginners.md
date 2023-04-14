<article class="first">
  <div class="title">
    <h1>R for Beginners</h1>
  </div>
</article>

---

[![made-with badge](https://img.shields.io/static/v1?label=Made%20with&message=Obsidian&color=7d5bed&logo=obsidian&labelColor=1a1a1a&style=flat)](https://obsidian.md/)

[![type](https://img.shields.io/static/v1?label=Type&message=blog&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAi0lEQVRIS+2WMQ7AIAhF/UNXrtP7rz2OYxeqTWxMTBUSxQVXfnzyQQKC8YExL7zAGCNbgIkIsIKVhBw4vbR7unR6Gp0LvwxXd2v+EvkdDpxWXpWlRTyi9/pABRyBJHEHSlxSadxSlV0SsVsqcUml2W/pynWxnsXNisHMRxrCl8qvH3ECnQDuOmy+0zwB4WNxmUKgwwAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/) [![category](https://img.shields.io/static/v1?label=Category&message=computer-science&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAB9UlEQVRIS6VWMU7DQBDkDAQEdrAoCISCAomCL1DxC95Azy9oeQS/oOIHVFAgREFoCHGCRSzZzEU+63LZ9W6CO/vudmZ2d9Zn1pTPaDSqut2usduHw+FpFEUv7t1fk8LNAkiPDWj3+ADuTPjNvXMxWwGzLCuqqtqwh5MkiY0xEwfOAfrEKFAWUBO4DZQDXgCEqjuouvbZUanUrocpngMMVUkKtKC+WhFQUudAUd8r1PkepJ/w7Tysn4uzkNJlascF9WOASAki6w0xrn19b3Gpps5y3kRfJADPZgr9gJSP0EgDHDiQ/Mp50PfxAmDtuQhsZmb/z0OVhwSkmGrSGp5bGRDp3EFaJ5JaiahdZ2vYNj/JkWVMgW7sgNw2yOW+99gacp7TeFE72OcUrgo4Ho93+/3+D5T9QmGHm0BNSnHgMI7jj9Ai2tElZGCK9S3S+GA4BcNNydBaIuEstu/iLJWCa+pLDm+Nz+xQAsBenucnRVG8asFq0s/Yf9YoVAI21wyn3N4I7M1A8ijWHwB42XrFqIO9YfMRlVqqyXC5ukED3nIEVJcoBXv1lmWa5gIpeeQioyTWVj1uXf0DpgKUZbmfpunXKnVnU9rWDKiTHRSDNkDu36iqIQK/Q+mxU8sBYniL/1EVoJ9Wqwo/5x6Cf9YKv6Em1XbNH5bGfSwvuRe1AAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/categories/computer-science/) [![technologies](https://img.shields.io/static/v1?label=Technologies&message=R,%20RStudio,%20PowerShell%207&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA1klEQVR4nM2RMW7CUBBEnUikIQUIlBJxrrQgJG7ABRBnoUkaWhpoUgWJlgNYbvz/G1dUi1ayoy87rpOtVrszs6OdLPtXlef5UNJXjHHcCwohjMzsKZ3FGN+Bq/e+c0xHGfiWtEznkg6SNnW/dIxjs0YJ2AMnM3tJSFPgHkKY17gBcAQ+zOw5A3aSbsCkdW0NnNOZY2rstpcInJ3cS/SzwGdqtSzLmdusquqtIXWsehVF8QpcJK1qmxt/TMv6wjE/z0leP27i8Ag8inT/axxtAQ+9o/zn9QD3JOiyTjnQEQAAAABJRU5ErkJggg==&labelColor=1a1a1a&style=flat)](https://pabloagn.com/technologies/) [![website article](https://img.shields.io/static/v1?label=Website&message=Post%20Link&color=e60048&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB+ElEQVR4nO2VOYgUURCGR/BAI4MN1EwjI89EMDYQvNBNNNlcE0VBUdlUUSMjj2BF2UDRePDAwGzNF2GNPIYd8Hjv/6YnEHSf/FIDPTJiu4nJFBTd1Kv6/nrVBd1q/S8DJiU9AmaBm5LOSjoATPwDY0LSQUnnzDArmJOjkqclvQceSHohaR6oJC1JeiPprqT9pZSVg5pSyirH4sw5S1EzbwZwP5jTIwWBdj1meEppZ6/XOyXpCdCX9Am4Fv45Yo+Bk1VV7ag3FNz2kKC7yznvHiX4u3U6nXU55xPAW7vfHfvLmNtmW8NaFux67k0Ea03esTfJJQTj23bHgiNtPNK6jZem3Wpg46Wp23hp2q0GNl6axksjaRGYkXRF0mnHq6ra2HSk/X5/k6RDks6YEazFPwnuBS5KuirptqTnkj4CJZ4zwNFSytqBoP/2wDHgXi33A/BM0i2zzDR7SBC4LGlPr9fb5huVUlYMus45b5E0FYJfgQS8C8/Al7jJVEpp86DODLPMNDs0up7xXBQZVKLLb8CCpIfA+ZzzvpTS+lLKGuAI8DT8cClltc+c49yoWQjGL140ao25oW8QXW1IKe3KOR8Hbkh66ZtI+i7plaG+iR244JjP3HDkXnetGWbVp9XYopHtHgvwWtIPu9+BSx7bssBNDdhqX07xT/Jbz1SBBDGHAAAAAElFTkSuQmCC&labelColor=1a1a1a&style=flat)](https://pabloagn.com/blog/r-for-beginners/)

R is an open-source, dynamically-typed, multi-paradigm programming language mainly used for statistical computing. It provides a wide variety of statistical and graphical techniques and is highly extensible due to the vast amount of community packages found in CRAN.

Many times, R gets compared with Python, particularly in the Data Science, ML & Scientific programing context; both offer great capabilities, but when talking about statistical computing, R is just better.  

In this Blog Article, we'll

We'll be using R scripts which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/computer-science/r-for-beginners).

---

# Table of Contents
- Why R?
	- Statistical computing
	- Data visualization
	- Syntax
	- Functional programming
	- Package management
	- Community
	- Academia
- What to expect
- Creating a new project
- Package management
	- Loading/unloading base packages
	- Managing third-party packages
		- Using the built-in installer
		- Using pacman
	- Useful packages
- Help
- 
- [Next steps]()
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# Why R?
Why learn R, when we have Python?

## 1. Statistical computing
R was specifically designed for statistical computing and analysis, so it has a comprehensive set of built-in libraries for data manipulation, modeling, and visualization.

## 2. Data visualization
R has a powerful and flexible graphics system, which makes it easy to create high-quality visualizations of data. While Python has libraries such as Matplotlib and Seaborn, R's ggplot2 is widely considered to be the best data visualization library.

## 3. Syntax
R has a syntax that is specifically designed for statistical computing, which makes it easier to write and read statistical code. The syntax is also highly consistent, which makes it easier to learn and remember.

## 4. Functional programming

## 5. Package management
R has a built-in package management system (CRAN), which makes it easy to find and install packages for a wide range of statistical and machine learning tasks.

## 6. Community
R has a large and active community of users, which means that there are many resources available for learning and troubleshooting.


## 7. Academia




---

# What to expect
If we're coming from a Python context, several of R's syntactic elements are very similar between the two. Variable declaration, data types, and objects also share similarities. The main difference is that the main paradigm in R is functional programming, while in Python is Object-oriented programming (OOP). This means that while in Python it's more common to use iteration-based approaches for interacting with data structures, in R, these are not as widely used; instead, R has a wide variety of built-in functions for performing vectorized operations.

Additionally, R is specialized in statistical computing; this means that many of its functions will be tailored for this purpose, and some of its main methods and concepts will be more statistically oriented.

This segment is meant to serve as an introduction to the R language; we will not be diving deep into all of its methods; however, we will be diving reasonably deep into some of R's core concepts around data wrangling, statistical computing, plotting.

---

# Creating a new project
In RStudio:
- Head to file
- Select `Create new project`
	- New directory
	- Existing directory
- Project Type: New Project

Some files will be created:
- `.Rproj.user`: Contains user-specific project settings and temporary files that are generated as we work on the project in R Studio. Some of the files stored in the `.Rproj.user` folder include our RStudio workspace, which contains information about our current R session (*such as loaded packages, defined functions, and created objects*); our RStudio project history, which includes a log of your interactions with the project in R Studio; and our RStudio project options, which are settings specific to the project (*such as the project's working directory and build tools*).
- `r_for_beginners.Rproj`

---

# Package management
There are two ways to perform package management in R, depending if the packages are base or third-party: 
- **Base packages:** They are already installed with the latest R language installation, but are not loaded by default when we start a project.
- **Contributed (*Third-party*)**: They require download, install and load separately. Two main sources can be used:
	- [CRAN](https://cran.r-project.org/): Comprehensive R Archive Network. Packages need to be accepted by the CRAN team, and must meet certain requirements such as documentation, functionality, non-redundancy, reliability, efficiency, compliance, incensing, and maintenance.
	- [GitHub](https://github.com/trending/r): User-created packages which may or may not have not been officially accepted in the CRAN repository. This means that packages might not be fully tested, and may introduce unexpected behavior in our R projects.

We can view CRAN packages using two main ways:
- [The complete CRAN index](https://cran.r-project.org/web/packages/index.html)
- [Packages in CRAN by topics](https://cran.r-project.org/web/views/)

## 1. Loading/unloading base packages
As we mentioned, base packages come with the R language installation. We can load a base package in our current environment by using the following syntax:

##### **Code**
```R
# Gives a confirmation message
require(datasets)

# Does not give a confirmation message.
library(datasets)
```

Once we load a package (*base or third-party*), its methods and data will be stored in memory and become available upon calling.

If we would like to unload a base loaded package for increasing memory availability, we can do so by using the following syntax:

##### **Code**
```R
detach("package:datasets", unload = TRUE)
```

This will effectively clear the package contents from memory.

## 2. Managing third-party packages
There is a wide variety of package managers we can use to manage third-party packages:
- **GitHub:** For GitHub hosted packages.
- **`packrat`**: A package management system for R that allows us to manage packages and their dependencies within a project. It can be used to ensure that our code runs consistently across different systems and environments.
- **`pacman`**: A package manager that provides a convenient way to load and manage packages and dependencies in R.
- **`renv`**: A package management system for R that provides a way to isolate and manage package dependencies within a project.

For this segment we'll be using the built-in installer and `pacman` to manage our packages and dependencies.

### 2.1 Using the built-in installer
R has a built-in installer for installing third-party packages. However, it's simple and does not have advanced dependency-management capabilities.

We can install a third-party package using the following syntax:

##### **Code**
```R
install.packages("pacman")
```

Once we installed our package, we can simply load it using `library(pacman)`.

### 2.2 Using pacman
Pacman itself is a package; we already installed and loaded it to our environment in our previous step.

We can then use `pacman` to install and load third-party packages using the following syntax (*will install if not found*): 

##### **Code**
```R
pacman::p_load(dplyr, GGally, ggplot2, ggthemes,
               ggvis, httr, lubridate, plotly, rio, rmarkdown,
               shiny, stringr, tidyr, data.table, readr,
               jsonlite, tseries, sqldf, caret, arrow, data.table)
```

When we use the `pacman::p_load()` function to load other packages, we do not need to explicitly load `pacman` first. However, we do need to have `pacman` installed on our system before we can use its functions.

If we want to unload a third-party package that was loaded with `pacman`, we can use the following expression:

##### **Code**
```R
p_unload(dplyr)
```

The best practice when using a package manager is to always import base packages separately using `require` or `library`, then install / import third-party packages using our package manager, and finally unload using the appropriate method.

## 3. Useful packages
At the time of this writing, there are 18k+ packages in CRAN; this means we have plenty of options to choose from. However, there are some packages that are discipline-agnostic, and can be used in general applications.

Below are some of the most popular packages currently available in CRAN:

|Package       |Description                                                                                                                  |
|--------------|-----------------------------------------------------------------------------------------------------------------------------|
|`dplyr`       | Manipulating DataFrames.                                                                                                    |
|`ggplot2`     | Creating beautiful visuals.                                                                                                 |
|`data.table`  | A faster alternative to `data.frame`.                                                                                       |
|`tidyr`       | For tidying data.                                                                                                           |
|`stringr`     | For working with strings.                                                                                                   |
|`lubridate`   | For working with date information.                                                                                          |
|`httr`        | For working with website data.                                                                                              |
|`ggvis`       | Interactive visualizations.                                                                                                 |
|`rio`         | Importing & exporting data.                                                                                                 |
|`rmarkdown`   | Interactive markdown notebooks.                                                                                             |
|`pacman`      | Package manager.                                                                                                            |
|`IRkernel`    | Jupyter Notebook kernel for R.                                                                                              |
|`readr`       | For reading files more easily.                                                                                              |
|`jsonlite`    | For working with `.json` files.                                                                                             |
|`tseries`     | For time series analysis.                                                                                                   |
|`RColorBrewer`| For creating color palettes for `ggplot2`.                                                                                  |
|`ggmap`       | For data visualization using maps.                                                                                          |
|`sqldf`       | For using SQL syntax in DataFrames.                                                                                         |
|`caret`       | For classification and regression training.                                                                                 |
|`GGally`      | Extends `ggplot2` by adding several functions to reduce the complexity of combining geometric objects with transformed data.|
|`ggthemes`    | Provides additional `ggplot2` themes and scales.                                                                            |
|`plotly`      | Create interactive web graphics from 'ggplot2' graphs and/or a custom interface                                             |

###### *Table N: Most Useful General-Purpose Packages in CRAN* 

---

# Help
Asking for help in R is as simple as using the question mark `?` following the library or method we wish to get help for:

##### **Code**
```R
?print
```

##### **Output**
B016A033_help.png

---

# Commenting
We can include single line comments or multiline comments:

For single line comments, we use the hash `#` symbol:

##### **Code**
```R
# Single line comment
# Another single line comment
```

For multiline comment, we enclose our string in double quotes `""`:

##### **Code**
```R
"
Multiline comment
continues in line 2
"
```

We can also comment the entire selection by using the shortcut <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd> in RStudio for Windows. This will prepend every selected line with a hash `#` symbol.

---

# Variables
There are two ways of assigning variables in R:

The `<-` symbol is known as the "assignment operator". It assigns a value to a variable and is commonly used in R for this purpose. For example:

```R
x <- 10
```

On the other hand, the `=` symbol is also used for assignment in R, but it has a slightly different meaning. It is known as the "named argument" operator, and is typically used to pass named arguments to functions. For example:

```R
my_function(arg1 = "value1", arg2 = "value2")
```

In this case, the `=` symbol is used to specify the values for the named arguments `arg1` and `arg2`.

In most cases, `<-` and `=` can be used interchangeably for variable assignment, but it is generally recommended to use `<-` for this purpose, as it is the more commonly used operator for assignment in R.

---

# Printing & viewing
There are multiple ways we can use to print & view objects in R:
- `print()`
- `print0()`
- `message()`
- `cat()`
- `paste()`
- `cat()` & `paste()`
- `view()`

## 1. Using print()
The `print()` function is a generic function in R that can be used to print various types of objects to the console. When we call `print()` on an object, it prints the object to the console in a format that is appropriate for that object.

One thing to note, is that `print()` cannot be called by itself to print multiple comma-separated arguments. For that, we can use `paste()` instead.

Let us print some variables:

##### **Code**
```R
# Define variables
myint <- 7
myvec <- c(1, 2, 3, 4, 5)
mymat <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3)

# Print variables to stdout
print(myint)
print(myvec)
print(mymat)
```

##### **Output**
```
[1] 7
[1] 1 2 3 4 5
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
```

As we can see, the matrix representation is in table-form, which is convenient if we're working with multi-dimensional objects.

## 2. Using paste() & paste0()
The `paste()` function is used to concatenate strings and/or variables into a single character string.

The `paste0()` function provides the same result as `paste()`, with the only difference being there are no blank spaces inserted between statements.

Let us print two messages using both methods:

##### **Code**
```R
# Using paste() & paste0()
myvar <- 7
paste("My variable is", myvar)
paste0("My variable is", myvar)
```

##### **Output**
```
[1] "My variable is 7"
[1] "My variable is7"
```

## 3. Using print() & paste()

##### **Code**
```R
myint <- 7
myfloat <- 7.14
print(paste("int =", myint, "float =", myfloat))
```

##### **Output**
```
[1] "int = 7 float = 7.14"
```

## 4. Using cat()
The `cat()` function is used to concatenate and print its arguments to the console. It does not add any formatting or separators between the arguments.

##### **Code**
```R
myint <- 7
myfloat <- 7.15
cat("int =", myint, "float =", myfloat, "\n")
```

##### **Output**
```
int = 7 float = 7.15
```

## 5. Using message()
The `message()` function is similar to `print()`, but is used for informational messages rather than output that is part of a computation. It prints its arguments to the console, but does not return anything.

We can inform the user about the outcome of an evaluation:

##### **Code**
```R
x <- 10
if (x > 5) {
  message("x is greater than 5.")
} else {
  message("x is less than or equal to 5.")
}
```

##### **Output**
```
x is greater than 5.
```

Note that unlike the `print()` function, `message()` does not return anything, so we cannot assign its output to a variable or use it in a computation. It is intended for displaying messages to the user or providing information about the progress of a computation.

We can also use `cat()` or `paste()` functions to print messages to the console, but `message()` is preferred because it allows messages to be suppressed or redirected if needed.

## 6. Using View()
The `View()` method is not a printing method per se. Instead, it's a function used to view data in a spreadsheet-like format using an external viewer. The `View()` method is part of the `utils` package and provides a built-in viewer for data frames and array-like structures.

Let us try to view a matrix object:

##### **Code**
```R
mymat <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3)
View(mymat)
```

##### **Output**

B016A033_View.png

###### *Figure N: Matrix Displayed in External Viewer* 


---

# Data types
There are 6 main data types in R:
-   `logical`: Boolean (*i.e., `TRUE`, `FALSE`*)
-   `numeric`: Can be integer or floating point numbers.
-   `integer`: 
-   `complex`
-   `character`
-   `raw`

## 1. Logical

## 2. Numeric

## 3. Integer

## 4. Complex

## 5. Character

## 6. Raw

## 7. Checking a variable's type
There are two main ways we can use to determine a variable's type in R:
- Using `typeof()`
- Using `class()`

## 7.1 Using typeof()
`typeof()` returns a string that specifies the basic type of an R object. It tells us what kind of data structure an object is, without taking into account any attributes or methods that the object might have.

## 7.2 Using class()
`class()`, on the other hand, returns a string that specifies the class of an R object. It tells us what type of object it is, taking into account any attributes or methods that the object might have.

---

# Data structures

## 1. Vectors
**Vectors** are the simplest and most basic data structure in R. They can hold data of a single data type (*e.g., numeric, character, logical*), and can be of any length.

We can explicitly create vectors:

##### **Code**
```R
# Define a vector of integers
myvec1 <- c(10, 20, 30, 40, 50)
print(myvec1)

# Define a vector of strings
myvec2 <- c("Hello", "World")
print(myvec2)
```

##### Output
```
[1] 10 20 30 40 50
[1] "Hello" "World"
```

We can also index vectors using square brackets `[]`:

##### **Code**
```R
myvec1[2]
```

##### **Output**
```
20
```

We must keep in mind that R uses 1-based indexing, meaning the first index of any object is set to 1.

### 1.1 Vectors as ranges or sequences
There is no built-in `range` type in R. However, we can represent a `range`  by defining a vector of integers.

##### **Code**
```R
myrange <- 1:10
myrange[3]
```

##### **Output**
```
3
```

This declaration will be inclusive, meaning both 1 and 10 will be included in our object.

As we will see later on, these types of declarations are useful when we would like to perform iterations.

## 2. Matrices
**Matrices** are two-dimensional arrays that contain data of the same data type. They are created by combining vectors, and can be manipulated using matrix algebra.


## 3. DataFrames
**DataFrames** are similar to matrices, but they can contain columns of different data types. They are commonly used to store and manipulate data in R, and are similar to DataFrames in Python.

DataFrames are widely used in R, since they provide an object we can use to perform transformations to our data. This is why we'll spend a little bit more time exploring DataFrames.

We can declare a DataFrame:



### 3.n Getting dimensions
- `dim()`: Returns the shape of a DataFrame. The output will be a vector.
- `nrow()`: Returns the number of rows. The output will be an integer.
- `ncol()`: Returns the number of columns. The output will be an integer.

##### **Code**
```R
# Read data
df <- read.csv("datasets/gdp_countries.csv")

# Get dimensions
dim(df)
nrow(df)
ncol(df)
```

##### **Output**
```
[1] 212   8
[1] 212
[1] 8
```

### 3.n Getting column names
There are two main methods for getting the column names of a DataFrame:
- `colnames()`: Specific method for extracting the column names.
- `names()`: Can also be used to get or set the names of other R objects, such as vectors or lists.

##### **Code**
```R
# Read data
df <- read.csv("datasets/gdp_countries.csv")

# Get column names
colnames(df)
names(df)
```

##### **Output**
```
[1] "Rank"           "ID"             "Country"        "Continent"      "Population"     "IMF_GDP"        "UN_GDP"         "GDP_per_capita"
[1] "Rank"           "ID"             "Country"        "Continent"      "Population"     "IMF_GDP"        "UN_GDP"         "GDP_per_capita"
```

As we can see, both methods return the same output.

### 3.n Accessing columns
We can access the column of a DataFrame by using the following syntax:

##### **Code**
```R

```

### 3.n Extracting columns
We can access and extract the columns of a given DataFrame using two main methods:
- Using square brackets `[]`.
- Using `subset()` method.

##### **Code**
```R
# Read data
df <- read.csv("datasets/gdp_countries.csv")

# Extract Country and GDP_per_capita using square brackets []
df_subset1 <- df[, c("Country", "GDP_per_capita")]

# Extract Country and GDP_per_capita using subset
df_subset2 <- subset(df, select = c("Country", "GDP_per_capita"))

# Get columns and shapes
colnames(df_subset1)
colnames(df_subset2)
dim(df_subset1)
dim(df_subset2)
```

##### **Output**
```
[1] "Country"        "GDP_per_capita"
[1] "Country"        "GDP_per_capita"
[1] 212   2
[1] 212   2
```

As we can see, we get the same output.

### 3.n 

## 4. Lists
**Lists** are a collection of objects of different data types, and can contain other data structures such as vectors, matrices, and data frames. They are highly flexible and can be used to store complex data structures.


## 5. Factors
**Factors** are used to represent categorical data in R, and are created from vectors. They can be ordered or unordered, and are commonly used in statistical modeling.


## 6. Arrays
**Arrays** are similar to matrices, but can have more than two dimensions.

## 7. data.table
The last structure we'll review will be the `data.table`. This class is not included in the base packages of R. It is an external package that needs to be installed separately.

The reason why we included this class, is because, even though it's built top of R's `data.frame` class, `data.table` offers many improvements such as fast grouping and aggregation, fast join operations, memory efficiency, and extended syntax. In short, it's designed for efficiently working with large datasets and provides faster and more memory-efficient operations than traditional data frames.

Let us first install the package:

##### **Code**
```R
pacman::p_load(data.table)
```

We can then declare a simple data.table using the following syntax:

##### **Code**
```R
# Declare a data.table
dt <- data.table(A = c(10, 20, 30),
                 B = c(40, 50, 60),
                 C = c(TRUE, FALSE, TRUE)
                 )

# Check type, class and dimensions
class(dt)
typeof(df)
dim(dt)
nrow(dt)
ncol(dt)
colnames(dt)
```

##### **Output**
```
[1] "data.table" "data.frame"
[1] "list"
[1] 3 3
[1] 3
[1] 3
[1] "A" "B" "C"
```

As we can see, a `data.table` has its own class, but also inherits the `data.frame` class. Also, the `data.table` and `data.frame` class  are both based on R's `list` type.

We can then perform some operations on our table:

##### **Code**
```R

```

---

# Operators
R provides arithmetic, rational and logical operators, which can be used for multiple data types and structures.

## 1. Arithmetic operators
An arithmetic operator is a mathematical function that takes two operands and performs a calculation on them.

Below are the main arithmetic operators in R:

| Operator    | Description          |
| ----------- | -------------------- |
| `+`         | Addition             |
| `-`         | Subtraction          |
| `*`         | Product              |
| `/`         | Division             |
| `%%`        | Reminder (*Modulus*) |
| `^`         | Power                |
| `sum(a, b)` | Sum of a and b       |

###### *Table N: Arithmetic Operators in R*

It's important to remember that the operations get executed in **PEMDAS** order:
- Parenthesis: `()`
- Exponent: `^`
- Multiplication and Division (*left to right*): `*`, `/`
- Addition and Subtraction (*left to right*): `+`, `-`

## 2. Comparison operators
A comparison operator is a sign or symbol used to compare two expressions or values and returns a Boolean value of either true or false.

R provides the most relevant comparison operators:

| Operator | Description              |
| -------- | ------------------------ |
| `>`      | Greater than             |
| `<`      | Less than                |
| `==`     | Equal to                 |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |
| `!=`     | Different than           |

###### *Table N: Comparison Operators in R*

All of the operators above will return a boolean value once evaluated. However, there is one additional operator,  `all.equal(A, B)`, that can be used to compare how equal are two values; this method will not return a boolean value. Instead, it will return the [mean relative difference](https://stats.stackexchange.com/questions/21587/how-to-find-mean-relative-differences).

## 3. Logical operators
Logical operators are used to combine two or more logical expressions or values. R provides the three basic logical operators:

| Operator | Description              |
| -------- | ------------------------ |
| `&`      | And                |
| <code>&#124;</code>      | Or |
| `!`      | Not             |

###### *Table N: Logical Operators in R*

We can use the to compare multiple expressions:

##### **Code**
```R
# Define three variables to compare
myvar1 <- 7
myvar2 <- 14
myvar3 <- 21

# And
(myvar2 > myvar1) & (myvar1*2 == myvar2)

# Or
(myvar2 > myvar1) | (myvar1^2 == myvar2)

# Not
!(myvar1 == myvar2)
```

##### **Output**
```
[1] TRUE
[1] TRUE
[1] TRUE
```

---

# Mathematical functions

---

# Reading files
https://www.kaggle.com/datasets/ppb00x/country-gdp

## 1. Reading CSV files
We can read a csv tile using the `read.csv()` built-in method:

##### **Code**
```R
# Read a csv file
df <- read.csv("datasets/gdp_countries.csv")
head(df)
```

##### **Output**
```
  Rank  ID        Country     Continent Population      IMF_GDP       UN_GDP GDP_per_capita
1    1 840  United States North America  339996.56 2.669515e+13 1.862448e+13       78515.94
2    2 156          China          Asia 1425671.35 2.186548e+13 1.121828e+13       15336.97
3    3 392          Japan          Asia  123294.51 5.291351e+12 4.936212e+12       42916.35
4    4 276        Germany        Europe   83294.63 4.564778e+12 3.477796e+12       54802.79
5    5 356          India          Asia 1428627.66 3.893670e+12 2.259642e+12        2725.46
6    6 826 United Kingdom        Europe   67736.80 3.686935e+12 2.647899e+12       54430.31
```

We check the type of the object the file was read into:

##### **Code**
```R
typeof(df)
class(df)
```

##### **Output**
```
[1] "list"
[1] "data.frame"
```

We can see we get two different answers; the reason is that in R, a DataFrame is not a basic type; it's implemented as a special kind of `list`, where each element of the `list` corresponds to a column in the data frame.

## 2. Reading TXT files


## 3. Reading parquet files


## 4. Reading JSON files


---

# Writing files
Conversely, we can also write to files of different formats.

## 1. Writing to CSV


## 2. Writing to TXT

### 2.1 

### 2.2. Using cat() & paste()
Both `cat()` and `paste()` can also be used to write output to a file, rather than to the console.

To do this, we can specify a file argument:

##### **Code**
```R
cat("This is output to a file.", file = "output.txt")
```

##### **Code**
```R
message <- paste("This is output to a file.", "This is a second line.")
writeLines(message, "output.txt")
```

##### **Code**
```R

```



## 3. Writing to parquet


## 4. Writing to JSON


---

# Plotting

## 1. Using the base package
The `plot` base package in R adapts to the data types we're using; it generates plots automatically based on our data types (*e.g., the most common plot for a categorical variable in the $x$ axis vs a numerical variable in the $y$ axis, would be a boxplot*).

## 2. Plotting bar charts


---

# Conclusions
Aaa

---

# References
- Aaa

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.