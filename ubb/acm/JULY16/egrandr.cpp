#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; ++ t) {
        int n;
        cin >> n;
        bool failed = false;
        bool maximum = false;
        int sum = 0;
        for(int i = 0; i < n; ++ i) {
            int now;
            cin >> now;
            if(now == 2)
                failed = true;
            if(now == 5)
                maximum = true;
            sum += now;
        }
        if(!failed && maximum && sum >= 4 * n)
            cout << "Yes\n";
        else
            cout << "No\n";
    }
}
