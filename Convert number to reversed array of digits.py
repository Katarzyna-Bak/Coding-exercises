"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
"""

def digitize(n):
    result = []
    number = str(n)
    for r in range(len(number)):
        result.append(int(number[r]))
    return result[::-1]

print("Tests:")
print(digitize(35231))
print(digitize(23582357))
print(digitize(984764738))
print(digitize(45762893920))
print(digitize(548702838394))