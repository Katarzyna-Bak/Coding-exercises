"""
You task is to implement an simple interpreter for the
notorious esoteric language HQ9+ that will work for
a single character input:

If the input is 'H', return 'Hello World!'
If the input is 'Q', return the input
If the input is '9', return the full lyrics of 99 Bottles
of Beer. It should be formatted like this:
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on
the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the
wall.
97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the
wall.
...
...
...
2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the
wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on
the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the
wall.
For everything else, don't return anything (return null in
C#, None in Rust). 
(+ has no visible effects so we can safely ignore it.)
"""

def HQ9(code):
    d = {1: 'bottles of beer', 2: 'on the wall', 3: 'Take one down and pass it around'}
    bottle = ''
    n = 99
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9':
        for n in range(99, 2, -1):
            bottle += f'{n} {d[1]} {d[2]}, {n} {d[1]}.\n{d[3]}, {n-1} {d[1]} {d[2]}.\n'
        bottle += f'2 {d[1]} {d[2]}, 2 {d[1]}.\n{d[3]}, 1 bottle of beer on the wall.\n1 bottle of beer {d[2]}, 1 bottle of beer.\n{d[3]}, no more {d[1]} {d[2]}.\nNo more {d[1]} {d[2]}, no more {d[1]}.\nGo to the store and buy some more, 99 {d[1]} {d[2]}.'
        return bottle
    else:
        return None

print('Tests:')
print(HQ9('H'))
print(HQ9('Q'))
print(HQ9('9'))
print(HQ9('X'))