"""
Given a non-empty array of integers, return the result
of multiplying the values together in order.

Example:
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""

def grow(arr):
    b = 1
    for a in arr:
        b = b*a
    return b

print("Tests:")
print(grow([1, 2, 3]))
print(grow([4, 1, 1, 1, 4]))
print(grow([2, 2, 2, 2, 2, 2]))