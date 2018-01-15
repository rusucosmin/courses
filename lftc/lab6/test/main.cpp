#include <iostream>

using namespace std;

int main(){
  int a;
  int b;
  int c;
  cin >> a;
  cin >> b;
  if(a + 1 > 5) {
    cout << a;
    cout << b;
  }
  c = 1 + (a * (b - 1));
  cout << c;
  return 0;
}
