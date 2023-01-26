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
	
# Breaking comments in a newline
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

msw = (3, 1, 4.3, 6.5, 2)
kEla = [4, 3, 5, 6, 7, 3]
thePanty = [1, 2, 3, 4, 5]
theOtherpanty = [4, 3, 6, 7, 8, 2]
mthBreather = [8, 7, 1, 4, 5, 6]
xyz = 3.1416

for w in range(len(mthBreather)):
    theOtherpanty.append(w)
    for d in thePanty:
        print(xyz)
    copyofthePanty = thePanty.copy()
    

myTuple = (3, 1, 4.3, 6.5, 2)
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




#--------------------------





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
    if type()
    
    if age1 < 0 or age1 < 0 or age1 < 0:
        print('Please provide positive integers')
    
    
    
    return 









