# You are at the beginning of a password series. Every mission
# is based on the previous one. Going forward the missions will
# become slightly more complex.
# In this mission, you need to create a password verification
# function.
# The verification condition is:
# the length should be bigger than 6.

# Input: A string.
# Output: A bool.
# Example:
# is_acceptable_password('short') == False
# is_acceptable_password('muchlonger') == True

def is_acceptable_password(password: str) -> bool:
    if len(password) <= 6:
        booleanValue = False
    else:
        booleanValue = True
    return booleanValue

print("Tests:")
print(is_acceptable_password('short'))
print(is_acceptable_password('muchlonger'))
print(is_acceptable_password('ashort'))