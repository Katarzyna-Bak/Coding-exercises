"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.

Example:
beginning_zeros('100') == 0
beginning_zeros('001') == 2
beginning_zeros('100100') == 0
beginning_zeros('001001') == 2
beginning_zeros('012345679') == 1
beginning_zeros('0000') == 4
"""

def beginning_zeros(number: str) -> int:
    count = 0
    for i in range(len(number)):
        if number[i] == '0':
            count += 1
        else:
            break
    return count

print("Tests:")
print(beginning_zeros('100'))
print(beginning_zeros('001'))
print(beginning_zeros('100100'))
print(beginning_zeros('001001'))
print(beginning_zeros('012345679'))
print(beginning_zeros('0000'))