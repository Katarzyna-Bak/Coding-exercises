"""
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.
Output: A string.

Example:
backward_string_by_word('') == ''
backward_string_by_word('world') == 'dlrow'
backward_string_by_word('hello world') == 'olleh dlrow'
backward_string_by_word('hello   world') == 'olleh   dlrow'

Precondition: The line consists only from alphabetical symbols and spaces.
"""

def backward_string_by_word(text: str) -> str:
    spaces = []
    output = ''

    for i in range(len(text)):
        if text[i] == ' ':
            spaces += [i]

    text = text.split()

    for t in text:
        output += t[::-1]
        while len(output) in spaces:
            output += ' '
            
    return output

print('Tests:')
print(backward_string_by_word(''))
print(backward_string_by_word('world'))
print(backward_string_by_word('hello world'))
print(backward_string_by_word('hello   world'))
print(backward_string_by_word('welcome to a game'))
print(backward_string_by_word('welcome  to a   game'))