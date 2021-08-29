# You should return a given string in reverse order.

# Input: A string.
# Output: A string.
# Example:
# backward_string('val') == 'lav'
# backward_string('') == ''
# backward_string('ohho') == 'ohho'
# backward_string('123456789') == '987654321'

def backward_string(val: str) -> str:
    return val[::-1]

print("Tests:")
print(backward_string('val'))
print(backward_string(''))
print(backward_string('ohho'))
print(backward_string('123456789'))