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

def is_majority(items: list):
    return items.count(True) > items.count(False)

print('Examples:')
print(is_majority([True, True, False, True, False]))
print(is_majority([True, True, False]))
print(is_majority([True, True, False, False]))
print(is_majority([True, True, False, False, False]))
print(is_majority([False]))
print(is_majority([True]))
print(is_majority([]))