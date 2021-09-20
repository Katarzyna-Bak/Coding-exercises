"""
In this mission you should check if all elements in the given list
are equal.

Input: List.

Output: Bool.

Example:
all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True

The idea for this mission was found on Python Tricks series
by Dan Bader

Precondition: all elements of the input list are hashable
"""

from typing import List, Any


def all_the_same(elements: List[Any]):
    if len(set(elements)) >  1:
        return False
    return True

print("Examples:")
print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))
print(all_the_same(['a', 'a', 'a']))
print(all_the_same([]))
print(all_the_same([1]))