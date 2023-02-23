"""
Created on Thu Feb 22 19:09:12 2023

@author: pablo aguirre

GitHub: https://github.com/pabloagn
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact

Part of Blog Article: the-motivations-behind-this-blog
"""

import string

def decodeString(**kwargs):
    '''
    Parameters
    ----------
    **kwargs : list, list
        An encrypted message.
        A list of uppercase alphabet letters.

    Returns
    -------
    decoded : string
        A decoded message.
    '''
    
    decoded = ''.join([my_alphabet[x] if x >=0 else ' ' for x in my_list])
    
    print(decoded)
    
    return decoded

# Declare message and alphabet
my_list = [0, -1,
           9, 14, 20, 17, 13, 4, 24, -1,
           19, 7, 17, 14, 20, 6, 7, -1,
           3, 0, 19, 0, -1,
           18, 2, 8, 4, 13, 2, 4]

my_alphabet = list(string.ascii_uppercase)

decodeString()