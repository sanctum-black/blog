#=
Created on Wed Jan 25 19:31:58 2023
@author: Pablo Aguirre
GitHub: https://github.com/pabloagn
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact
Part of Blog Article: programming-best-practices-writing-better-code
=#

# Getting familiar with the VS Code extension
# ----------------------

# Test packages
using DataFrames
using Plots

# Test libraries
x = range(0, 10, length=100)
y = sin.(x)
plot(x, y)

z = round.(y, digits=4)

print(z)

# Reading a CSV file into a DataFrame object
using CSV, DataFrames 

df_1 = CSV.read("datasets/test.csv", DataFrame)

vscodedisplay(df_1)














# Data processing
# ----------------------

using CSV

# Reading a large CSV dataset into a DataFrame object
df_2 = CSV.read("datasets/books.csv", DataFrame)