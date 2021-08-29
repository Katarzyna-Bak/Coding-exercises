"""
You need to count the number of digits in a given string.

Input: A Str.

Output: An Int.

Example:

count_digits('hi') == 0
count_digits('who is 1st here') == 1
count_digits('my numbers is 2') == 1
count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
count_digits('5 plus 6 is') == 2
count_digits('') == 0
"""

def count_digits(text: str) -> int:
    count = 0
    for t in text:
        if t in '0123456789':
            count += 1
    return count

print("Tests:")
print(count_digits('hi'))
print(count_digits('who is 1st here'))
print(count_digits('my numbers is 2'))
print(count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year'))
print(count_digits('5 plus 6 is'))
print(count_digits(''))