"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""

def square_sum(numbers):
    result = 0
    for n in numbers:
        result += n ** 2
    return result

print('Tests:')
print(square_sum([1,2]))
print(square_sum([0, 3, 4, 5]))
print(square_sum([]))
print(square_sum([-1,-2]))
print(square_sum([-1,0,1]))