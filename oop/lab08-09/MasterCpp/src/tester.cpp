#include "tester.h"

#include <cassert>
#include <dynamicvector.h>
#include <tutorial.h>
#include <iostream>
using namespace std;

Tester::Tester()
{
    testDynamicVector();
    //ctor
}

void Tester::testDynamicVector() {
    DynamicVector <Tutorial> v;
    v.push_back(Tutorial("Title", "Presenter", "www.link.com", 30, 20));
    DynamicVector <Tutorial> cv(v);
    DynamicVector <Tutorial> dv = v;
    v.remove(Tutorial("Title", " ", "www.link.com", 60, 20));

    assert(v.size() == 0);
    assert(cv.size() == 1);
    assert(dv.size() == 1);
    cv[0] = Tutorial();

    DynamicVector <int> ints;
    for(int i = 1 ; i <= 100 ; ++ i) {
        ints.push_back(i);
    }
    for(int i = 0 ; i < 10 ; ++ i)
        assert(ints[i] == i + 1);
    ints.remove(10);
    assert(ints[9] == 100);
    for(int i = 11 ; i < 98 ; ++ i)
        assert(ints[i] == i + 1);
    cerr << "Dynamic Vector test passed\n";
}
