"""
Your friend has been out shopping for puppies (what a time
to be alive!)... He arrives back with multiple dogs, and you
simply do not know how to respond!

By repairing the function provided, you will find out exactly
how you should respond, depending on the number of dogs he has.

The number of dogs will always be a number and there will
always be at least 1 dog.

Good luck!
"""

def how_many_dalmatians(number):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return dogs[0] if number <= 10 else dogs[1] if number <= 50 else dogs[3] if number == 101 else dogs[2]

print("Tests:")
print(how_many_dalmatians(26))
print(how_many_dalmatians(8))
print(how_many_dalmatians(14))
print(how_many_dalmatians(80))
print(how_many_dalmatians(100))
print(how_many_dalmatians(50))
print(how_many_dalmatians(10))
print(how_many_dalmatians(101))