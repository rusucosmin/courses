#include <iostream>

using namespace std;

inline void example_a() {
  cerr << "example_a()\n";
  unsigned int a;
  a = 0xffffffff;
  cerr << a << '\n';
  a = a + 1;
  cout << a << '\n';;
}

inline void example_b() {
  cerr << "example_b()\n";
  unsigned int a;
  a = 0;
  cerr << a << '\n';
  a = a - 1;
  cout << a << '\n';
}


int main() {
  example_a();
  example_b();
}
