"""
Implement String#digit? (in Java
StringUtils.isDigit(String)), which should return true
if given object is a digit (0-9), false otherwise.
"""

def is_digit(n):
    return n.isdigit() and len(n) == 1

print('Tests:')
print(is_digit(""))
print(is_digit("7"))
print(is_digit(" "))
print(is_digit("a"))
print(is_digit("a5"))