"""
Your task is to make two functions, max and min (maximum
and minimum in PHP and Python, maxi and mini in Julia)
that take a(n) array/vector of integers list as input
and outputs, respectively, the largest and lowest number
in that array/vector.

#Examples
maximun([4,6,2,1,9,63,-134,566]) returns 566
minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
maximun([5]) returns 5
minimun([42, 54, 65, 87, 0]) returns 0
"""

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

print("Tests:")
print(maximum([-52, 56, 30, 29, -54, 0, -110]))
print(maximum([4,6,2,1,9,63,-134,566]))
print(maximum([534,43,2,1,3,4,5,5,443,443,555,555]))
print(maximum([9]))
print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(minimum([42, 54, 65, 87, 0]))
print(minimum([1, 2, 3, 4, 5, 10]))
print(minimum([-1, -2, -3, -4, -5, -10]))
print(minimum([9]))