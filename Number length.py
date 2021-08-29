# You have a positive integer. Try to find out how many
# digits it has?

# Input: A positive Int
# Output: An Int.
# Example:
# number_length(10) == 2
# number_length(0) == 1

def number_length(a: int) -> int:
    b = int(len(str(a)))
    return b

print("Tests:")
print(number_length(10))
print(number_length(0))
print(number_length(4))
print(number_length(44))