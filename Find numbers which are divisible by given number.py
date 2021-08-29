"""
Complete the function which takes two arguments and returns
all numbers which are divisible by the given divisor.
First argument is an array of numbers and the second is
the divisor.

Example
divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
"""

def divisible_by(numbers, divisor):
    return [n for n in numbers if n % divisor == 0]

print("Tests:")
print(divisible_by([1,2,3,4,5,6], 2))
print(divisible_by([1,2,3,4,5,6], 3))
print(divisible_by([0,1,2,3,4,5,6], 4))
print(divisible_by([0], 4))
print(divisible_by([1,3,5], 2))
print(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1))