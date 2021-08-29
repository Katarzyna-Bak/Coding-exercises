"""
Simple challenge - eliminate all bugs from the supplied code
so that the code runs and outputs the expected value. Output
should be the length of the longest word, as a number.

There will only be one 'longest' word.
"""

def find_longest(string):
    return len(max(string.split(), key=len))

print("Tests:")
print(find_longest("The quick white fox jumped around the massive dog"))
print(find_longest("Take me to tinseltown with you"))
print(find_longest("Sausage chops"))
print(find_longest("Wind your body and wiggle your belly"))
print(find_longest("Lets all go on holiday"))