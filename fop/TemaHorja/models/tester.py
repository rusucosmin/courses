from models.poligon import Poligon

class Tester:
    '''
    Specificaţi şi implementaţi tipurile abstracte de date menţionate mai jos.
        La toate tipurile de date vor exista operaţii pentru:

        a) creare de valori din domeniul tipului respectiv;
        b) operaţii aritmetice
        c) comparare de valori
        d) extragere de componente
        e) eventual conversii din alte tipuri mentionate.
    Tester Poligon (în planul real)
    '''
    def __init__(self):
        pass

    def testPoligon(self):
        p = Poligon(4, [[-2, -2], [2, -2], [2, 2], [-2, 2]])
        assert(p.getArea() - 16.00 < 0.00001)
        q = Poligon(4, [[-2, -2], [2, -2], [2, 2], [-2, 2]])
        assert(p == q)
        assert(p <= q)
        assert(p >= q)