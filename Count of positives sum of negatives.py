"""
Given an array of integers.

Return an array, where the first element is the count of
positives numbers and the second element is sum of negative
numbers.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13,
-14, -15], you should return [10, -65].
"""

def count_positives_sum_negatives(arr):
    negSum = 0
    posCount = 0
    for a in arr:
        if a > 0: posCount += 1
        elif a < 0: negSum += a
    return [posCount, negSum] if len(arr) > 0 else []

print("Tests:")
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([1]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
print(count_positives_sum_negatives([]))