"""
Your task in this kata is to implement a function
that calculates the sum of the integers inside
a string. For example, in the string
"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy
dog", the sum of the integers is 3635.

Note: only positive integers will be tested.
"""

def sum_of_integers_in_string(s):
    temp = []
    sum = 0
    for i in s:
        if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            s = s.replace(i, ' ')
        temp = s.split()
    for t in temp:
        sum += int(t)
    return sum

print("Tests:")
print(sum_of_integers_in_string("12.4"))
print(sum_of_integers_in_string("h3ll0w0rld"))
print(sum_of_integers_in_string("2 + 3 = "))
print(sum_of_integers_in_string("Our company made approximately 1 million in gross revenue last quarter."))
print(sum_of_integers_in_string("The Great Depression lasted from 1929 to 1939."))
print(sum_of_integers_in_string("Dogs are our best friends."))
print(sum_of_integers_in_string("C4t5 are 4m4z1ng."))
print(sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))