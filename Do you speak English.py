"""
Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".

The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.

Upper or lower case letter does not matter -- "eNglisH" is also correct.

Return value as boolean values, true for the string to contains "English", false for it does not.
"""

def sp_eng(sentence): 
    return 'english' in sentence.lower()

print("Tests:")
print(sp_eng("english"))
print(sp_eng("egnlish"))
print(sp_eng("1234egn lis;h"))
print(sp_eng("1234english ;k"))
print(sp_eng("English"))
print(sp_eng("eNgliSh"))
print(sp_eng("1234#$%%eNglish ;k9"))
print(sp_eng("EGNlihs"))
print(sp_eng("1234englihs**"))