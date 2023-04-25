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

In this Blog Article, we'll start by discussing R's main features, and talk about what makes R a great option for statistical & scientific computing. We'll then install R along with RStudio, and discuss different ways we can use to manage packages and dependencies in our R environment. We'll go over R's main syntactic elements, variable declaration, data types & data structures, logical and arithmetic operators, some of the most relevant mathematical functions, vectorized operations, flow control using mainly conditional constructs, reading & writing files using different formats, and plotting using different types of plots. We'll close this segment by providing next steps for those interested in learning more about R, depending on the targeted application.

We'll be using R scripts which can be found in the [Blog Article Repo](https://github.com/pabloagn/blog/tree/master/computer-science/r-for-beginners).

---

# Table of Contents
- Why R?]()
	- Statistical computing]()
	- Data visualization]()
	- Syntax]()
	- Functional programming]()
	- Package management]()
	- Community]()
	- Academia]()
- What to expect]()
- Creating a new project]()
- Package management]()
	- Loading/unloading base packages]()
	- Managing third-party packages]()
		- Using the built-in installer]()
		- Using pacman]()
	- Useful packages]()
- Help]()
- Variables]()
- Printing & viewing]()
	- Using print()]()
	- Using paste() & paste0()]()
	- Using print() & paste()]()
	- Using cat()]()
	- Using message()]()
	- Using View()]()
- Data types]()
	- Logical]()
	- Numeric]()
	- Integer]()
	- Complex]()
	- Character]()
	- Raw]()
	- Checking a variable's type]()
		- Using typeof()]()
		- Using class()]()
- Data structures]()
	- Vectors]()
		- Vectors as ranges or sequences]()
	- Matrices]()
	- DataFrames]()
		- Getting dimensions]()
		- Getting column names]()
		- Accessing columns]()
		- Extracting columns]()
	- Lists]()
	- Factors]()
	- Arrays]()
	- data.table]()
- Operators]()
	- Arithmetic operators]()
	- Comparison operators]()
	- Logical operators]()
- Mathematical functions]()
- Flow control]()
	- Using if]()
	- Using if-else]()
	- Using for loop]()
	- Using nested loops]()
	- Using while loop]()
	- Using repeat-break]()
	- Using return]()
	- Using next]()
- Functions]()
	- Named functions]()
		- Without arguments]()
		- With arguments]()
		- With default arguments]()
	- Anonymus functions]()
- Vectorized operations]()
- Reading files]()
	- Reading CSV files]()
	- Reading TXT files]()
	- Reading parquet files]()
	- Reading JSON files]()
- Writing files]()
	- Writing to CSV]()
	- Writing to TXT]()
	- Writing to parquet]()
	- Writing to JSON]()
- Plotting]()
	- Using the base package]()
	- Plotting bar charts]()
