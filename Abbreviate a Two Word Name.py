"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:
Sam Harris => S.H
Patrick Feeney => P.F
"""

def abbrev_name(name):
    return '{}.{}'.format(name[0].upper(), name[name.find(' ')+1].upper())

print("Tests:")
print(abbrev_name("Sam Harris"))
print(abbrev_name("Patrick Feenan"))
print(abbrev_name("Evan Cole"))
print(abbrev_name("P Favuzzi"))
print(abbrev_name("David Mendieta"))