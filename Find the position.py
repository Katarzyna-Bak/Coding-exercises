"""
When provided with a letter, return its position in the
alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"

This kata is meant for beginners. Rank and upvote to bring
it out of beta
"""

def position(alphabet):
    pos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    return f'Position of alphabet: {pos.index(alphabet)+1}'

print("Tests:")
print(position("a"))
print(position("z"))
print(position("e"))