from models.polinom import Polinom
from models.multime import Multime

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