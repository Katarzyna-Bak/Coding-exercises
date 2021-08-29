"""
Create a function (or write a script in Shell) that
takes an integer as an argument and returns "Even"
for even numbers or "Odd" for odd numbers.
"""

def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'

print('Tests:')
print(even_or_odd(2))
print(even_or_odd(1545452))
print(even_or_odd(74156741))
print(even_or_odd(100000))
print(even_or_odd(-123))