"""
Complete the function that receives as input a string,
and produces outputs according to the following table:

Input	Output
"Jabroni"	"Patron Tequila"
"School Counselor"	"Anything with Alcohol"
"Programmer"	"Hipster Craft Beer"
"Bike Gang Member"	"Moonshine"
"Politician"	"Your tax dollars"
"Rapper"	"Cristal"
anything else	"Beer"
Note: anything else is the default case: if the input
to the function is not any of the values in the table,
then the return value should be "Beer".

Make sure you cover the cases where certain words do
not show up with correct capitalization. For example,
the input "pOLitiCIaN" should still return "Your tax dollars".
"""

def get_drink_by_profession(param):
    drinks = {"jabroni": "Patron Tequila",
              "school counselor": "Anything with Alcohol",
              "programmer": "Hipster Craft Beer",
              "bike gang member": "Moonshine",
              "politician": "Your tax dollars",
              "rapper": "Cristal"}
    if param.lower() in drinks.keys(): return drinks[param.lower()]
    else: return "Beer"

print('Tests:')
print(get_drink_by_profession("jabrOni"))
print(get_drink_by_profession("scHOOl counselor"))
print(get_drink_by_profession("prOgramMer"))
print(get_drink_by_profession("bike ganG member"))
print(get_drink_by_profession("poLiTiCian"))
print(get_drink_by_profession("rapper"))
print(get_drink_by_profession("pundit"))
print(get_drink_by_profession("Pug"))