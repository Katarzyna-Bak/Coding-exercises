"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"
"""

def bmi(weight, height):
    bmiMetric = weight / (height ** 2)
    if bmiMetric <= 18.5:
        return 'Underweight'
    elif bmiMetric <=25.0:
        return 'Normal'
    elif bmiMetric <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'

print("Tests:")
print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(90, 1.80))
print(bmi(110, 1.80))
print(bmi(50, 1.50))
print(bmi(96, 1.54))