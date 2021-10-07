"""
POST CODES GENERATOR
The function should take 2 strings: "79-900" and "80-155"
and return a list of codes between them
"""
def postCodes(str1, str2):
    result = []
    for i in range(int(str1[:2]+str1[3:])+1, int(str2[:2]+str2[3:])):
        i = str(i)
        result.append(f'{i[0:2]}-{i[2:]}')
    return result

def postCodes2(str1, str2):
    result = []
    start = int(str1.replace('-', ''))+1
    end = int(str2.replace('-', ''))
    for i in range(start, end):
        i = str(i)
        result.append(f'{i[0:2]}-{i[2:]}')
    return result

print(postCodes('79-900', '80-155'))
print(postCodes2('79-900', '80-155'))