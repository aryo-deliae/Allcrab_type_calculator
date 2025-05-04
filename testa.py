
from Utils import test_faiblesse_double, test_faiblesse, Equivalence
from Utils import test_resistance,test_resistance_double, test_immunité

Equi = [
    {"num" : 1, "nom" : "humain"},
    {"num" : 2, "nom" : "bestial"},
    {"num" : 3, "nom" : "insect"},
    {"num" : 4, "nom" : "plante"},
    {"num" : 5, "nom" : "dragon"},
    {"num" : 6, "nom" : "sacré"},
    {"num" : 7, "nom" : "tenebre"},
    {"num" : 8, "nom" : "magie"},
    {"num" : 9, "nom" : "poison"},
    {"num" : 10, "nom" : "mort"},
    {"num" : 11, "nom" : "feu"},
    {"num" : 12, "nom" : "eau"},
    {"num" : 13, "nom" : "air"},
    {"num" : 14, "nom" : "glace"},
    {"num" : 15, "nom" : "foudre"},
    {"num" : 16, "nom" : "roche"},
    {"num" : 17, "nom" : "terre"}, 
    {"num" : 18, "nom" : "metal"}
]

aga = [201, 206, 207, 213, 217, 314, 315, 410]

ligne1 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"] 
ligne2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"] 
ligne3 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"] 
ligne4 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"] 
ligne5 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"] 

num = 0 
for i in aga :
    if test_faiblesse(i) is not None :
        ligne1[num] = test_faiblesse(i)
        num += 1

num = 0 
for i in aga :
    if test_faiblesse_double(i) is not None :
        ligne2[num] = test_faiblesse_double(i)
        num += 1

num = 0 
for i in aga :
    if test_resistance(i) is not None :
        ligne3[num] = test_resistance(i)
        num += 1  

num = 0 
for i in aga :
    if test_resistance_double(i) is not None :
        ligne4[num] = test_resistance_double(i)
        num += 1

num = 0 
for i in aga :
    if test_immunité(i) is not None :
        ligne5[num] = test_immunité(i)
        num += 1


print(ligne1)
print(ligne2)
print(ligne3)
print(ligne4)
print(ligne5)

