"""
Task.
Calculate area of given triangle. Create a function t_area that will take a string which will represent triangle, find area of the triangle, one space will be equal to one length unit. The smallest triangle will have one length unit.

Hints
Ignore dots.

Example:
.
.      .  
.      .       .      ---> should return 2.0

.
.      .  
.      .       .     
.      .       .      .      ---> should return 4.5
"""

def t_area(t_str):
    return 0.5 * (t_str.count('\n')-2) ** 2

print("Tests:")
print(t_area('\n.\n. .\n. . .\n. . . .\n. . . . .\n'))
print(t_area('\n.\n. .\n. . .\n'))
print(t_area('\n.\n. .\n. . .\n. . . .\n. . . . .\n. . . . . .\n. . . . . . .\n. . . . . . . .\n. . . . . . . . .\n'))
print(t_area('\n.\n. .\n'))