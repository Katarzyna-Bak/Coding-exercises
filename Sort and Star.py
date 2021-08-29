"""
You will be given a vector of strings. You must sort it
lphabetically (case-sensitive, and based on the ASCII
values of the chars) and then return the first value.

The returned value must be a string, and have "***" between
each of its letters.

You should not remove or add elements from/to the array.
"""

def two_sort(array):
    return '***'.join(min(array))

print("Tests:")
print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))
print(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]))
print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]))
print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]))