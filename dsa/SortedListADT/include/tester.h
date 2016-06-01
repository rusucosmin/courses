#ifndef TESTER_H
#define TESTER_H

#include <sortedsllist.h>
#include <sortedlistbst.h>
#include <iostream>
#include <time.h>
#include <set>
#include <algorithm>
#include <stdlib.h>

class Tester {
public:
    /** Default constructor */
    Tester();
    /** Unit tests for all the SortedListBST methods */
    void unitTestSortedListBSTAdd();
    void unitTestSortedListBSTRemove();
    void unitTestSortedListBSTGet();
    void unitTestSortedListBSTContains();
    void unitTestSortedListBSTClear();

        /** Unit tests for all the SortedSLList methods */
    void unitTestSortedSLListAdd();
    void unitTestSortedSLListRemove();
    void unitTestSortedSLListGet();
    void unitTestSortedSLListContains();
    void unitTestSortedSLListClear();

    void randomTest();
};

Tester::Tester() {
    /*
    SortedListBST <int> l;
    l.add(6567);
    l.add(7073);
    l.add(4334);
    l._dfs(l._root);
    l.removeAtIndex(1);

    l.add(4);
    l.add(2);
    l.add(1);
    l.add(3);
    l.add(6);
    l.add(5);
    l.add(7);
    l.removeAtIndex(0);
    l.removeAtIndex(0);
    l.removeAtIndex(0);
    while(l.size())
        l.removeAtIndex(rand() % l.size());
    l._dfs(l._root);
    return ;*/
    srand(time(NULL));

    randomTest();
    std::cerr << "RandomTest - passed\n";
    unitTestSortedSLListAdd();
    std::cerr << "SortedSLListAdd - passed\n";
    unitTestSortedSLListRemove();
    std::cerr << "SortedSLListRemove - passed\n";
    unitTestSortedSLListGet();
    std::cerr << "SortedSLListGet - passed\n";
    unitTestSortedSLListContains();
    std::cerr << "SortedSLListContains - passed\n";
    unitTestSortedSLListClear();
    std::cerr << "SortedSLListClear - passed\n";

    unitTestSortedListBSTAdd();
    std::cerr << "SortedBSTAdd - passed\n";
    unitTestSortedListBSTRemove();
    std::cerr << "SortedBSTRemove - passed\n";
    unitTestSortedListBSTGet();
    std::cerr << "SortedBSTGet - passed\n";
    unitTestSortedListBSTContains();
    std::cerr << "SortedBSTContains - passed\n";
    unitTestSortedListBSTClear();
    std::cerr << "SortedBSTCleas - passed\n";
}

void Tester::unitTestSortedListBSTAdd() {
    SortedListBST <int> sList;
    sList.add(5);
    sList.add(4);
    sList.add(1);
    sList.add(2);
    sList.add(0);
    sList.add(3);
    sList.add(6);
    ///sList._dfs(sList._root);
    for(int i = 0 ; i < sList.size() ; ++ i) {
        assert(sList.getAtIndex(i) == i);
    }
}

void Tester::unitTestSortedListBSTRemove() {
    SortedListBST<int> sList;
    sList.add(5);
    sList.add(4);
    sList.add(3);
    sList.add(2);
    sList.add(1);
    sList.add(6);
    sList.add(0);

    sList.removeAtIndex(0);
    for(int i = 0 ; i < sList.size() ; ++ i) {
        assert(sList.getAtIndex(i) == i + 1);
    }
    sList.removeAtIndex(sList.size() - 1);
    for(int i = 0 ; i < sList.size() ; ++ i) {
        assert(sList.getAtIndex(i) == i + 1);
    }
    sList.removeAtIndex(3);
    assert(sList.getAtIndex(0) == 1);
    assert(sList.getAtIndex(1) == 2);
    assert(sList.getAtIndex(2) == 3);
    assert(sList.getAtIndex(3) == 5);
    for(int i = 0; i < sList.size(); ++ i)
        std::cerr << sList.getAtIndex(i) << ' ';
    while(sList.size()) {
        int ind = rand() % sList.size();
        std::cerr << "Remove " << ind << '\n';
        sList.removeAtIndex(ind);
    }
    assert(sList.size() == 0);
}

void Tester::unitTestSortedListBSTGet() {
    SortedListBST<int> sList;

    assert(sList.size() == 0);
    sList.add(5);
    assert(sList.size() == 1);
    sList.add(4);
    assert(sList.size() == 2);
    sList.add(3);
    assert(sList.size() == 3);
    sList.add(2);
    assert(sList.size() == 4);
    sList.add(1);
    assert(sList.size() == 5);
    sList.add(6);
    assert(sList.size() == 6);
    sList.add(0);
    assert(sList.size() == 7);
    for (int index = 0; index < 7; index++) {
        assert(sList.getAtIndex(index) == index);
    }
}

void Tester::unitTestSortedListBSTContains() {
    SortedListBST<int> sList;
    sList.add(5);
    sList.add(4);
    sList.add(3);
    sList.add(2);
    sList.add(1);
    sList.add(6);
    sList.add(0);
    assert(true == sList.contains(0));
    assert(true == sList.contains(1));
    assert(true == sList.contains(2));
    assert(true == sList.contains(3));
    assert(true == sList.contains(4));
    assert(true == sList.contains(5));
    assert(true == sList.contains(6));
    assert(false == sList.contains(7));
    assert(false == sList.contains(-1));
}

