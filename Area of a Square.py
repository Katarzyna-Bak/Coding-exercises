"""
Complete the function that calculates the area of the
red square, when the length of the circular arc A is
given as the input. Return the result rounded to two
decimals.

Note: use the π value provided in your language (Math::PI,
M_PI, math.pi, etc)
"""

import math

def square_area(A):
    return round((2 * A / math.pi) ** 2, 2)

print('Tests:')
print(square_area(2))
print(square_area(0))
print(square_area(14.05))
print(square_area(1))
print(square_area(100))