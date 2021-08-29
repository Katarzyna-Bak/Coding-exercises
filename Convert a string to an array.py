"""
Write a function to split a string and convert it into
an array of words. For example:

"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love",
"arrays", "they", "are", "my", "favorite"]
"""

def string_to_array(s):
    return s.split() if len(s) > 0 else ['']

print("Tests:")
print(string_to_array("Robin Singh"))
print(string_to_array("CodeWars"))
print(string_to_array("I love arrays they are my favorite"))
print(string_to_array("1 2 3"))
print(string_to_array(""))