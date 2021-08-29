# Try to find out how many zeros a given number has at the end.

# Input: A positive Int
# Output: An Int.
# Example:
# end_zeros(0) == 1
# end_zeros(1) == 0
# end_zeros(10) == 1
# end_zeros(101) == 0

def end_zeros(num: int) -> int:
    num = str(num)
    rangeVal = len(num)
    index = -1
    count = 0

    for i in range(rangeVal):
        if num[index] == '0':
            count += 1
            index -= 1
        else:
            break
    
    return count

print("Tests:")
print(end_zeros(0))
print(end_zeros(1))
print(end_zeros(10))
print(end_zeros(101))
print(end_zeros(245))
print(end_zeros(100100))