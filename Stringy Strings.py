"""
write me a function stringy that takes a size and returns
a string of alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use
whole numbers.
"""

def stringy(size):
    result = ''
    for i in range(size):
        if i == 0 or i % 2 == 0: result += '1'
        else: result += '0'
    return result

print("Tests:")
print(stringy(5))
print(stringy(10)[0])
print(stringy(3))
print(stringy(12))
print(stringy(26))
print(stringy(28))