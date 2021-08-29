"""
This Kata is intended as a small challenge for my students

All Star Code Challenge #18

Create a function that accepts 2 string arguments and
returns an integer of the count of occurrences the 2nd
argument is found in the first one.

If no occurrences can be found, a count of 0 should be
returned.

Example (Inputs --> Output)
"Hello", 'o' => 1
"Hello", 'l' => 2
"", 'z'      => 0

Notes:
The first argument can be an empty string
The second string argument will always be of length 1
"""

def str_count(string, letter):
    return string.count(letter)

print('Tests:')
print(str_count('hello', 'l'))
print(str_count('hello', 'e'))
print(str_count('codewars', 'c'))
print(str_count('ggggg', 'g'))
print(str_count('hello world', 'o'))