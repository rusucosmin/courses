from copy import deepcopy


class Poligon:
    '''
    Poligon (în planul real)
        Specificaţi şi implementaţi tipurile abstracte de date menţionate mai jos.
        La toate tipurile de date vor exista operaţii pentru:

        a) creare de valori din domeniul tipului respectiv;
        b) operaţii aritmetice
        c) comparare de valori
        d) extragere de componente
        e) eventual conversii din alte tipuri mentionate.
    '''
    def __init__(self, n, puncte):
        self.n = n
        self.puncte = puncte

    def getArea(self):
        area = 0
        aux = deepcopy(self.puncte)
        aux.append(aux[0])
        for i in range(self.n):
            area = area + (aux[i][0] * aux[i + 1][1] - aux[i + 1][0] * aux[i][1])
        area = area / 2
        return area

    def getPoints(self):
        return self.puncte

    def getN(self):
        return self.n

    def __getitem__(self, item):
        return self.puncte[item]

    def __setitem__(self, key, value):
        self.puncte[key] = value

    def compare(self, other):
        if self.getArea() > other.getArea():
            return -1
        elif self.getArea() < other.getArea():
            return 1
        else:
            return 0

    def __gt__(self, other):
        return self.compare(other) == -1

    def __lt__(self, other):
        return self.compare(other) == 1

    def __eq__(self, other):
        return self.compare(other) == 0

    def __le__(self, other):
        return self.compare(other) >= 0

    def __gt__(self, other):
        return self.compare(other) <= 0