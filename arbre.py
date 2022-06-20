class arbre:
    def __init__(self,nom,fg=None,fd=None):
        self.noeud = nom
        self.fg = fg
        self.fd = fd        

    def __eq__(self,other):
        if not isinstance(other, arbre):
            return None
        if self.noeud != other.noeud:
            return False
        if self.fg is not None and self.fd is not None:
            return self.fg.__eq__(other.fg) or self.fd.__eq__(other.fd)
        if self.fg is not None and other.fg is not None:
            return self.fg.__eq__(other.fg)
        if self.fd is not None and other.fd is not None:
            return self.fd.__eq__(other.fd)
        return True

    def tableau(self):
        if self.fg is not None and self.fd is not None:
            return [[self.fg.tableau()], [self.noeud],[self.fd.tableau()]]
        if self.fg is not None:
            return [[self.fg.tableau()], [self.noeud]]
        if self.fd is not None:
            return [[self.noeud], [self.fd.tableau()]]
        return self.noeud

    def is_paper(self):
        return self.fg is None and self.fd is None

    def hauteur(self):
        if self.fg is not None and self.fd is not None:
            g = 1+self.fg.hauteur()
            d = 1+self.fd.hauteur()
            if g > d:
                return g
            return d
        elif self.fg is not None:
            return 1 + self.fg.hauteur()
        elif self.fd is not None:
            return 1 + self.fd.hauteur()
        return 1

    def taille(self):
        if self.fg is not None and self.fd is not None:
            g = 1+self.fg.taille()
            d = 1+self.fd.taille()
            return d+g-1
        elif self.fg is not None:
            return 1 + self.fg.taille()
        elif self.fd is not None:
            return 1 + self.fd.taille()
        return 1

    def largeur(self):
        long_g = 1
        long_d = 0
        if self.fg is not None:
            long_g = self.fg.sub_largeur("g")
        if self.fd is not None:
            long_d = self.fd.sub_largeur("d")
        return long_g + long_d

    def sub_largeur(self, side):
        if side == "g":
            if self.fg is not None and self.fd is not None:
                g = self.fg.largeur() + 1
                d = self.fd.largeur() - 1
                if g > d:
                    return g
                return d
            elif self.fg is not None:
                return self.fg.largeur() + 1
            elif self.fd is not None:
                return self.fd.largeur() - 1
            return 1
        if side == "d":
            if self.fg is not None and self.fd is not None:
                g = self.fg.largeur() - 1
                d = self.fd.largeur() + 1
                if g > d:
                    return g
                return d
            elif self.fg is not None:
                return self.fg.largeur() - 1
            elif self.fd is not None:
                return self.fd.largeur() + 1
            return 1

    def recherche(self, elt):
        if self.noeud == elt:
            return True
        elif self.fg is not None and self.fd is not None:
            return self.fg.recherche(elt) or self.fd.recherche(elt)
        elif self.fg is not None:
            return self.fg.recherche(elt)
        elif self.fd is not None:
            return self.fd.recherche(elt)
        return False

if __name__ == "__main__":
    a = arbre(1,arbre(2,arbre(4,None,arbre(3))))
    c = arbre("+",arbre("2"),arbre("*",arbre("3"),arbre("-",arbre("7"),arbre("4"))))
    b = arbre("+",arbre("2"),arbre("*",arbre("3"),arbre("-",arbre("7"),arbre("4"))))
    print("hauteur de a:", a.hauteur())
    print("hauteur de b:", b.hauteur())
    print("taille de a:", a.taille())
    print("taille de b:", b.taille())
    print("largeur de a:", a.largeur())
    print("largeur de b:", b.largeur())
    print("1 est-il dans a:", a.recherche(1))
    print("5 est-il dans a:", a.recherche(5))
    print('"1" est-il dans a:', b.recherche("3"))
    print("3 est-il dans a:", b.recherche(3))
    print(a==b)
    print(b==c)
    print("tableau de a:", a.tableau())
    print("tableau de b:", b.tableau())