void Tester::unitTestSortedListBSTClear() {
    SortedListBST<int> sList;

    sList.add(5);
    sList.add(4);
    sList.add(3);
    sList.add(2);
    sList.add(1);
    sList.add(6);
    sList.add(0);

    assert(true == sList.contains(0));
    assert(true == sList.contains(1));
    assert(true == sList.contains(2));
    assert(true == sList.contains(3));
    assert(true == sList.contains(4));
    assert(true == sList.contains(5));
    assert(true == sList.contains(6));
    sList.clear();
    assert(false == sList.contains(0));
    assert(false == sList.contains(1));
    assert(false == sList.contains(2));
    assert(false == sList.contains(3));
    assert(false == sList.contains(4));
    assert(false == sList.contains(5));
    assert(false == sList.contains(6));
    assert(0 == sList.size());
}

void Tester::unitTestSortedSLListAdd() {
    SortedSLList <int> sList;
    sList.add(5);
    sList.add(4);
    sList.add(1);
    sList.add(2);
    sList.add(0);
    sList.add(3);
    sList.add(6);
    for(int i = 0 ; i < sList.size() ; ++ i)
        assert(sList.getAtIndex(i) == i);
}

void Tester::unitTestSortedSLListRemove() {
    SortedSLList<int> sList;
    sList.add(5);
    sList.add(4);
    sList.add(3);
    sList.add(2);
    sList.add(1);
    sList.add(6);
    sList.add(0);

    sList.removeFront();
    assert(sList.getFront() == 1);
    sList.removeBack();
    assert(sList.getBack() == 5);
    sList.removeAtIndex(2);
    assert(sList.getAtIndex(0) == 1);
    assert(sList.getAtIndex(1) == 2);
    assert(sList.getAtIndex(2) == 4);
    assert(sList.getAtIndex(3) == 5);
}
void Tester::unitTestSortedSLListGet() {
    SortedSLList<int> sList;

    assert(sList.size() == 0);
    sList.add(5);
    assert(sList.size() == 1);
    sList.add(4);
    assert(sList.size() == 2);
    sList.add(3);
    assert(sList.size() == 3);
    sList.add(2);
    assert(sList.size() == 4);
    sList.add(1);
    assert(sList.size() == 5);
    sList.add(6);
    assert(sList.size() == 6);
    sList.add(0);
    assert(sList.size() == 7);
    for (int index = 0; index < 7; index++) {
        assert(sList.getAtIndex(index) == index);
    }
    assert(sList.getFront() == 0);
    assert(sList.getBack() == 6);
}

void Tester::unitTestSortedSLListContains() {
    SortedSLList<int> sList;
    sList.add(5);
    sList.add(4);
    sList.add(3);
    sList.add(2);
    sList.add(1);
    sList.add(6);
    sList.add(0);
    assert(true == sList.contains(0));
    assert(true == sList.contains(1));
    assert(true == sList.contains(2));
    assert(true == sList.contains(3));
    assert(true == sList.contains(4));
    assert(true == sList.contains(5));
    assert(true == sList.contains(6));
    assert(false == sList.contains(7));
    assert(false == sList.contains(-1));
}

void Tester::unitTestSortedSLListClear() {
    SortedSLList<int> sList;

    sList.add(5);
    sList.add(4);
    sList.add(3);
    sList.add(2);
    sList.add(1);
    sList.add(6);
    sList.add(0);

    assert(true == sList.contains(0));
    assert(true == sList.contains(1));
    assert(true == sList.contains(2));
    assert(true == sList.contains(3));
    assert(true == sList.contains(4));
    assert(true == sList.contains(5));
    assert(true == sList.contains(6));
    sList.clear();
    assert(false == sList.contains(0));
    assert(false == sList.contains(1));
    assert(false == sList.contains(2));
    assert(false == sList.contains(3));
    assert(false == sList.contains(4));
    assert(false == sList.contains(5));
    assert(false == sList.contains(6));
    assert(0 == sList.size());
}

void Tester::randomTest() {
    int m = 1000;
    int maxval = 1000000000;
    std::multiset <int> s;
    SortedListBST<int> bstList;
    SortedSLList<int> slList;
    for(int i = 1; i <= m; ++ i) {
        assert(slList.size() == s.size());
        assert(bstList.size() == s.size());
        int op = rand() % 3;
        if(op == 0) { /// insert
            int val = rand() % maxval;
            s.insert(val);
            slList.add(val);
            bstList.add(val);
        }
        else if(op == 1) {
            if(!s.size())  /// they are empty
                continue;
            int ind = rand() % s.size();
            auto it = s.begin();
            std::advance(it, ind);
            s.erase(it);
            slList.removeAtIndex(ind);
            bstList.removeAtIndex(ind);
        }
        else {
            std::vector <int> v;
            std::vector <int> a, b;
            for(int i = 0; i < v.size(); ++ i) {
                a.push_back(slList.getAtIndex(i));
                b.push_back(bstList.getAtIndex(i));
            }
            assert(v == a); /// and implictly, a == b
            assert(v == b);
        }
    }
}


#endif // TESTER_H
