from geometrie import *
from random import randint

"""
Vecteurs:
    -à partir de:
        -2 points
        -equation cartésienne d'un plan
        -equation paramétrique d'une droite

Equation paramétrique d'un droite:
    -à partir de:
        -vecteur (et/ou combinaisons) + point
        -2 points (ou plus)

Equation cartésienne d'un plan:
    -à partir de:
        -2 vecteurs (ou plus) + point
        -3 points (ou plus)
        -2 droites sécantes (ou plus)
        -droite (ou plus) + point (ou plus)

Points:
    -à partir de:
        -vecteur (et/ou combinaisons) + point
        -droite
        -2 droties sécantes
        -plan
        -plan secant à une droite
        -projeté orthogonal
"""
"""
    A = Point()
    B = Point(1)
    C = Point(0, 1)
    AB = Vecteur(A, B)
    print(AB)
    AC = Vecteur(A, C)
    print(AC)
    p = Plan(A, B, C)
    print(p)
    print("A:", p.appartient(A))
    print("B:", p.appartient(B))
    print("C:", p.appartient(C))
    p2 = Plan("0.0*x + 0.0*y + 2.0*z + 0 = 0")
    print(p2)
    print("p = p2:", p == p2)
    print("p // p2:", p // p2)
    d = Droite(A, AB)
    print("d € p:", p.appartient(d))
    print("d € p2:", p2.appartient(d))
    print("p inter p2: \n", p.secant(p2))
    p3 = Plan("3/4*x + 2.5*y + 1/3 = 0")
    print("p inter p3: \n", p.secant(p3))
    print("d inter p3:", p3.secant(d))
"""

def enonce(depart, arrive, seed: list = [randint(0, 9), randint(0, 9), randint(1, 9)]):
    """
    Prend un objet de la géométrie de l'espace de départ et un autre à obtenir. Prend aussi Une graine (généré aléatoirement si vide)
    Retourne une chaîne de caractères correspondant à un énoncé de mathématiques
    
    :param depart: Objet de départ
    :param arrive: Objet d'arrivé
    :param seed: Graine (si identique, produira le même énonce)
    :type seed: liste de nombre
    :return: Une chaine de caractères.
    """
    if depart == arrive or (depart in ("Plan", "Droite") and arrive == "Vecteur"):
        return None
    long = 0
    if depart == "Plan":
        long += 4
        if arrive == "Point":
            long += 2
        elif arrive == "Droite":
            long += 5
    elif depart == "Droite":
        long += 6
        if arrive == "Point":
            long += 1
        elif arrive == "Plan":
            long += 4
    elif depart in ("Vecteur", "Point"):
        long += 3
        if arrive == "Point":
            long += 3
        elif arrive == "Vecteur":
            long += 3
        elif arrive == "Droite":
            long += 3
        elif arrive == "Plan":
            long += 6
    if len(seed) < long:
        if len(seed) < 3:
            while len(seed) < 3:
                seed += randint(1, 9)
        while len(seed) < long:
            temp = str(int(seed[-1] + seed[-2]))
            value = 0
            for i in temp:
                value += int(i)
            seed += [value]
    print(f"Creation d'un énoncé à partir de {depart} pour obtenir {arrive} avec la graine: {str(seed)}.")
    if depart == "Plan":
        P = Plan(*seed[:4])
        if arrive in ("Point", "Droite"):
            po1 = Point(seed[4], seed[5])
            po1.z = -(P[0] * po1[0] + P[1] * po1[1] + P[3]) / (P[2] if P[2] != 0 else 1)
            if P.appartient(po1):
                if arrive == "Droite":
                    po2 = Point(*seed[6:])
                    n = Vecteur(po1, po2)
                    d = Droite(po1, n)
                    return f"Soient un plan P admettant une équation cartésienne tel que {str(P)}, un point A{po1} appartennant à P et un point B{po2}.\nDéterminer une équation parmétrique de la droite D passant par les points A et B.\n\nSolution: d:\n{d}."
            else:
                return f"Soit un plan P admettant une équation cartésienne tel que {str(P)}.\nDéterminer z tel que A({po1[0]};{po1[1]};z) appartienne au plan P.\n\nSolution: z={po1[2] if P[2] != 0 else 'R'}."
        raise ValueError("Une erreur est survenue lors de la création de l'énoncé avec cette seed")
    if depart == "Droite":
        po1 = Point(*seed[:3])
        n = Vecteur(*seed[3:6])
        d = Droite(po1, n)
        if arrive in ("Point", "Plan"):
            po2 = d.image(seed[6])
            if arrive == "Plan":
                po3 = Point(*seed[7:])
                P = Plan(po1, po2, po3)
                if P.appartient(po1) and P.appartient(po2) and P.appartient(po3):
                    return f"Soit une droite D admettant une équation paramétrique tel que:\n{d}\nSoient un point A{po1}, un point B appartennant à la droite D avec t={seed[6]} et C{po3}.\nDéterminer un plan P qui contient la droite D et le point C.\n\nSolution: {P}."
            else:
                return f"Soit une droite D admettant une équation paramétrique tel que:\n{d}\nDéterminer un point A appartennant à la droite D avec t={seed[6]}."
        raise ValueError("Une erreur est survenue lors de la création de l'énoncé avec cette seed")
    if depart == "Vecteur":
        n = Vecteur(*seed[:3])
        po1 = Point(*seed[3:6])
        if arrive == "Droite":
            d = Droite(po1, n)
            return f"Soit un point A{po1} et un vecteur n{n}.\nDéterminer une équation paramétrique de la droite d ayant pour vecteur directeur n et passant par A.\n\nSolution: d:\n{d}"
        if arrive == "Plan":
            n2 = Vecteur(*seed[6:])
            P = Plan(po1, n, n2)
            checks = [n.image(po1), n2.image(po1)]
            if P.appartient(po1) and P.appartient(checks[0]) and P.appartient(checks[1]):
                return f"Soit un point A{po1} et deux vecteurs n{n} et n2{n2}.\nDéterminer une équation cartésienne du plan P définie par A, n et n2.\n\nSolution: {P}."
        raise ValueError("Une erreur est survenue lors de la création de l'énoncé avec cette seed")
    if depart == "Point":
        po1 = Point(*seed[:3])
        po2 = Point(*seed[3:6])
        if arrive == "Vecteur":
            n = Vecteur(po1, po2)
            return f"Soit deux point A{po1} et B{po2}.\nDéterminer le vecteur AB{n}.\n\nSolution: AB{n}."
        if arrive == "Droite":
            n = Vecteur(po1, po2)
            d = Droite(po1, n)
            return f"Soit deux point A{po1} et B{po2}.\nDéterminer une équation paramétrique de la droite d passant par A et B.\n\nSolution: d:\n{d}"
        if arrive == "Plan":
            po3 = Point(*seed[6:9])
            P = Plan(po1, po2, po3)
            return f"Soit trois point A{po1}, B{po2} et C{po3}.\nDéterminer une équation cartésienne du plan P définie par A, B et C\n\nSolution: {P}"
        raise ValueError("Une erreur est survenue lors de la création de l'énoncé avec cette seed")
    return None

print(enonce("Point", "Plan"))