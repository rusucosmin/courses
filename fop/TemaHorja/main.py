'''
Programare modulara –TAD

Specificaţi şi implementaţi tipurile abstracte de date menţionate mai jos.

 La toate tipurile de date vor exista operaţii pentru:

a) creare de valori din domeniul tipului respectiv;

 b) operaţii aritmetice

 c) comparare de valori

d) extragere de componente

e) eventual conversii din alte tipuri mentionate.

4. POLINOM  (cu coeficienţi întregi)

7. COLECTIE de numere întregi (asemănător mulţimii)

17. Tad Timp (Ora, Min, Sec)

20. Tad Poligon (în planul real)

La problema 20 trebuie si testare
'''


from models.polinom import Polinom
from models.multime import Multime
from models.timp import Timp
from models.poligon import Poligon
from models.tester import Tester


t = Tester()
t.testPoligon()

p = Polinom(3, [3, 2, 1])
q = Polinom(2, [1, 5])

print(p.value(2))
print(q.value(2))

print(p.cmp_value(q, 2))
print(q.cmp_value(p, 2))

print(p.value(10))
print(q.value(10))

print(p.cmp_value(q, 10))
print(q.cmp_value(p, 10))

a = Multime()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
b = Multime([1, 2, 3, 4])
b.remove(2)
print(a.el)
print(b.el)

tmp = Timp(12, 53, 59)
tmp.tickSecunda()
print(tmp)
print(tmp + tmp)
tmp.tickOra()
tmp = tmp + tmp
print(tmp)

p = Poligon(4, [[-2, -2], [2, -2], [2, 2], [-2, 2]])
print(p.getArea())

def examplesPolinom():
    
