#ifndef TESTER_H
#define TESTER_H

#include <sortedsllist.h>
#include <sortedlistbst.h>
#include <iostream>
#include <time.h>
#include <set>
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
};

Tester::Tester() {
    srand(time(NULL));

    unitTestSortedSLListAdd();
    unitTestSortedSLListRemove();
    unitTestSortedSLListGet();
    unitTestSortedSLListContains();
    unitTestSortedSLListClear();

    unitTestSortedListBSTAdd();
    unitTestSortedListBSTRemove();
    unitTestSortedListBSTGet();
    unitTestSortedListBSTContains();
    unitTestSortedListBSTClear();
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
    while(sList.size())
        sList.removeAtIndex(rand() % sList.size());
    assert(sList.size() == 0);
    ///todo continu
    std::set <int> s = {1, 2, 3, 4};
    std::set <int> :: iterator it = s.begin();
    std::advance(it, 2);
    s.erase(it);
    for(auto it : s)
        std::cerr << it << '\n';
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


#endif // TESTER_H
