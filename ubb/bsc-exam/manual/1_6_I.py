'''
I. Write a program in one of the programming languages Python, C++, Java, C# that:
  a. Define a class B with an integer attribute b and a printing method that displays the
attribute b to the standard output.
54
  b. Define a class D derived from B with an attribte d of type string and also a method
of printing on standard output that displays the attribute b of the base class and the
attribute d.
  c. Define a function that builds a list containing: an object o1 of type B having b
equal to 8; an object o2 of type D having b equal to 5 and d equal to D5; an
object o3 of type B having b equal to -3; an object o4 of type D having b equal to 9
and d equal to D9.
  d. Define a function that receives a List of objects of type B and returns a List
containing only the items that satisfy the property: b>6.
  e. For data type List used in the program, write the specifications of the used
operations.
'''
class B:
  def __init__(self, b = 0):
    self.b = b

  def print(self):
    print(self.b)


x = B(10)
x.print()

class D(B):
  def __init__(self, b = 0, d = ""):
    self.b = b
    self.d = d

  def print(self):
    print("%d %s\n" % (self.b, self.d));

y = D(10, 'ana')
y.print()

def build_list():
  return [B(8), D(5, "D5"), B(-3), D(9, "D9")]

def filter_list(x):
  return [el for el in x if el.b > 6]

for x in filter_list(build_list()):
  x.print()







