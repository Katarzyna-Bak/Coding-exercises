"""
Complete the function, which calculates how much you need
to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%
The rating is case insensitive (so "great" = "GREAT").

If an unrecognised rating is received, then you need to
return:
"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#

Because you're a nice person, you always round up the tip,
regardless of the service.
"""

import math

def calculate_tip(amount, rating):
    tipPerc = {'Terrible': 0, 'Poor': 0.05, 'Good': 0.1, 'Great': 0.15, 'Excellent': 0.20}
    
    if rating.title() in tipPerc.keys():
        return math.ceil(amount * tipPerc[rating.title()])
    else:
        return 'Rating not recognised'

print('Tests:')
print(calculate_tip(30, "poor"))
print(calculate_tip(20, "Excellent"))
print(calculate_tip(20, "hi"))
print(calculate_tip(107.65, "GReat"))
print(calculate_tip(20, "great!"))