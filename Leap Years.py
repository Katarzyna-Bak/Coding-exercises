"""
In this kata you should simply determine, whether a given year is a leap year or not.
In case you don't know the rules, here they are:

years divisible by 4 are leap years
but years divisible by 100 are not leap years
but years divisible by 400 are leap years
Additional Notes:

Only valid years (positive integers) will be tested, so you don't have
to validate them.

Examples can be found in the test fixture.
"""

def isLeapYear(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

print("Tests:")
print(isLeapYear(1984))
print(isLeapYear(2000))
print(isLeapYear(1234))
print(isLeapYear(1100))
print(isLeapYear(1987))