"""
For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.

Input: A string.

Output: A string.

Example:
correct_sentence("greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends.") == "Greetings, friends."

Precondition: No leading and trailing spaces, text contains only spaces, a-z A-Z , and .
"""

def correct_sentence(text: str) -> str:
    tempLetter = text[0]
    if text[-1] != '.': text += '.'
    if tempLetter.islower: text = tempLetter.upper() + text[1:]
    return text

print("Tests:")
print(correct_sentence("greetings, friends"))
print(correct_sentence("Greetings, friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("hi"))
print(correct_sentence("welcome to New York"))