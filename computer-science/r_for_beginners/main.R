# ------------------
# INSTALL PACKAGE MANAGER
# ------------------

# Installing packages
# install.packages("pacman")
# install.packages("IRkernel")

# ------------------
# LOAD THIRD-PARTY PACKAGES
# ------------------

# Gives a confirmation message
require(pacman)

# Does not give a confirmation message.
#library(pacman)

pacman::p_load(dplyr, GGally, ggplot2, ggthemes,
               ggvis, httr, lubridate, plotly, rio, rmarkdown,
               shiny, stringr, tidyr, data.table, readr,
               jsonlite, tseries, sqldf, caret, arrow, data.table)

# ------------------
# LOAD BASE PACKAGES
# ------------------

# Load base package
library(datasets)
library(readxl)

# ------------------
# CLEAR PACKAGES USING PACMAN
# ------------------

# Unload single third-party package
p_unload(tseries)

# Unload all third-party packages
# p_unload(all)

# Unload internal (base) package
detach("package:datasets", unload = TRUE)

# ------------------
# ASK FOR HELP
# ------------------
?cat

# ------------------
# COMMENTING
# ------------------

# Single Line

# Multiline
"
aa
"

# ------------------
# DECLARE VARIABLES
# ------------------

# Define a variable
myint <- 1

# Variables can start with periods
.myint <- 2

# Variables cannot start with numbers
1number <- 3
# Error: unexpected symbol in "1number"

# ------------------
# PRINTING
# ------------------

# Using print()

# Define variables
myint <- 7
myvec <- c(1, 2, 3, 4, 5)
mymat <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3)

# Print variables to stdout
print(myint)
print(myvec)
print(mymat)

# Using paste() & paste0()
myvar <- 7
paste("My variable is", myvar)
paste0("My variable is", myvar)

# Using print() and paste()
myint <- 7
myfloat <- 7.14
print(paste("int =", myint, "float =", myfloat))

# Using cat()
myint <- 7
myfloat <- 7.15
cat("int =", myint, "float =", myfloat, "\n")


# Using message()
x <- 10
if (x > 5) {
  message("x is greater than 5.")
} else {
  message("x is less than or equal to 5.")
}


# Using view
mymat <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3)
View(mymat)

# ---------------------------
# DATA TYPES - LOGICAL
# ---------------------------

# Define a logical variable
mybool <- TRUE
print(mybool)
print(typeof(mybool))

# ---------------------------
# DATA TYPES - NUMERIC
# ---------------------------

# Integer number
mynum <- 1
print(mynum)
print(typeof(mynum))

# Float
myfloat <- 3.1415
print(myfloat)
print(typeof(myfloat))

# ---------------------------
# DATA TYPES - INTEGER
# ---------------------------

# Integer
myint <- 30L
print(myint)
print(typeof(myint))

# ---------------------------
# DATA TYPES - COMPLEX
# ---------------------------

# Complex
mycomplex <- 30 + 2i
print(mycomplex)
print(typeof(mycomplex))


# ---------------------------
# DATA TYPES - CHARACTER
# ---------------------------

# Character
mychar1 <- 'Hello 1'
mychar2 <- "Hello 2"
print(mychar1)
print(mychar2)
print(typeof(mychar1))
print(typeof(mychar2))

# ---------------------------
# DATA TYPES - RAW
# ---------------------------

# RAW
myraw <- raw(7)
print(myraw)
print(typeof(myraw))

# ----------------------------
# DATA STRUCTURES - VECTORS
# ----------------------------

# Define a vector of integers
myvec1 <- c(10, 20, 30, 40, 50)
print(myvec1)

# Define a vector of strings
myvec2 <- c("Hello", "World")
print(myvec2)

# Index a vector (1-based indexing)
myvec1[2]

# Define a vector of integers representing a range
myrange <- 1:10
myrange[10]

# ---------------------------
# DATA STRUCTURES - MATRICES
# ---------------------------

# Create a matrix
mymatrix <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3)
print(mymatrix)

# ---------------------------
# DATA STRUCTURES - DATAFRAMES
# ---------------------------

# Create a DataFrame
mydata <- data.frame(x = 1:5, y = c("A", "B", "C", "D", "E"))

# Read data
df <- read.csv("datasets/gdp_countries.csv")

# Get dimensions
dim(df)
nrow(df)
ncol(df)

# Get column names
colnames(df)
names(df)

# Access columns
head(df$Country)



# Extract Country and GDP_per_capita using square brackets []
df_subset1 <- df[, c("Country", "GDP_per_capita")]

# Extract Country and GDP_per_capita using subset
df_subset2 <- subset(df, select = c("Country", "GDP_per_capita"))

