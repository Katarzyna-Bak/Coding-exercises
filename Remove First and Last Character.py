"""
It's pretty straightforward. Your goal is to create a function
that removes the first and last characters of a string. You're
given one parameter, the original string. You don't have to
worry with strings with less than two characters.
"""

def remove_char(s):
    return s[1:-1]

print("Tests:")
print(remove_char('eloquent'))
print(remove_char('country'))
print(remove_char('person'))
print(remove_char('place'))
print(remove_char('ok'))
print(remove_char('ooopsss'))