"""
*** No Loops Allowed ***

You will be given an array (a) and a value (x). All
you need to do is check whether the provided array
contains the value, without using a loop.

Array can contain numbers or strings. X can be either.
Return true if the array contains the value, false if not.
With strings you will need to account for case.

Looking for more, loop-restrained fun? Check out the other
kata in the series:

https://www.codewars.com/kata/no-loops-1-small-enough
https://www.codewars.com/kata/no-loops-3-copy-within
"""

def check(a, x):
    return x in a

print('Tests:')
print(check([66, 101], 66))
print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))
print(check(['t', 'e', 's', 't'], 'e'))
print(check(['what', 'a', 'great', 'kata'], 'kat'))