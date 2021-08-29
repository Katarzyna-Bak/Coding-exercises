# Not all of the elements are important. What you need to
# do here is to remove from the list all of the elements
# before the given one.

# We have two edge cases here: (1) if a cutting element
# cannot be found, then the list shoudn't be changed.
# (2) if the list is empty, then it should remain empty.

# Input: List and the border element.
# Output: Iterable (tuple, list, iterator ...).
# Example:
# remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
# remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]

from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    if border not in items:
        result = items
    else:
        ind = int(items.index(border))
        result = items[ind:]
    return result

print("Tests:")
print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
print(list(remove_all_before([1, 1, 2, 2, 3, 3], 2)))
print(list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)))
print(list(remove_all_before([1, 1, 5, 6, 7], 2)))
print(list(remove_all_before([], 0)))
print(list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)))