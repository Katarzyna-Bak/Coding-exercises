"""
You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.
"""

def small_enough(array, limit):
    return max(array) <= limit

print("Tests:")
print(small_enough([66, 101] ,200))
print(small_enough([78, 117, 110, 99, 104, 117, 107, 115] ,100))
print(small_enough([101, 45, 75, 105, 99, 107], 107))
print(small_enough([80, 117, 115, 104, 45, 85, 112, 115] ,120))
print(small_enough([1, 1, 1, 1, 1, 2] ,1))
print(small_enough([78, 33, 22, 44, 88, 9, 6] ,87))
print(small_enough([1, 2, 3, 4, 5, 6, 7, 8, 9] ,10))
print(small_enough([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12] ,12))