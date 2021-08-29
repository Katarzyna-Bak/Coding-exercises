"""
Given a string of digits, you should replace any digit below
5 with '0' and any digit 5 and above with '1'. Return the
resulting string.
"""

def fake_bin(x):
    temp = list(x)
    endString = ''
    for t in temp:
        if int(t) < 5: endString += '0'
        else: endString += '1'
    return endString

print("Tests:")
print(fake_bin("45385593107843568"))
print(fake_bin("509321967506747"))
print(fake_bin("366058562030849490134388085"))
print(fake_bin("15889923"))
print(fake_bin("800857237867"))