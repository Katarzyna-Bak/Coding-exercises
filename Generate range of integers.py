"""
Implement a function named generateRange(min, max, step), which takes three arguments and generates a range of integers from min to max, with the step. The first integer is the minimum value, the second is the maximum of the range and the third is the step. (min < max)

Task
Implement a function named

generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
generate_range(1, 10, 3) # should return list of [1,4,7,10]
generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]

Note
- min < max
- step > 0
- the range does not HAVE to include max (depending on the step)
"""

def generate_range(min, max, step):
    return list(range(min, max+1, step))

print('Tests:')
print(generate_range(1, 10, 1))
print(generate_range(-10, 1, 1))
print(generate_range(1, 15, 20))
print(generate_range(1, 7, 2))
print(generate_range(0, 20, 3))