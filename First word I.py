# You are given a string and you have to find its first word.
# This is a simplified version of the First Word mission,
# which can be solved later.
# The input string consists of only English letters
# and spaces.
# There aren’t any spaces at the beginning and
# the end of the string.

# Input: A string.
# Output: A string.
# Example:
# first_word("Hello world") == "Hello"

def first_word(text: str) -> str:
    if ' ' in text:
        ind = int(text.find(' '))
    else:
        ind = len(text)
    return text[0:ind]

print("Tests:")
print(first_word("Hello world"))
print(first_word("a word"))
print(first_word("a word"))
print(first_word("a"))
print(first_word("hi"))