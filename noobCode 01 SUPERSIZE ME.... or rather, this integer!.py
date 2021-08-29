"""
Write a function that rearranges an integer into its
largest possible value.

Example (Input --> Output)
123456 --> 654321
105 --> 510
12 --> 21

If the argument passed through is single digit or is
already the maximum possible integer, your function
should simply return it.
"""

def super_size(n):
    result = ''
    tempList = sorted(str(n), reverse = True)
    for t in tempList:
        result += t
    return int(result)

print('Tests:')
print(super_size(69))
print(super_size(513))
print(super_size(2017))
print(super_size(414))
print(super_size(608719))
print(super_size(123456789))
print(super_size(700000000001))
print(super_size(666666))
print(super_size(2))
print(super_size(0))