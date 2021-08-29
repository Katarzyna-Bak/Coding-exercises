"""
Given an array of numbers, check if any of the numbers are
the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array.
"""

def is_vow(inp):
    vowels = {117: 'u', 97: 'a', 105: 'i', 101: 'e', 111: 'o'}
    for i in range(len(inp)):
        if inp[i] in vowels.keys():
            inp[i] = vowels[inp[i]]
    return inp

print("Tests:")
print(is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106]))
print(is_vow([101,121,110,113,113,103,121,121,101,107,103]))
print(is_vow([118,103,110,109,104,106]))
print(is_vow([107,99,110,107,118,106,112,102]))
print(is_vow([100,100,116,105,117,121]))