- JupyterLab]()
- [Next steps]()
- [Conclusions](#conclusions)
- [References](#references)
- [Copyright](#copyright)

---

# Why R?
Why learn R, when we have Python? As we'll see later on, it's not a question about which language to use, but how to use both for what they're best. Python and R have been the gold standard for Data Science-related tasks for some time now. However, there's no denying that Python excels at tasks that R simply does not, and vice versa.

We can then talk about the main advantages R brings to the table, and how to leverage them in conjunction with Python.

## 1. Statistical computing
R was specifically designed for statistical computing and analysis, so it has a comprehensive set of built-in libraries for data manipulation, modeling, and visualization. There are many reasons why R is better at statistical computing than Python

### 1.1 Built-in statistical functions and packages
This might be the main reason why R excels at statistical computing; it was created as a statistical language, from statisticians, to statisticians. This means that R has considerably more built-in methods for statistical computing.

### 1.2 Data visualization
Statistical analysis is inherently intertwined with data visualization. This is because visualizations let us identify patterns and trends faster, communicate insights in a more concise way, identify outliers quickly, and many other applications. Since R is a statistical language, it's naturally packed with visualization packages that make working with plots in R a breeze, while also being beautiful.

### 1.3 Community support
When we're dealing with any science, it's helpful to have constant interaction with a community specialized in the domain we're studying. Statistics is no different; there is a vast community specialized in the field, more than willing to help if we get stuck in the way. Additionally, this help not only comes in the form of the actual writing of code, but also in the theoretical aspect of statistics. 

## 2. Specialized applications
Another thing to bear in mind is that, while Python is considered a general-purpose language, R is not (*at least not entirely*); R is generally used for more specialized analytic and research applications. That is not to say we cannot deploy a production application using R, but its core functionalities are oriented towards specialized analysis (*even so that CRAN offers a per-scientific-domain package classification*).

## 3. Data visualization
WE already mentioned that R has a powerful and flexible graphics system. This allows us to easily create beautiful, high-quality visualizations of data. While Python has libraries such as `Matplotlib` and `Seaborn`, R's `ggplot2` is widely considered to be the gold standard data visualization library.

## 4. Syntax
R has a syntax that is specifically designed for statistical computing, which makes it easier to write and read statistical code. The syntax is also highly consistent, which makes it easier to learn and remember. For example, it would be easier to translate a statistical research paper directly to R, than to Python.

## 5. Functional programming
Functional programming in the context of R has many advantages:
- **Easier to reason about code:** R's functional programming features, such as higher-order functions and closures, allow for the creation of modular and composable code that is easier to reason about. This can lead to more reliable and maintainable code, as well as easier debugging and testing.
- **Improved performance:** We are able to write more efficient and optimized code, as well as easier parallelization and distributed computing. For example, functions such as `lapply` and `sapply` can apply a function to a list or vector in a parallelized and optimized way.
- **Flexibility and expressiveness:** We can write more flexible and expressive code that can be tailored to specific use cases. For example, functional programming in R allows for more powerful data manipulation capabilities, as well as the creation of custom functions that can be reused across different projects.
- **Data pipelining:** We are able to create data pipelines, which are sequences of functions that operate on a dataset to produce a desired output. This can make data manipulation and analysis more streamlined and efficient.

More generally, functional programming introduces a new way of thinking about problem-solving using code; concepts such as recursion and piping are extremely valuable, and can often result in better performing code.

## 6. Package management
R has a built-in package repository (*CRAN*), which makes it easy to find and install packages for a wide range of statistical and machine learning tasks. In addition, there are various package management tools such as `pacman` and `packrat`, which make our life easier when managing our project's dependencies.

## 7. Community
R has a large and active community of users, which means that there are many resources available for learning and troubleshooting. Additionally, the community is specialized in statistical computing, so we also get a collection of domain experts that can and will help if we get stuck reasoning about our code.

---

# What to expect
If we're coming from a Python context, several of R's syntactic elements are very similar between the two. Variable declaration, data types, and objects also share similarities. The main difference is that the main paradigm in R is functional programming, while in Python is Object-oriented programming (OOP). This means that while in Python it's more common to use iteration-based approaches for interacting with data structures, in R, these are not as widely used; instead, R has a wide variety of built-in functions for performing vectorized operations.

Additionally, R is specialized in statistical computing; this means that many of its functions will be tailored for this purpose, and some of its main methods and concepts will be more statistically oriented.

This segment is meant to serve as an introduction to the R language; we will not be diving deep into all of its methods; however, we will be diving reasonably deep into some of R's core concepts around data wrangling, statistical computing, plotting.

---

# Installation
For this segment, we'll be using the R language along with RStudio, an IDE tailored for working with R.

We will also install some packages, which will come later when we get to the dependencies section.

The installation and setup will be focused on the Windows operating system. Still, a similar process can be used for macOS or Unix-like platforms.

## 1. R
We will first install the latest stable release of the R programming language. We can head to the official [CRAN R Download Page for Windows](https://cran.r-project.org/bin/windows/base/). We will click on *Download R for Windows*. Once we have it, we'll run the executable and follow the steps below:
- A
- A
- A
- A


## 2. RStudio
RStudio is an IDE developed by Posit (*previously RStudio*). We could use VS Code, Spyder, or even PyCharm. However, RStudio brings in a wide variety of useful features to the table, as we'll see further on.

To download RStudio, we will head to the [Official Posit RStudio Desktop Download Page](https://posit.co/download/rstudio-desktop/). We'll click on *Download RStudio Desktop for windows*, and wait for the executable to download. We'll then follow the steps below:
- A
- A
- A
- A

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

| Package        | Description                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `tidyverse`        | A collection of multiple Data Science packages.                                                                                                     |
| `dplyr`        | Manipulating DataFrames.                                                                                                     |
| `ggplot2`      | Creating beautiful visuals.                                                                                                  |
| `data.table`   | A faster alternative to `data.frame`.                                                                                        |
| `tidyr`        | For tidying data.                                                                                                            |
| `stringr`      | For working with strings.                                                                                                    |
| `lubridate`    | For working with date information.                                                                                           |
| `httr`         | For working with website data.                                                                                               |
| `ggvis`        | Interactive visualizations.                                                                                                  |
| `rio`          | Importing & exporting data.                                                                                                  |
| `rmarkdown`    | Interactive markdown notebooks.                                                                                              |
| `pacman`       | Package manager.                                                                                                             |
| `IRkernel`     | Jupyter Notebook kernel for R.                                                                                               |
| `readr`        | For reading files more easily.                                                                                               |
| `jsonlite`     | For working with `.json` files.                                                                                              |
| `tseries`      | For time series analysis.                                                                                                    |
| `RColorBrewer` | For creating color palettes for `ggplot2`.                                                                                   |
| `ggmap`        | For data visualization using maps.                                                                                           |
| `sqldf`        | For using SQL syntax in DataFrames.                                                                                          |
| `caret`        | For classification and regression training.                                                                                  |
| `GGally`       | Extends `ggplot2` by adding several functions to reduce the complexity of combining geometric objects with transformed data. |
| `ggthemes`     | Provides additional `ggplot2` themes and scales.                                                                             |
| `plotly`       | Create interactive web graphics from 'ggplot2' graphs and/or a custom interface                                              |

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
- `paste()` & `paste0()`
- `print()` & `paste()`
- `cat()`
- `message()`
- `View()`

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
There are 7 main data structures in R:
- **Vectors**: A basic data structure that can hold a sequence of values of the same data type.
- **Matrices**: A two-dimensional array that can hold a collection of values of the same data type.
- **Arrays**: A multi-dimensional data structure that can hold a collection of values of the same data type.
- **Lists**: A data structure that can hold a collection of values of different types.
- **DataFrames**: A two-dimensional table-like data structure in R that can hold a collection of values of different types.
- **Factors**: A data structure that is used to represent categorical variables.
- **Tables**: A special type of data structure in R that is used to represent tabular data.

Additionally, there are third-party packages that provide more data structures built on top of the base structures: 
- **Data tables:** The `data.table` package provides a faster alternative to the `data.frame` class.
- **Tidy data:** A standard way of mapping the meaning of a dataset to its structure when using the `tidyr` package.
- **Time series data:** The `xts` and `zoo` packages provide tools for working with time series data in R.
- **Spatial data:** The `sp` and `sf` packages provide tools for working with spatial data in R.

For the third-party libraries, we'll only be reviewing the `data.tables` class.

## 1. Base structures

### 1.1 Vectors
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

### 1.1.1 Vectors as ranges or sequences
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

### 1.2 Matrices
**Matrices** are two-dimensional arrays that contain data of the same data type. They are created by combining vectors, and can be manipulated using matrix algebra.

### 1.3 Arrays
**Arrays** are similar to matrices, but can have more than two dimensions.

### 1.4 Lists
**Lists** are a collection of objects of different data types, and can contain other data structures such as vectors, matrices, and data frames. They are highly flexible and can be used to store complex data structures.

### 1.5. DataFrames
**DataFrames** are similar to matrices, but they can contain columns of different data types. They are commonly used to store and manipulate data in R, and are similar to DataFrames in Python.

DataFrames are widely used in R, since they provide an object we can use to perform transformations to our data. This is why we'll spend a little bit more time exploring DataFrames.

We can build a DataFrame of two columns by using 2 vectors, each one for specifying a column:

##### **Code**
```R
mydata <- data.frame(x = 1:5, y = c("1", "2", "3", "4", "5"))
class(mydata)
print(mydata)
```

##### **Output**
```
[1] "data.frame"

  x y
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
```

We can see that upon calling `print()`, the index and the contents get outputted to `stdout`.

#### 1.5.1 Getting dimensions
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

#### 1.5.2 Getting column names
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

#### 1.5.3 Accessing columns
We can access the column of a DataFrame by using the dollar sign `$` after our DataFrame, and before the target column name:

##### **Code**
```R
# Read data
df <- read.csv("datasets/gdp_countries.csv")

# Access head of Country column
head(df$Country)
```

##### **Output**
```
[1] "United States"  "China"          "Japan"          "Germany"        "India"          "United Kingdom"
```

#### 1.5.4 Extracting columns
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

#### 1.5.5 Aa


### 1.6 Factors
**Factors** are used to represent categorical data in R, and are created from vectors. They can be ordered or unordered, and are commonly used in statistical modeling.

### 1.7 Tables

## 2. External libraries

### 2.1 data.table
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

# Flow control
In R, flow control can be achieved by using conditional constructs. The main constructs are:
- `if`
- `if`-`else`

We also have loop constructs, but are not encouraged when writing functional code:
- `for`
- `while`
- `repeat`-`break`

Additionally, we also have constructs for ending or returning values in a given execution flow:
- `return`
- `next`
- `break`

## 1. Conditional constructs

### 1.1 Using if


### 1.2 Using if-else

## 2. Loop constructs

### 2.1 Using for loop
We will not be investing too much time in `for` and `while` loops, since as we mentioned, they are discouraged in functional programming, in favor of using vectorized operations or recursion. However, it's still important to know that they exist, and that they can be used.

A `for` loop is 

### 2.2 Using nested loops

### 2.3 Using while loop

### 2.4 Using repeat-break

## 3. Returning constructs

### 3.1 Using return


### 3.2 Using next



---

# Functions
Functions in R can be named or anonymous. They can also be defined without parameters, with parameters, or with default parameters.

## 1. Named functions

## 2. Antonymous functions

## 3. Functions without parameters

## 4. Functions with parameters

## 5. Functions with default parameters

---

# Vectorized operations
We mentioned that vectorization is a key feature of functional programming languages, but, what is vectorization?

Vectorized operations are methods that allow us to perform operations on entire vectors of data at once, rather than looping over each element individually. This can result in significant performance improvements and more concise and readable code.

There are multiple methods for vectorized operations in R. In fact, we already used some of them when performing arithmetic, comparison and logical operations between vectors.

## 1. Vectorized arithmetic operations
If we're working with vectors in R, arithmetic operations are vectorized operations. We can perform operations between vectors:

##### **Code**
```R
x <- c(1, 2, 3)
y <- c(4, 5, 6)

# Vector addition
x + y

# Vector multiplication
x * y

# Vector exponentiation
x ^ 2
```

##### **Output**
```

```

## 2. Vectorized comparison operations


## 3. Vectorized logical operations


## 4. Vectorized mathematical functions


## 5. Vectorized transformation functions


### 5.1 The apply() family
The `apply()` family of functions is used to apply a function to a matrix or array, and to return a vector or array of results. These functions are built-in, and can be accessed without the need of library importing:
- `apply()`
- `lapply()`
- `sapply()`
- `tapply()`

#### 5.1.1 apply()


#### 5.1.2 lapply()


#### 5.1.3 sapply()


#### 5.1.4 tapply()


### 5.2 The dplyr package
The `dplyr` package is a third-party package that provides a wide range of functions and tools for data manipulation and transformation, many of them vectorized.



### 5.3 The tidyr package
The `tidyr` package is a third-party package that provides a wide range of functions and tools for data tidying, cleaning and preprocessing, many of them vectorized.

---

# Reading files
R is a statistical analysis language, meaning we'll probably be spending some time reading datasets in multiple file formats, from multiple sources; R provides a wide range of methods for reading datasets. Additionally, there are third-party languages for reading more specialized file formats such as `.parquet` & `.avro` datasets. 

For this section, we'll be using the [country-gdp dataset](https://www.kaggle.com/datasets/ppb00x/country-gdp) provided by [spear>](https://www.kaggle.com/ppb00x), available on [Kaggle](https://www.kaggle.com/).

## 1. Reading CSV files
R provides a great built-in method for reading `.csv` files into DataFrame objects. We can read a csv tile using the `read.csv()` built-in method:

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
Similarly, we can read a `.txt` file using 

## 3. Reading Parquet files


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


## 3. Writing to Parquet


## 4. Writing to JSON



---

# Plotting

## 1. Using the base package
The `plot` base package in R adapts to the data types we're using; it generates plots automatically based on our data types (*e.g., the most common plot for a categorical variable in the $x$ axis vs a numerical variable in the $y$ axis, would be a boxplot*).

## 2. Plotting bar charts


---

# JupyterLab
This segment would not be complete without at least mentioning `JupyterLab`; an interactive development environment (*IDE*) for working with Jupyter notebooks, code, and data.

If we come from a Python context, we're probably we'll aware of this environment; the great thing is that it also supports R, among other languages.

`IRkernel` is a kernel for Jupyter notebooks that enables the use of the R programming language. It's available as a CRAN package, which we can download using the following syntax:

##### **Code**
```R
install.packages("IRkernel")
```

Upon installation, we need to register the kernel with Jupyter notebooks by running the following command:

##### **Code**
```R
IRkernel::installspec()
```

And voila, we have an R JupyterLab kernel. From there, we can create a new R Jupyter Notebook in our current directory by using the following syntax:

##### Code
```PowerShell
New-Item -ItemType File -Path ".\MyNotebook.ipynb"
```

We then have two options:
- **Using VS Code:** Open the newly-created notebook in VS Code, and select the appropriate R Kernel.
- **Using a web browser:** We can head to the terminal and execute `jupyter notebook`. This will launch a new Jupyter Lab server, which we can access using a web browser.

---

# Next steps
We're reviewed a lot of information. However, this segment is meant to serve as an introduction to the R language. There are a vast amount of resources to further deepen our understanding, either for depending our understanding on a specific domain, or just learning R as an additional data processing & analysis tool:

*Disclaimer: None of the resources below are sponsored. All the material was selected by myself.*

First stops:
- **[The R Project](https://www.r-project.org/)**: Contains material for everything R-related, including a list of contributors, bug reporting, conferences, mailing lists, contributions, R Blogs, R Foundation, manuals, certifications, bibliographical resources, and all kinds of useful information.
- **[CRAN](https://cran.r-project.org/)**: We already mentioned how The Comprehensive R Archive Network can be useful for downloading packages. However, CRAN also contains a wide variety of documentation sheets and FAQs for all kinds of packages. Additionally, visiting CRAN and seeing the latest and greatest is always a great way to get a glimpse of where R is heading.
- **[R Topic, GitHub](https://github.com/topics/r)**: A great way to get in touch with the latest developments in the R community.
- **[R Source, GitHub](https://github.com/wch/r-source)**: The official GitHub repository for the R language source code. Great if we'd like to report an issue, see the latest releases and developments, and more.
- **[Posit](https://posit.co/products/open-source/rstudio/)**: remember we mentioned RStudio as being an amazing IDE for R? Well, the company behind it is Posit. In their official RStudio page, we'll be able to find all kinds of information regarding the IDE, as well as enterprise-level solutions for professional workflows.
- **[TidyVerse](https://www.tidyverse.org/)**: An opinionated collection of R packages designed for data science. All packages share an underlying design philosophy, grammar, and data structures.

Forums:
- **[#rstats, Twitter](https://twitter.com/search?q=%23rstats)**: A responsive, welcoming, and inclusive community of R users to interact with on Twitter
- **[R weekly](https://rweekly.org/)**: An incredible weekly recap of all R-related content.
- **[R Conferences](https://jumpingrivers.github.io/meetingsR/events.html)**: An index of community-led conferences around the globe.
- **[useR!](https://user2022.r-project.org/)**: The biggest annual R conference.

Bibliographical resources:
- **[R in Action, Manning Publications](https://www.manning.com/books/r-in-action-third-edition)**: A practical textbook focusing on data analysis and graphics with R and [Tidyverse](https://www.tidyverse.org/).
- [R for Data Science, O'Reilly](https://www.oreilly.com/library/view/r-for-data/9781491910382/)
- [Art of R Programming, No Starch Press](https://nostarch.com/artofr.htm)
- [R Graphics Cookbook, O'Reilly](https://www.oreilly.com/library/view/r-graphics-cookbook/9781491978597/)
- [R Cookbook, O'Reilly](https://www.oreilly.com/library/view/r-cookbook-2nd/9781492040675/)
- [Machine Learning with R, Packt](https://www.amazon.com/Machine-Learning-techniques-predictive-modeling/dp/1788295862)

Paid resources:
- **[HarvardX, Data Science Professional Certificate](https://www.edx.org/professional-certificate/harvardx-data-science)**: An extensive 9-course program focused on teaching probability theory & statistics, data analysis, data science, and ML in R.
- **[R Programming, Johns Hopkins University](https://www.coursera.org/learn/r-programming)**: A great intermediate-level course targeting data analysis.

---

# Conclusions
In this segment we discussed what the R language is, and how to install it along with RStudio, a great IDE offering a wide variety of functionalities. We then discussed some of R's main features such as relevant syntactic elements, variable declarations, data types & data structures, logical and arithmetic operators, mathematical functions, vectorized operations, flow control, reading & writing files, and plotting. We closed this segment by providing domain-specific next steps.

In a Python-centric world, we can sometimes opt for ease-of-use over performance. We tend to stick to what we know better, but the reality is that Python is just not great at some applications. Statistical modeling, scientific computing, plotting, and domain-specific research are sometimes better in R.

Additionally, Python and R are not meant to be used separately; in fact, RStudio provides support for creating and editing Python scripts, executing Python code, and interacting with Python packages and libraries. Also, the `reticulate` R package provides an interface to Python, allowing us to execute Python code from R and to pass data between both languages. Conversely, the `rpy2` package in Python provides the same inverse functionality.

As we can see, this is not an OR question, but an AND question, particularly if we're working on statistical, ML, domain-specific or scientific projects.

---

# References
- Aaa

---

# Copyright
Pablo Aguirre, Creative Commons Attribution 4.0 International, All Rights Reserved.