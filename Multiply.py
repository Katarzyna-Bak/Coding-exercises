# Write a function that will receive 2 numbers as input and it
# should return the multiplication of these 2 numbers.

# Input: Two arguments. Both are int
# Output: Int.
# Example:
# mult_two(2, 3) == 6
# mult_two(1, 0) == 0

#%% - my idea
def mult_two(val1, val2):
    result = val1 * val2
    print('The result is: {}'.format(result))

val1 = int(input('Add the first number: '))
val2 = int(input('Add the second number: '))
mult_two(val1, val2)

#%% - actual solution
def mult_two(a: int, b: int) -> int:
    return a*b

a = int(input('Add the first number: '))
b = int(input('Add the second number: '))

c = mult_two(a, b)
print(c)