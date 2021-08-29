"""
At the annual family gathering, the family likes to find
the oldest living family member’s age and the youngest
family member’s age and calculate the difference between them.

You will be given an array of all the family members' ages,
in any order. The ages will be given in whole numbers, so
a baby of 5 months, will have an ascribed ‘age’ of 0.
Return a new array (a tuple in Python) with [youngest
age, oldest age, difference between the youngest and
oldest age].
"""

def difference_in_ages(ages):
    a = sorted(ages)
    return (a[0], a[-1], a[-1] - a[0])

print('Tests:')
print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))
print(difference_in_ages([62, 0, 3, 77, 88, 102, 26, 44, 55]))
print(difference_in_ages([46, 86, 33, 29, 87, 47, 28, 12, 1, 4, 78, 92]))
print(difference_in_ages([66, 73, 88, 24, 36, 65, 5]))
print(difference_in_ages([0, 110]))
print(difference_in_ages([33, 33, 33]))