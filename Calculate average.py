"""
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""

def find_average(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum/len(numbers)

print("Tests:")
print(find_average([1, 2, 3]))