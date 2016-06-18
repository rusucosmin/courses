#include <iostream>

using namespace std;

int main() {
    int ***a = new int**[10];
    for(int i = 0 ; i < 10; ++ i) {
       a[i] = new int*[10];
       for(int j = 0 ; j < 10; ++ j)
            a[i][j] = new int[10];
    }
    cout << a[0][0][0] << '\n';
}
