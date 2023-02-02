# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 19:23:00 2023
@author: Pablo Aguirre
GitHub: https://github.com/pabloagn
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact
Part of Blog Article: what-are-github-gists-and-how-to-use-them
"""

def myFun(my_list):
    '''
    Parameters
    ----------
    my_list : list
        Contains a set of integer numbers.

    Returns
    -------
    sum_of_nums : int
        The sum of the numbers inside my_list.
    '''
    print(f'List contains {len(my_list)} numbers.')
    
    sum_of_nums = 0

    for i in my_list:
        sum_of_nums += i

    print(f'Sum of numbers is {sum_of_nums}.')

    return sum_of_nums

my_list = [1, 2, 3, 4, 5]

myFun(my_list)