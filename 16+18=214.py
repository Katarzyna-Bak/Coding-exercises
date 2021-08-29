"""
For this kata you will have to forget how to add two numbers.
In simple terms, our method does not like the principle
of carrying over numbers and just writes down every number
it calculates :-)
You may assume both integers are positive integers.
"""

def add(num1, num2):
    result = ''
    a = str(num1)
    b = str(num2)
    
    if len(a) > len(b):
        b = '0'*(len(a)-len(b)) + b
    elif len(a) < len(b):
        a = '0'*(len(b)-len(a)) + a

    for i in range(len(a)):
        result += str(int(a[i]) + int(b[i]))
    
    return int(result)

print('Tests:')
print(add(2,11))
print(add(0,1))
print(add(0,0))
print(add(16,18))
print(add(26,39))
print(add(122,81))