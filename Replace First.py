"""
In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

example:
starting list -> [1, 2, 3, 4]
end list -> [2, 3, 4, 1]

Input: List.

Output: Iterable.

Example:
replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
replace_first([1]) == [1]
"""

from typing import Iterable

def replace_first(items: list) -> Iterable:
    temp = []
    if len(items) > 1:
        for i in range(1, len(items)):
            temp.append(items[i])
        temp.append(items[0])
        items = temp
    return items

print("Tests:")
print(replace_first([1, 2, 3, 4]))
print(replace_first([1]))
print(replace_first([]))