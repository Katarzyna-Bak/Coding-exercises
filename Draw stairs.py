"""
Given a number n, draw stairs using the letter "I",
n tall and n wide, with the tallest in the top left.

For example n = 3 result in:

"I\n I\n  I"
or printed:

I
 I
  I
Another example, a 7-step stairs should be drawn like this:

I
 I
  I
   I
    I
     I
      I
"""

def draw_stairs(number):
    result = ''
    for n in range(number):
        if n < number - 1:
            result += ' ' * n + 'I\n'
        else:
            result += ' ' * n + 'I'
    return result

print('Tests:')
print(draw_stairs(3))
print(draw_stairs(30))