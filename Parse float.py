"""
Write function parse_float which takes a string/list
and returns a number or 'none' if conversion is not possible.
"""

def parse_float(string):
    try:
        return float(string)
    except:
        return None

print("Tests:")
print(parse_float("1.0"))
print(parse_float("a"))
print(parse_float("234.0234"))