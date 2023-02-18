#=
Created on Wed Jan 25 19:31:58 2023
@author: Pablo Aguirre
GitHub: https://github.com/pabloagn
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact
Part of Blog Article: programming-best-practices-writing-better-code
=#




# ----------------------

# Test packages
using DataFrames
using Plots
using LinearAlgebra

# Test libraries
x = range(0, 10, length=100)
y = sin.(x)
plot(x, y)

# Read a CSV file into a DataFrame object