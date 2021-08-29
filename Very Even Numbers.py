"""
Description:

#Task:
Write a function that returns true if the number is a "Very
Even" number.

If a number is a single digit, then it is simply "Very Even"
if it itself is even.

If it has 2 or more digits, it is "Very Even" if the
sum of it's digits is "Very Even".

#Examples:
input(88) => returns false -> 8 + 8 = 16 -> 1 + 6 = 7
=> 7 is odd 
input(222) => returns true
input(5) => returns false

input(841) => returns true -> 8 + 4 + 1 = 13 -> 1 + 3
=> 4 is even
Note: The numbers will always be 0 or positive integers!
"""

def is_very_even_number(n):
    while n > 9:
        n = str(n)
        n = sum(int(n[i]) for i in range(len(n)))
    return n % 2 == 0

print('Tests:')
print(is_very_even_number(584))
print(is_very_even_number(111))
print(is_very_even_number(222))
print(is_very_even_number(0))
print(is_very_even_number(5))
print(is_very_even_number(1234))
print(is_very_even_number(400000220))