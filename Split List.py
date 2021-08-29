"""
You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. If it has no elements, then two empty arrays should be returned.

example

Input: Array.

Output: Array or two arrays.

Example:
split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) == [[1, 2], [3]]
"""
def split_list(items: list) -> list:
    if len(items) <= 1:
        return items,[]
    elif len(items) % 2 == 0:
        return items[:len(items)//2],items[len(items)//2:]
    else:
        return items[:len(items)//2+1],items[len(items)//2+1:]

print('Tests:')
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))