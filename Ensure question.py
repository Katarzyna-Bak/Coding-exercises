"""
Given a string, write a function that returns the string with
a question mark ("?") appends to the end, unless the original
string ends with a question mark, in which case, returns the
original string.

ensure_question("Yes") == "Yes?" 
ensure_question("No?") == "No?"
"""

def ensure_question(s):
    return s if s.endswith('?') else s + '?'

print("Tests:")
print(ensure_question(""))
print(ensure_question("Yes"))
print(ensure_question("No?"))