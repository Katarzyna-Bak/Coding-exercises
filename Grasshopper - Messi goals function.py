"""
Messi goals function
Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of
goals in all three leagues.

Note: the input will always be valid.

For example:
5, 10, 2  -->  17
"""

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

print('Tests:')
print(goals(0, 0, 0))
print(goals(5, 10, 2))