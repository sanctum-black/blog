# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:31:58 2023

@author: Pablo Aguirre

GitHub: https://github.com/pabloaguirrenck
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact

Part of Blog Article: programming-best-practices-writing-better-code
"""

def getSum(nums):
    total = 0

    for x in nums:
        total += x
        
    print(f'Sum of values is: {total}')
    
    return total