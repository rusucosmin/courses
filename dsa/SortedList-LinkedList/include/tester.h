#ifndef TESTER_H
#define TESTER_H

#include <sortedlist.h>
#include <set>
#include <cassert>

using namespace std;

class Tester {
public:
    /** Default constructor */
    Tester() {
        srand(time(NULL));
    }
    void testAll() {
        unitTest();
        randomTest();
    }
    void unitTest() {
        SortedList<int> l;
        multiset<int> s;
        l.insert(1);
        l.insert(2);
        assert(l.size() == 2);
        assert(*l.find(1) == 1);
        assert(*l.find(2) == 2);
        assert(l.find(3) == l.end());
        l.remove(2);
        assert(l.size() == 1);
        assert(*l.find(1) == 1);
        assert(l.find(2) == l.end());
        assert(l.find(3) == l.end());
        l.remove(1);
        assert(l.size() == 0);
        assert(l.find(1) == l.end());
        assert(l.find(2) == l.end());
        assert(l.find(3) == l.end());
    }
    inline bool equal(SortedList <int> &l, multiset <int> &s) {
        vector <int> v1, v2;
        for(SortedList <int> :: iterator it = l.begin() ; it != l.end() ; ++ it)
            v1.push_back(*it);
        for(multiset <int> :: iterator it = s.begin() ; it != s.end() ; ++ it)
            v2.push_back(*it);
        return v1 == v2;
    }
    void randomTest() {
        SortedList <int> l;
        multiset <int> s;
        vector <int> values;
        values.push_back(1);
        for(int cnt = 0 ; cnt < NOP ; ++ cnt) {
            int op = rand() % MAXOP;
            assert(l.size() == s.size());
            cerr << cnt << "\n";
            int val;
            switch(op) {
            case 0:
                val = rand() % MAXVAL;
                values.push_back(val);
                l.insert(val);
                s.insert(val);
                break;
            case 1:
                break;
                val = rand() % values.size();
                val = values[val];
                l.remove(val);
                s.erase(val);
                break;
            case 2:
                val = rand() % values.size();
                val = values[val];
                cerr << "val = " << val << ": " << l.count(val) << ' ' << s.count(val) << '\n';
                assert(l.count(val) == s.count(val));
                break;
            case 3:
                assert(equal(l, s));
                break;
            }
        }
    }
public:
    static const int NOP = 100000; /// test for NOP operation
    static const int MAXOP = 4; /// 0 - insert, 1 - remove all, 2 - count, 3 - getall
    static const int MAXVAL = 10;
};

#endif // TESTER_H
