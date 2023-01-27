# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:48:18 2023

@author: Pablo Aguirre

GitHub: https://github.com/pabloaguirrenck
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact

Part of Blog Article: programming-best-practices-writing-better-code
"""

# -------------------------------
# -------------------------------
# Introduction
# -------------------------------
# -------------------------------

# In this file, we will review different techniques for
# improving code

# -------------------------------
# -------------------------------
# Legibility
# -------------------------------
# -------------------------------

# -------------------------------
# Authoring
# -------------------------------

# Include authoring metadata example
'''
Created on: Wed Jan 18 20:48:18 2023
@author: Lucifer Morningstar
contact: lucifermorningstar@gmail.com
'''

# -------------------------------
# Comments
# -------------------------------

# Simple commenting
# -------------------------------

# This is a comment

# Simple commenting
# -------------------------------

# Over-commenting
# -------------------------------

# Declare a while loop that prints 'Hello',
# and stops after 8 iterations
i = 0
while i < 8:
    print('Hello')
    i += 1
	
# Breaking comments in a new line
# -------------------------------

# Declare a list variable that will serve to store dictionaries. This is crucial since we won't be able to retrieve the objects otherwise.
mylist = []

# Declare a list variable that will serve to store dictionaries.
# This is crucial since we won't be able to retrieve the objects otherwise.
mylist = []

'''
Declare a list variable that will serve to store dictionaries.
This is crucial since we won't be able to retrieve the objects otherwise.
'''
mylist = []

# Section definition
# -------------------------------

# -------------------------------
# -------------------------------
# This denotes a section start point
# -------------------------------
# -------------------------------

# -------------------------------
# -------------------------------
# This denotes a section end point
# -------------------------------
# -------------------------------

# -------------------------------
# This denotes a subsection start point
# -------------------------------

# -------------------------------
# This denotes a subsection end point
# -------------------------------

# This denotes a subtitle
# -------------------------------

# +-----------------------------------------+
# |      This denotes a centered title      |
# +-----------------------------------------+


# -------------------------------
# Docstrings
# -------------------------------

def addAges(age1, age2, age3):
    '''
    Parameters
    ----------
    age1 : int
        Age 1, from 1 to 10.
    age2 : int
        Age 2, from 11 to 20.
    age3 : int
        Age 3, from 21 to 30.
    
    Returns
    -------
    sumOfAges : int
        Sum of ages 1, 2 and 3.
    '''

    sumOfAges = age1 + age2 + age3
    
    return sumOfAges


def addAges(age1, age2, age3):
'''
Parameters
----------
age1 : int
    Age 1, from 1 to 10.
age2 : int
    Age 2, from 11 to 20.
age3 : int
    Age 3, from 21 to 30.

Returns
-------
sumOfAges : int
    Sum of ages 1, 2 and 3.
'''

    sumOfAges = age1 + age2 + age3
    
    return sumOfAges


# -------------------------------
# Indentation
# -------------------------------

mylist1 = [1, 2, 3, 4,
     5, 6, 7, 8]

mylist2 = [1, 2, 3, 4,
		    5, 6, 7, 8]


mylist1 = [1, 2, 3, 4,
           5, 6, 7, 8]

mylist2 = [1, 2, 3, 4, 
           5, 6, 7, 8]


# -------------------------------
# Line breaks & parenthesis
# -------------------------------

myvar = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + \
        9 + 10 + 11 + 12

myvar = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 +
        9 + 10 + 11 + 12)

import numpy as np

# Declare a 3-dimensional numpy array
myarr = np.array([[[10,20,30,40], [50,60,70,80]]])

myarr = np.array([
                    [
                        [10,20,30,40],
                        [50,60,70,80]
                    ]
                ])

schema = {'type': 'record','name': 'dataset','namespace': 'dataset','doc': 'This schema consists of 1 int type and 7 string types','fields': [{'name': 'Name', 'type': 'string'},{'name': 'Age', 'type': 'int'},{'name': 'Occupation', 'type': 'string'},{'name': 'Country', 'type': 'string'},{'name': 'State', 'type': 'string'},{'name': 'City', 'type': 'string'}]}

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

# -------------------------------
# Approproate variable naming
# -------------------------------

styaway = (3, 1, 4.3, 6.5, 2)
Gobbledegook = [4, 3, 5, 6, 7, 3]
theCollywobbles = [1, 2, 3, 4, 5]
theothercollywobbles = [4, 3, 6, 7, 8, 2]
mthBreather = [8, 7, 1, 4, 5, 6]
KNickers = (1, 2, 3)
xyz = 3.1416

for w in range(len(mthBreather)):
    theothercollywobbles.append(w)
    for d in theCollywobbles:
        print(xyz)
    copyofthecollywobbles = theCollywobbles.copy()
    

myTuple = (3, 1, 4.3, 6.5, 2)
myTuple_2 = (1, 2, 3)
myList = [4, 3, 5, 6, 7, 3]
myList_2 = [1, 2, 3, 4, 5]
myList_3 = [4, 3, 6, 7, 8, 2]
myList_4 = [8, 7, 1, 4, 5, 6]
pi = 3.1416

for constants in range(len(myList_4)):
    myList_3.append(constants)
    
    for items in myList_2:
        print(pi)
    
    myList_2_copy = myList_2.copy()


# -------------------------------
# Spacing
# -------------------------------

myList = [1,2,3,4,5,6,  7, 8,9,10, 11]

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def myFun(x, y, z):
    x =+ 1
    y *= 1
    z -+ 1
    t = 3
    
    for i in range(x):
        t -= x

    return t


# -------------------------------
# Modularization & scalability
# -------------------------------

nums = [1, 2, 3, 4, 5]

total = 0

for x in nums:
    total += x
    
print(f'Sum of values is: {total}')


def getSum(nums):
    total = 0

    for x in nums:
        total += x
        
    print(f'Sum of values is: {total}')
    
    return total

nums_1 = [1, 2, 3, 4, 5]
nums_2 = [6, 7, 8, 9, 10]
nums_3 = [11, 12, 13, 14, 15]
nums_4 = [16, 17, 18, 19, 20] 

total_1 = getSum(nums_1)
total_2 = getSum(nums_2)
total_3 = getSum(nums_3)
total_4 = getSum(nums_4)

print(total_1, total_2, total_3, total_4)


from my_fun import getSum

nums_5 = [-3, -2, -1, 0, 1, 2, 3] 
total_5 = getSum(nums_5)


from my_fun import getSum as sumVals

nums_6 = [-3, -2, -1, 0, 1, 2, 3] 
total_5 = sumVals(nums_6)

# -------------------------------
# Performance
# -------------------------------

import numpy as np

myarr = np.array([1, 2, 3])

from numpy import array as arr

myarr = arr([1, 2, 3])

# Conventional for loop
mylist_1 = []
for i in range(5):
    mylist_1.append(i)

# List comprehension
mylist_2 = [i for i in range(5)]

# Print resulting objects
print(mylist_1)
print(mylist_2)


import time

num_trials = 100000000

# Conventional for loop
start = time.time()
mylist_1 = []

for i in range(num_trials):
    mylist_1.append(i)

end = time.time()
print('For loop execution time:', end-start, 'seconds')

# List comprehension
start = time.time()

mylist_2 = [i for i in range(num_trials)]

end = time.time()

print('List comprehension execution time:', end-start, 'seconds')

# New line variable assignment
myvar_1 = 1
myvar_2 = 2
myvar_3 = 3
myvar_4 = 4
myvar_5 = 5

# Single line variable assignment
myvar_1, myvar_2, myvar_3, myvar_4, myvar_5 = 1, 2, 3, 4, 5

# Define a decorator function
def decoratorFun(decoratedFun):
    
    def wrapperFun(*args, **kwargs):
        print('Start decorator')
        decoratedFun(*args, **kwargs)
        print('End decorator')
        
    return wrapperFun

@decoratorFun
# Define a simple function
def myFun(x, y):
    print(x, y)
    
myFun(7, 77)


# -------------------------------
# Testing and debugging
# -------------------------------

def addAges(age1, age2, age3):
    '''
    Parameters
    ----------
    age1 : int
        Age 1, from 1 to 10.
    age2 : int
        Age 2, from 11 to 20.
    age3 : int
        Age 3, from 21 to 30.

    Returns
    -------
    sumOfAges : int
        Sum of ages 1, 2 and 3.
    '''

    sumOfAges = age1 + age2 + age3
    
    return sumOfAges


addAges('1', '1', '0')

addAges('1', 2, 3)


def inputNum(num):
    '''
    Parameters
    ----------
    num : int
        Num, a real integer number.

    Returns
    -------
    num_s : str
        num as string type.
    '''
    if type(num) != int:
        raise TypeError('Please input a real integer number')

    else:
        num_s = str(num)

    return num_s

inputNum('a')


def inputNum(num):
    '''
    Parameters
    ----------
    num : int
        Num, a real integer number.

    Returns
    -------
    num_s : str
        num as string type.
    '''
    if type(num) != int:
        try:
            num_i = int(num)
            num_s = str(num_i)
        except ValueError:
            raise TypeError('Please input a real integer number')

    else:
        num_s = str(num)

    return num_s

inputNum('a')
inputNum(3.56)



def addAges(age1, age2, age3):
    '''
    Parameters
    ----------
    age1 : int
        Age 1, from 1 to 10.
    age2 : int
        Age 2, from 11 to 20.
    age3 : int
        Age 3, from 21 to 30.

    Returns
    -------
    sumOfAges : int
        Sum of ages 1, 2 and 3.
    '''
    if (type(age1) != int) | (type(age2) != int) | (type(age3) != int):
        raise TypeError('Please input an integer number.')
    
    elif (age1 <= 0) | (age2 <= 0) | (age3 <= 0):
        raise AttributeError('All numbers have to be positive and non-zero.')

    elif (age1 < 10) | (age2 < 20) | (age3 < 30):
        raise AttributeError('Age 1 must be between 1 and 10. '\
                             'Age 2 must be between 11 and 20. '\
                             'Age 3 must be between 21 and 30. ')

    else:
        sumOfAges = age1 + age2 + age3
        
    return sumOfAges

addAges('-1', 1, 1)

