"""
There are 32 letters in the Polish alphabet: 9 vowels
and 23 consonants.

Your task is to change the letters with diacritics:
ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z

and print out the string without the use of the Polish
letters.

For example:
"Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"
"""

def correct_polish_letters(st):
    letters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
               'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    st = list(st)
    result = ''
    for r in range(len(st)):
        if st[r] in letters:
            result += letters[st[r]]
        else:
            result += st[r]
    return result

print('Tests:')
print(correct_polish_letters("Jędrzej Błądziński"))
print(correct_polish_letters("Lech Wałęsa"))
print(correct_polish_letters("Maria Skłodowska-Curie"))