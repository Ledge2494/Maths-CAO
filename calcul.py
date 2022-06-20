from arbre import arbre

def sub_calcul(expr):
    if expr.find("(") != -1:
        parenth = expr.index("(")
        temp = expr[parenth:]
        bord = 0
        i = 0
        while i < len(temp):
            if temp[i] == "(":
                bord +=1
            elif temp[i] == ")":
                bord -= 1
                if bord == 0:
                    edit = calcul(temp[1:i])
                    expr = expr[:parenth] + str(edit) + expr[parenth+i+1:]
                    if expr.find("(") != -1:
                        i = -1
                        parenth = expr.index("(")
                        temp = expr[parenth:]
            i += 1
    if expr.find("+") != -1:
        ind = expr.index("+")
        if ind == 0:
            return arbre("+", sub_calcul("0"), sub_calcul(expr[ind+1:]))
        return arbre("+", sub_calcul(expr[0:ind]), sub_calcul(expr[ind+1:]))
    if expr.find("-") != -1:
        ind = expr.index("-")
        while True:
            if ind == 0:
                return arbre("-", sub_calcul("0"), sub_calcul(expr[ind+1:]))
            if expr[ind-1] != "*":
                return arbre("-", sub_calcul(expr[:ind]), sub_calcul(expr[ind+1:]))
            if expr[ind+1:].find("-") != -1:
                ind = ind + 1 + expr[ind+1:].index("-")
            else:
                break
    if expr.find("*") != -1:
        ind = expr.index("*")
        return arbre("*", sub_calcul(expr[0:ind]), sub_calcul(expr[ind+1:]))
    if expr.find("/") != -1:
        ind = expr.index("/")
        return arbre("/", sub_calcul(expr[0:ind]), sub_calcul(expr[ind+1:]))
    return arbre(expr)

def calcul(expr):
    if isinstance(expr, str):
        expr = sub_calcul(expr)
    if isinstance(expr.noeud, str):
        if expr.noeud == "+":
            return calcul(expr.fg) + calcul(expr.fd)
        if expr.noeud == "-":
            return calcul(expr.fg) - calcul(expr.fd)
        if expr.noeud == "*":
            return calcul(expr.fg) * calcul(expr.fd)
        if expr.noeud == "/":
            return calcul(expr.fg) / calcul(expr.fd)
    return float(expr.noeud)
    

if __name__ == "__main__":
    tests = [
        "1+2",
        "2*3",
        "1+2*3",
        "2*-1",
        "-1*2",
        "-1*-2",
        "2*-1+1",
        "2*-1-5",
        "1+2*-1",
        "(1+2)*3",
        "2*(4+2)+1",
        "2*(1+2)*(3+4)",
        "2*(4-(2+3))+1",
        "(((15.3+4))*3-(2-6)*4+7*4)/2"
    ]
    for i in tests:
        print(i,"=",calcul(i))