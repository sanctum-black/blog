# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:31:58 2023
@author: Pablo Aguirre
GitHub: https://github.com/pabloagn
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact
Part of Blog Article: programming-paradigms-explained
"""

import time

# Implement a linear search algorithm
def linear_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            end_time = time.time()
            total_time = end_time - start_time
            print(f'Linear Search: {round(total_time, 4)} s')
            return i
        
    return -1

# Implement a binary search algorithm
def binary_search(arr, target):
    start_time = time.time()
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            end_time = time.time()
            total_time = end_time - start_time
            print(f'Binary Search: {total_time} s')
            return mid
            
        elif arr[mid] < target:
            start = mid + 1
            
        else:
            end = mid - 1
            
    return -1

# Declare a list and a target value
arr = [i for i in range(1000000000)]
target = 9999999

# Get results for both methods
linear_search(arr, target)
binary_search(arr, target)