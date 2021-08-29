"""
Grade book
Complete the function so that it finds the average of the
three scores passed to it and returns the letter value
associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no
need to check for negative values or values greater than 100.
"""

def get_grade(s1, s2, s3):
    if (s1 + s2 + s3)/3 >= 90: return 'A'
    elif (s1 + s2 + s3)/3 >= 80: return 'B'
    elif (s1 + s2 + s3)/3 >= 70: return 'C'
    elif (s1 + s2 + s3)/3 >= 60: return 'D'
    else: return 'F'

print('Tests:')
print(get_grade(95, 90, 93))
print(get_grade(70, 70, 100))
print(get_grade(84, 79, 85))
print(get_grade(92, 93, 94))
print(get_grade(70, 70, 70))
print(get_grade(100, 100, 100))
print(get_grade(100, 85, 96))
print(get_grade(82, 85, 87))
print(get_grade(65, 70, 59))
print(get_grade(58, 59, 60))
print(get_grade(44, 55, 52))
print(get_grade(75, 70, 79))
print(get_grade(66, 62, 68))