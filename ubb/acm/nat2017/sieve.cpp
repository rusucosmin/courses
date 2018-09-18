#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <cstring>
#define DN 100005
#define LL long long
using namespace std;


int countSteps(int n, vector<int> p) {
    vector<bool> Composite(n + 1, false);
    int steps = 0;
    // p este o permutare a multimii {2, 3, ..., n}
    for(int index = 0; index < n - 1; ++index) {
        if(not Composite[p[index]]) {
            for(int multiple = 2 * p[index]; multiple <= n; multiple += p[index]) {
                Composite[multiple] = true;
                steps += 1;
            }
        }
    }
 
    return steps;
}

int main() {
    int lrz=1;
    for(int n=2; n<=12; ++n) {
        vector<int> p;
        int fct=1;
        for(int i=2; i<=n; ++i) {
            p.push_back(i);
            if(i<n) fct*=i;
        }
        long long rz=0;
        do {
            rz+=countSteps(n,p);
        }while(next_permutation(p.begin(),p.end()));
        cout << rz << ' ' <<(double)rz/fct<<"\n";
        //cout<<rz<<", ";
    }
}
