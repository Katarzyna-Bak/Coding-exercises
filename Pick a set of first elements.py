"""
Write a function to get the first elements of asequence. Passing a parameter n (default=1) will return the first n elements of the sequence.

If n == 0 return an empty sequence []

Examples
arr = ['a', 'b', 'c', 'd', 'e']
first(arr)    # --> ['a']
first(arr, 2) # --> ['a', 'b']
first(arr, 3) # --> ['a', 'b', 'c']
first(arr, 0) # --> []
"""

def first(seq, n = 1): 
    return seq[:n]

seq = ['a', 'b', 'c', 'd', 'e']

print("Tests:")
print(first(seq))
print(first(seq, 0))
print(first(seq, 1))
print(first(seq, 2))
print(first(seq, 10))