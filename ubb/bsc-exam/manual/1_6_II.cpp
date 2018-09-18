/*
II. Write a program in one of the Python, C++, Java, C# languages which:
  a. Defines a class B having an attribute b of type integer and a display method,
which displays the attribute b to the standard output.
  b. Defines a class D derived from B having an attribute d of type string and also a
method to display on the standard output attribute b from the base class and
attribute d.
  c. Define a function which builds a map which contains: an object o1 of type B
having b equal to 8; an object o2 of type D having b equal to 5 and d equal to
„D5”; an object o3 of type B having b equal to -3; an object o4 of type D having b
equal to 9 and d equal to „D9”. (the key of an object from the map is the value of
b, and the value associated to this key is the object itself.)
  d. Define a function which receives a map with objects of type B and verifies
whether in the map there is an object which satisfies the property: b>6.
  e. For the map abstract data type used in the program, write the specifications of the
used operations.
*/

#include <iostream>
#include <map>
using namespace std;

class B {
protected:
  int b;
public:
  B(int b) {
    this->b = b;
  }
  int get_b() {
    return this->b;
  }
  virtual void display() {
    cout << b << '\n';
  }
};

class D: public B {
protected:
  string d;
public:
  D(int b, string d): B(b) {
    this->d = d;
  }
  virtual void display() {
    B::display();
    cout << d << '\n';
  }
};

map<int, B*> build_map() {
  map<int, B*> m;
  B* o1 = new B(8);
  B* o2 = new D(5, "D5");
  B* o3 = new B(-3);
  B* o4 = new D(9, "D9");
  m[o1->get_b()] = o1;
  m[o2->get_b()] = o2;
  m[o3->get_b()] = o3;
  m[o4->get_b()] = o4;
  return m;
}

bool is_property(map<int, B*> m) {
  for(auto it : m) {
    if(it.second->get_b() > 6) {
      return true;
    }
  }
  return false;
}

int main() {
  B b(10);
  b.display();
  D d(10, "ana");
  d.display();
}
