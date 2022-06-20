from calcul import calcul

class Point:
    """
    Une classe qui représente un point dans l'espace
    Possède 3 attributs: x, y et z. Accessible via index ou nom d'attributs (Point.x; Point[0]; Point[-2])
    
    Construction possible:
        -Point(1, 1)
    
    Méthodes magiques présentes:
        -getitem
        -str
        -eq
    """
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, indice: int):
        if indice in (0, -3):
            return self.x
        if indice in (1, -2):
            return self.y
        if indice in (2, -1):
            return self.z
        raise IndexError("Index out of range")

    def __str__(self):
        """
        Renvoie le point sous forme de la chaine: (Point.x; Point.y; Point.z)
        """
        return "(" + str(self.x) + "; " +\
                    str(self.y) + "; " +\
                    str(self.z) + ")"

    def __eq__(self, other):
        return abs(self.x - other.x) < 10**-4 and\
                abs(self.y - other.y) < 10**-4 and\
                abs(self.z - other.z) < 10**-4

class Vecteur:
    """
    Une classe qui un vecteur dans l'espace
    Possède 3 attributs: x, y et z. Accessible via index ou nom d'attributs (Vecteur.x; Vecteur[0]; Vecteur[-2])
    2 autres attributs: origin et final sont présents si le vecteur est construit à partir de 2 points
    
    Constructions possibles:
        -Vecteur(1, 0, 1)
        -Vecteur(Point, Point)
    
    Méthodes magiques présentes:
        -getitem
        -str
        -eq
        -add
        -mult (ne fonctionne qui si appelé explicitement)
        -truediv (ne fonctionne qui si appelé explicitement)
        -floordiv
    
    Méthodes présentes:
        -image
        -scalaire
        -collinéaire
    """
    def __init__(self, x = 0.0, y = 0.0, z: float = 0.0):
        if isinstance(x, Point) and isinstance(y, Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
            self.z = y.z - x.z
            self.origin = x
            self.final = y
        else:
            self.x = float(x)
            self.y = float(y)
            self.z = z
            self.origin = None
            self.final = None

    def __getitem__(self, indice: int):
        if indice in (0, -3):
            return self.x
        if indice in (1, -2):
            return self.y
        if indice in (2, -1):
            return self.z
        raise IndexError("Index out of range")

    def __str__(self):
        """
        Renvoie le vecteur sous forme de la chaine: (Vecteur.x; Vecteur.y; Vecteur.z)
        """
        return "(" + str(self.x) + "; " +\
                    str(self.y) + "; " +\
                    str(self.z) + ")"

    def __eq__(self, other):
        return abs(self.x - other.x) < 10**-4 and\
                abs(self.y - other.y) < 10**-4 and\
                abs(self.z - other.z) < 10**-4

    def __add__(self, other):
        return Vecteur(self.x + other.x,
                       self.y + other.y,
                       self.z + other.z)
    
    def __mult__(self, other: float):
        """
        Multiplie le vecteur par un coefficient
        
        :param other: flottant
        """
        return Vecteur(self.x * other,
                        self.y * other,
                        self.z * other)

    def __truediv__(self, other: float):
        """
        Divise le vecteur par un coefficient
        
        :param other: flottant
        """
        return Vecteur(self.x / other,
                       self.y / other,
                       self.z / other)

    def __floordiv__(self, other):
        """
        Vérifie si 2 vecteurs sont collineaires
        
        :param other: Vecteur
        """
        t1 = self.x / other.x if other.x != 0 else None
        t2 = self.y / other.y if other.y != 0 else None
        t3 = self.z / other.z if other.z != 0 else None
        return t1 is not None and\
                t2 is not None and\
                t3 is not None and\
                abs(t1 - t2) < 10**-4 and\
                abs(t1 - t3) < 10**-4

    def image(self, point: Point):
        """
        Crée l'image d'un point par le vecteur
        
        :param other: Point
        """
        return Point(self.x + point.x,
                     self.y + point.y,
                     self.z + point.z)

    def scalaire(self, other):
        """
        Calcul le produit scalaire de 2 vecteurs
        
        :param other: Vecteur
        """
        return self.x * other.x +\
                self.y * other.y +\
                self.z * other.z

    def collineaire(self, other):
        """
        Vérifie si 2 vecteurs sont collineaires
        
        :param other: Vecteur
        """
        return self // other

class Droite:
    """
    Une classe qui représente une droite dans l'espace
    Possède 2 attributs: origine et vecteur. Accessible via nom d'attributs (Droite.origine)
    
    Construction possible:
        -Droite(Point, Vecteur)
    
    Méthodes magiques présentes:
        -str
        -eq
        -floordiv
    
    Méthodes présentes:
        -image
        -appartient
        -parallele
        -secant
    """
    def __init__(self, origine: Point, vecteur: Vecteur):
        self.origine = origine
        self.vecteur = vecteur

    def __eq__(self, other):
        cond1 = str(self) == str(other)
        cond2 = self.origine == other.origine
        cond3 = self.vecteur == other.vecteur
        cond4 = self.appartient(other.origine) or other.appartient(self.origine)
        cond5 = self.vecteur.collineaire(other.vecteur)
        return cond1 or ((cond2 or cond4) and (cond3 or cond5))

    def __str__(self):
        """
        Renvoie la drtoie sous forme de la chaine: 
        |x = - origine.x + vecteur.x * t
        |y = - origine.y + vecteur.y * t
        |z = - origine.z + vecteur.z * t
        """
        return f"|x = - {self.origine.x} + {self.vecteur.x} * t".replace("- -", "").replace("+ -", "-") + "\n" +\
               f"|y = - {self.origine.y} + {self.vecteur.y} * t".replace("- -", "").replace("+ -", "-") + "\n" +\
               f"|z = - {self.origine.z} + {self.vecteur.z} * t".reaplce("- -", "").replace("+ -", "-")

    def __floordiv__(self,other):
        """
        Vérifie si 2 droites sont parallèles
        
        :param other: Droite
        """
        return self.vecteur.collineaire(other.vecteur)

    def image(self, coef: float):
        """
        Crée un point de la droite à partir d'un coefficient et de l'origine
        
        :param other: floattant
        """
        return Point(self.origine.x + (coef * self.vecteur.x),
                     self.origine.y + (coef * self.vecteur.y),
                     self.origine.z + (coef * self.vecteur.z))

    def appartient(self, point: Point):
        """
        Vérifie si un point appartient à la droite
        
        :param other: Point
        """
        t1 = (point.x - self.origine.x) / self.vecteur.x
        t2 = (point.y - self.origine.y) / self.vecteur.y
        t3 = (point.z - self.origine.z) / self.vecteur.z
        return abs(t1 - t2) < 10**-4 and\
                abs(t1 - t3) < 10**-4

    def parallele(self, other):
        """
        Vérifie si 2 droites sont parallèles
        
        :param other: Droite
        """
        return self // other

    def secant(self, other):
        """
        Vérifie si 2 droties sont sécantes
        Renvie le point d'intersection si c'est le cas
        
        :param other: Droite
        """
        cond1 = self // other
        cond2 = (self.origine[0] + self.vecteur[0] - other.origine[0]) / other.vecteur[0]
        cond3 = (self.origine[1] + self.vecteur[1] - other.origine[1]) / other.vecteur[1]
        cond4 = (self.origine[2] + self.vecteur[2] - other.origine[2]) / other.vecteur[2]
        if not cond1 and\
        abs(cond2 - cond3) < 10**-4 and\
        abs(cond2 - cond4) < 10**-4:
            ret = Point()
            ret.x = ((self.origine[0] + self.vecteur[0]) ** 2) / (other[0] + (cond2 * other.vecteur[0]))
            ret.y = ((self.origine[1] + self.vecteur[1]) ** 2) / (other[1] + (cond3 * other.vecteur[1]))
            ret.z = ((self.origine[2] + self.vecteur[2]) ** 2) / (other[2] + (cond4 * other.vecteur[2]))
            return ret

class Plan:
    """
    Une classe qui représente un plan dans l'espace
    Possède 4 attributs: a, b, c et d (ax + by +cz + d = 0). Accessible via index ou nom d'attributs (Plan.a; Plan[0], Plan[-4])
    
    Constructions possibles:
        -Plan(2, 7, 6, -9)
        -Plan(Point, Vecteur, Vecteur)
        -Plan(Point, Point, Point)
        -Plan("3/4x - 0.66y + 8z - 5.5 = 0")
    
    Méthodes magiques présentes:
        -getitem
        -str
        -eq
        -floordiv
    
    Méthodes présentes:
        -appartient
        -parallele
        -secant
    """
    def __init__(self, *args):
        self.a = 0
        self.b = 0
        self.c = 0
        if len(args) == 4:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
            self.d = args[3]
        if len(args) == 3 and\
        isinstance(args[0], Point) and\
        isinstance(args[1], Vecteur) and isinstance(args[2], Vecteur):
            temp_vec = normal(args[1], args[2])
            d = - (args[0][0] * temp_vec[0] + args[0][1] * temp_vec[1] + args[0][2] * temp_vec[2])
            self.a = temp_vec[0]
            self.b = temp_vec[1]
            self.c = temp_vec[2]
            self.d = d
        if len(args) == 3 and\
        isinstance(args[0], Point) and\
        isinstance(args[1], Point) and\
        isinstance(args[2], Point):
            v1 = Vecteur(args[0], args[1])
            v2 = Vecteur(args[0], args[2])
            temp_vec = normal(v1, v2)
            d = - (args[0][0] * temp_vec[0] + args[0][1] * temp_vec[1] + args[0][2] * temp_vec[2])
            self.a = temp_vec[0]
            self.b = temp_vec[1]
            self.c = temp_vec[2]
            self.d = d
        if len(args) == 1 and\
        isinstance(args[0], str):
            tab = args[0].split(" + ")
            if len(tab) > 4:
                raise SyntaxError("La chaine ne respecte pas le format d'écriture supporté")
            for i in tab:
                if "x" in i:
                    self.a = calcul(i.replace("x", "1"))
                if "y" in i:
                    self.b = calcul(i.replace("y", "1"))
                if "z" in i:
                    self.c = calcul(i.replace("z", "1"))
                elif not "x" in i and not "y" in i and not "z" in i:
                    self.d = calcul(i[:-4])

    def __str__(self):
        """
        Renvoie le plan sous forme de la chaine: (P): Plan.a * x + Plan.b * y + Plan.c * z + Plan.d = 0
        """
        return f"(P): {self.a}*x + {self.b}*y + {self.c}*z + {self.d} = 0".replace("+ -", "-")

    def __eq__(self, other):
        cond1a = abs(self.a - other.a) < 10**-4
        cond1b = abs(self.b - other.b) < 10**-4
        cond1c = abs(self.c - other.c) < 10**-4
        cond1d = abs(self.d - other.d) < 10**-4

        cond1 = cond1a and cond1b and cond1c and cond1d

        cond2a = self.a / other.a if other.a != 0 else None
        cond2b = self.b / other.b if other.b != 0 else None
        cond2c = self.c / other.c if other.c != 0 else None
        cond2d = self.d / other.d if other.d != 0 else None
        cond2 = cond2a is not None and cond2b is not None and\
                cond2c is not None and cond2d is not None and\
                abs(cond2a - cond2b) < 10**-4 and\
                abs(cond2a - cond2c) < 10**-4 and\
                abs(cond2a - cond2d) < 10**-4

        return cond1 or cond2

    def __getitem__(self, indice: int):
        if indice in (0, -4):
            return self.a
        if indice in (1, -3):
            return self.b
        if indice in (2, -2):
            return self.c
        if indice in (3, -1):
            return self.d
        raise IndexError("Index out of range")

    def __floordiv__(self, other):
        """
        Vérifie si 2 plans sont parallèles
        
        :param other: Plan
        """
        return Vecteur(self.a, self.b, self.c) // Vecteur(other.a, other.b, other.c)

    def appartient(self, other):
        """
        Vérifie si un point appartient au plan ou si une droite est contenu dans le plan
        
        :param other: Point | Droite
        """
        if isinstance(other, Point):
            return abs(self.a * other[0] + self.b * other[1] + self.c * other[2] + self.d) < 10**-4
        if isinstance(other, Droite):
            test = other.image(1)
            return abs(self.a * other.vecteur[0] + self.b * other.vecteur[1] + self.c * other.vecteur[2] + self.d) < 10**-4 and\
                    abs(self.a * test[0] + self.b * test[1] + self.c * test[2] + self.d) < 10**-4

    def parallele(self, other):
        """
        Vérifie si 2 plans sont parallèles
        
        :param other: Plan
        """
        return self // other
    
    def secant(self, other):
        """
        Détermine la droite d'intersection entre 2 plans ou le point d'intersection entre le plan et une droite
        
        :param other: Droite | Plan
        """
        if isinstance(other, Droite):
            if self.appartient(other):
                return Droite(other.origine, other.vecteur)
            if self.a != 0:
                test = Droite(Point(-self.d), other.vecteur)
            elif self.b != 0:
                test = Droite(Point(0, -self.d), other.vecteur)
            else:
                test = Droite(Point(0, 0, -self.d), other.vecteur)
            if not self.appartient(test.image(1.0)):
                t = -(self.a * other.origine[0] + self.b * other.origine[1] + self.c * other.origine[2] + self.d)\
                / (self.a * other.vecteur[0] + self.b * other.vecteur[1] + self.c * other.vecteur[2])
                return other.image(t)
        if isinstance(other, Plan) and not self.parallele(other):
            vecteur = normal(Vecteur(self.a, self.b, self.c), Vecteur(other.a, other.b, other.c))
            t = (-self.d + other.d)\
            / (self.a * vecteur[0] + self.b * vecteur[1] + self.c * vecteur[2] -\
                (other.a * vecteur[0] + other.b * vecteur[1] + other.c * vecteur[2]))
            return Droite(vecteur.image(Point(vecteur[0] * t, vecteur[1] * t, vecteur[2] * t)), vecteur)
        return None

def normal(v1: Vecteur, v2: Vecteur):
    """
    Détermine une vecteur orthogonal à 2 autres
    
    :param v1: Vecteur
    :param v2: Vecteur
    """
    ret_vec = Vecteur(0,0,1)
    
    if ((v2[1] * v1[0]) - (v1[1] * v2[0])) != 0:
        num = (-ret_vec[2]) * (v2[2] * v1[0] - (v1[2] * v2[0]))
        denom = v2[1] * v1[0] - (v1[1] * v2[0])
        
        ret_vec.y = num / denom
    
    if v1[0] != 0:
        num = - ((ret_vec[1] * v1[1]) + (ret_vec[2] * v1[2]))
        ret_vec.x = num / v1[0]

    return ret_vec

if __name__ == "__main__":
    #Espace de test
    po1 = Point(1, 4, 6)
    n = Vecteur(1, 7, 8)
    d = Droite(po1, n)
    po2 = d.image(6)
    po3 = Point(5, 2, 7)
    P = Plan(po1, po2, po3)
    t1 = P.appartient(po1)
    t2 = P.appartient(po2)
    t3 = P.appartient(po3)
    v1 = Vecteur(po1, po2)
    v2 = Vecteur(po1, po3)
    print(po1, n, d, po2, po3, P, t1, t2, t3, v1, v2, sep="\n")
    print(P[0] * po1[0] + P[1] * po1[1] + P[2] * po1[2] + P[3])
    print(P[0] * po2[0] + P[1] * po2[1] + P[2] * po2[2] + P[3])
    print(P[0] * po3[0] + P[1] * po3[1] + P[2] * po3[2] + P[3])
    vnormal = normal(v1, v2)
    print(v1.scalaire(vnormal))
    print(v2.scalaire(vnormal))
