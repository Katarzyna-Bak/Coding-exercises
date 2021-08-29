"""
There's a "3 for 2" (or "2+1" if you like) offer on mangoes.
For a given quantity and price (per mango),
calculate the total cost of the mangoes.

Examples
mango(3, 3) ==> 6    # 2 mangoes for 3 = 6; +1 mango for free
mango(9, 5) ==> 30   # 6 mangoes for 5 = 30; +3 mangoes for free
"""

def mango(quantity, price):
    result = 0
    for r in range(1, quantity+1):
        if r % 3 != 0:
            result += price
    return result

print('Tests:')
print(mango(3, 3))
print(mango(9, 5))