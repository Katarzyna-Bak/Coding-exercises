"""
 Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.

Example:
split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']

Precondition: 0<=len(str)<=100 
"""

from typing import Iterable

def split_pairs(a):
    endList = []
    for n in range(0, len(a), 2):
        if n < len(a)-1:
            endList.append(a[n:n+2])
        else:
            endList.append(a[n:n+2]+'_')
    return endList   

print("Tests:")
print(split_pairs('abcd'))
print(split_pairs('abc'))
print(split_pairs('abcdf'))
print(split_pairs('a'))
print(split_pairs(''))