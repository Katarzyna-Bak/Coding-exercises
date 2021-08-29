"""
Complete the function which converts a binary number
(given as a string) to a decimal number.
"""

def bin_to_decimal(inp):
    return int(inp, 2)

print('Tests:')
print(bin_to_decimal("0"))
print(bin_to_decimal("1"))
print(bin_to_decimal("10"))
print(bin_to_decimal("11"))
print(bin_to_decimal("101010"))
print(bin_to_decimal("1001001"))