"""
In a given list the last element should become the first one.
An empty list or list with only one element should stay the same

Input: List.

Output: Iterable.

Example:
replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
replace_last([1]) == [1]
replace_last([]) == []
"""

def replace_last(line: list):
    output = []
    if len(line) > 1:
        output.append(line[-1])
        output += line[:-1]
        return output
    return line

print('Examples:')
print(replace_last([2, 3, 4, 1]))
print(replace_last([1, 2, 3, 4]))
print(replace_last([1]))
print(replace_last([]))