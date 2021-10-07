"""
FIND MISSING VALUES
You get a list of values from 1 to n. Write a function
that will check which elements are missing
1-n = [1,2,3,4,5,...,10]

e.g. n=10
input: [2,3,7,4,9], 10
output: [1,5,6,8,10]
"""

def checkValues(initialList, n):
    result = []
    for i in range(1, n+1):
        if i not in initialList:
            result.append(i)
    return result

print(checkValues([2,3,7,4,9], 10))