
Equivalence_numero = [
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


def test_faiblesse(test):
    for i in Equivalence_numero :
        if i["num"] == test-300 :
            resultat = i["nom"]
            return resultat

def test_faiblesse_double(test):
    for i in Equivalence_numero :
        if i["num"] == test-400 :
            resultat = i["nom"]
            return resultat

def test_resistance(test):
    for i in Equivalence_numero :
        if i["num"] == test-200 :
            resultat = i["nom"]
            return resultat


def test_resistance_double(test):
    for i in Equivalence_numero :
        if i["num"] == test-100 :
            resultat = i["nom"]
            return resultat

def test_immunité(test):
    for i in Equivalence_numero :
        if i["num"] == test-500 :
            resultat = i["nom"]
            return resultat 
        
class Equivalence :
        
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
