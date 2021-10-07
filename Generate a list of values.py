"""
GENERATATE A LIST OF VALUES
Generate decimal values with a 0.5 interval between given numbers
"""

def generateFloat(start, stop, step):
    result = []
    for i in range(int(start), int(stop)+1):
        result.append(float(i))
        i += step
        result.append(i)
    if int(stop) % 2 == 0:
        result.pop()
    return result

print(generateFloat(2, 5.5, 0.5))
print(generateFloat(3, 8, 0.5))
print(generateFloat(6, 50, 0.5))