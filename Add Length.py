"""
What if we need the length of the words separated by
a space to be added at the end of that same word and
have it returned as an array?

add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and
returns an Array/list with the length of each word added
to each element .

Note: String will have at least one element; words will
always be separated by a space.
"""

def add_length(str):
    s = str.split()
    output = []
    
    for i in range(len(s)):
        output.append(f'{s[i]} {len(s[i])}')
        
    return output

print('Tests:')
print(add_length('apple ban'))
print(add_length('you will win'))
print(add_length('you'))
print(add_length('y'))