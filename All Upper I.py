# Check if a given string has all symbols in upper case.
# If the string is empty or doesn't have any letter in it
# - function should return True.

# Input: A string.
# Output: a boolean.
# Example:
# is_all_upper('ALL UPPER') == True
# is_all_upper('all lower') == False
# is_all_upper('mixed UPPER and lower') == False
# is_all_upper('') == True
# Precondition: a-z, A-Z, 1-9 and spaces

def is_all_upper(text: str) -> bool:
    output = False

    if text == '' or text.isdigit() or text.isupper():
        output = True
    elif len(text) > 0:
        for char in range(len(text)):
            if text[char] != ' ':
                break
            else:
                output = True
    return output

print("Tests:")
print(is_all_upper('ALL UPPER'))
print(is_all_upper('all lower'))
print(is_all_upper('mixed UPPER and lower'))
print(is_all_upper(''))
print(is_all_upper('126541'))
print(is_all_upper('12sddd6541'))
print(is_all_upper('12SAAAA6541'))
print(is_all_upper('      '))
print(is_all_upper(' '))
