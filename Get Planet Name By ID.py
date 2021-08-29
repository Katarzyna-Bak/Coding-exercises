"""
The function is not returning the correct values.
Can you figure out why?

Example (Input --> Output ):
3 --> "Earth"
"""

def get_planet_name(id):
    switch = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
        }
    return switch.get(id, 'Invalid id)')

print('Tests:')
print(get_planet_name(2))
print(get_planet_name(5))
print(get_planet_name(3))
print(get_planet_name(4))
print(get_planet_name(8))
print(get_planet_name(1))