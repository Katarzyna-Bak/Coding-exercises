"""
Given the molecular mass of two molecules M1 and M2, their
masses present m1 and m2 in a vessel of volume VVV at
a specific temperature T, find the total pressure Ptotal
exerted by the molecules. 
"""

def solution(M1, M2, m1, m2, V, T) :
    return ((m1/M1 + m2/M2) * (T + 273.15) * 0.082) / V

print("Tests:")
print(solution(44, 30, 3, 2, 5, 50))
print(solution(60, 20, 10, 30, 10, 100))