"""
Bob needs a fast way to calculate the volume of a cuboid
with three values: length, width and the height of the
cuboid. Write a function to help Bob with this calculation.
"""

def getVolumeOfCubiod(length, width, height):
    return length * width * height

print('Tests:')
print(getVolumeOfCubiod(1, 2, 2))
print(getVolumeOfCubiod(6.3, 2, 5))