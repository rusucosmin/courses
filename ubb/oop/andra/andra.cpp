#include <iostream>

using namespace std;

class B {
public:
    B() {
        cout << "B()\n";
    }
    B(string name) {
        cout << "B(" << name << ")\n";
    }
    virtual void sayHello() {
        cout << "Hello from B\n";
    }
};


class D: public B {
public:
    D() {
        cout << "D()\n";
    }
    D(string s) {
        cout << "D(" << s << ")\n";
    }
    void sayHello() {
        cout << "Hello from D\n";
    }
};

int main() {
    D d;
}