# Get columns and shapes
colnames(df_subset1)
colnames(df_subset2)
dim(df_subset1)
dim(df_subset2)

# ---------------------------
# DATA STRUCTURES - LISTS
# ---------------------------

# Create a list
mylist <- list(a = 1, b = "hello", c = c(2, 4, 6))


# ---------------------------
# DATA STRUCTURES - FACTORS
# ---------------------------

# Create a vector of colors
mycolors <- c("red", "green", "blue", "red", "green", "red")

# Create a factor variable from the vector
myfactor <- factor(mycolors)

# Print the factor variable
print(myfactor)


# ---------------------------
# DATA STRUCTURES - ARRAYS
# ---------------------------

# Create a 2-dimensional array of numeric values
myarray2d <- array(data = c(1:27), dim = c(3, 3))
print(myarray2d)

# Create a 2-dimensional array of numeric values
myarray3d <- array(data = c(1:27), dim = c(3, 3, 3))
print(myarray3d)


# ---------------------------
# DATA STRUCTURES - DATA.TABLE
# ---------------------------

# Declare a data.table
dt <- data.table(A = c(10, 20, 30),
                 B = c(40, 50, 60),
                 C = c(TRUE, FALSE, TRUE)
                 )

class(dt)
typeof(df)
dim(dt)
nrow(dt)
ncol(dt)
colnames(dt)

# ---------------------------
# OPERATORS - ARITHMETIC
# ---------------------------

# Declare two variables
myvar1 <- 28
myvar2 <- 14
myvar3 <- 7

# Addition
myvar1 + myvar2

# Subtraction
myvar1 - myvar2

# Product
myvar1 * myvar2

# Division
myvar1 / myvar2

# Remainder (Modulus)
myvar1 %% 2

# Sum
sum(myvar1,
    myvar2,
    myvar3)

# Power
myvar3 ^ 2

# ---------------------------
# OPERATORS - COMPARISON
# ---------------------------

# Define three variables to compare
myvar1 <- 7
myvar2 <- 14
myvar3 <- 21

myvar1 > myvar2
myvar1 >= myvar2
myvar1 < myvar2
myvar1 <= myvar2
myvar1 == myvar2
all.equal(3.1416, 3.1415999)


# ---------------------------
# OPERATORS - LOGICAL
# ---------------------------

# Define three variables to compare
myvar1 = 7
myvar2 = 14
myvar3 = 21

# And
(myvar2 > myvar1) & (myvar1*2 == myvar2)

# Or
(myvar2 > myvar1) | (myvar1^2 == myvar2)

# Not
!(myvar1 == myvar2)



# ---------------------------
# MATHEMATICAL FUNCTIONS
# ---------------------------

# Square root
sqrt(49)

# Euler's number (exp(n) -> e^n)
exp(3)

# Natural logarithm
log(10)

# Logarithm base 10
log10(10)

# ---------------------------
# READING FILES
# ---------------------------

# Read a CSV file
df <- read.csv("datasets/gdp_countries.csv")
head(df)
typeof(df)
class(df)

# Read a TXT file



# ---------------------------
# WRITING FILES
# ---------------------------

# Write a DataFrame to a csv file
write.csv(df, file = "outputs/gdp_countries_written.csv", row.names = FALSE)

# Write a DataFrame to a parquet file
write_parquet(df, "outputs/gdp_countries_written.parquet")

# ---------------------------
# PLOTTING (BASE PACKAGE)
# ---------------------------

# Load datasets
load(datasets)

# Explore data
head(iris)

# Descriptive statistics
summary(iris)

# Plot
plot(iris)

# Plotting a categorical variable
plot(iris$Species)

# Plotting a numerical variable
plot(iris$Petal.Length)
plot(iris$Petal.Width)

# Plotting a categorical variable vs a numerical variable
plot(iris$Species, iris$Petal.Width)

# Plotting two numerical variables
plot(iris$Petal.Length, iris$Petal.Width)

# Plotting including parameters
plot(iris$Petal.Length, iris$Petal.Width,
     col = "#1a1a1a", # Hex code
     pch = 19, # Point Character (Solid circles for points)
     main = "Iris: Petal Length vs. Petal Width",
     xlab = "Petal Length",
     ylab = "Petal Width")

# Plotting using mathematical expressions
plot(cos, 0, 2*pi) # Function, min, max
plot(exp, 1, 5)
plot(dnorm, -3, 3,
     col = "#1a1a1a",
     lwd = 1, # Line width
     main = "Standard Normal Distribution",
     xlab = "Z-scores",
     ylab = "Density")

# ---------------------------
# CLEAN UP
# ---------------------------

# Clear plots
dev.off()

# Clear console
cat("\014")
