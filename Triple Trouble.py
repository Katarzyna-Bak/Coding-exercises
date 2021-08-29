"""
Triple Trouble
Create a function that will return a string that
combines all of the letters of the three inputed
strings in groups. Taking the first letter of all
of the inputs and grouping them next to each other.
Do this for every letter, see example below!

E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length.
"""

def triple_trouble(a, b, c):
    result = ''
    for i in range(len(a)):
        result += a[i]+b[i]+c[i]
    return result

print('Tests:')
print(triple_trouble("aaa","bbb","ccc"))
print(triple_trouble("aaaaaa","bbbbbb","cccccc"))
print(triple_trouble("burn", "reds", "roll"))
print(triple_trouble("Bm", "aa", "tn"))
print(triple_trouble("LLh", "euo", "xtr"))