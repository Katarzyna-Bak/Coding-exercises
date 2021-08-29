"""
Write a function that returns the total surface area and
volume of a box as an array: [area, volume]
"""

def get_size(w,h,d):
    return [2*(w*h+w*d+h*d), w*h*d]

print('Tests:')
print(get_size(4, 2, 6))
print(get_size(1, 1, 1))
print(get_size(1, 2, 1))
print(get_size(1, 2, 2))
print(get_size(10, 10, 10))