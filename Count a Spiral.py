"""
We have a List of booleans. Let's check if the majority of elements
are true.

Some cases worth mentioning: 1) an empty list should return false; 2)
if trues and falses have an equal amount, function should return false.

Input: A List of booleans.

Output: A Boolean.

Example:
is_majority([True, True, False, True, False]) == True
is_majority([True, True, False]) == True
"""

def spiral_sum(size):
    if size % 2 == 0:
        return size // 2 * size + size - 1
    else:
        return (size // 2 + 1) * size + size // 2

print('Examples:')
print(spiral_sum(5))
print(spiral_sum(10))
print(spiral_sum(1000))
print(spiral_sum(123456))
print(spiral_sum(584757902734057049235907840235937429075234))