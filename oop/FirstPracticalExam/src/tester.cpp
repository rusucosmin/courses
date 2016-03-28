#include "tester.h"

#include <cassert>
#include <repository.h>
#include <vector>
#include <club.h>
#include <iostream>
#include <controller.h>

using namespace std;

Tester::Tester()
{
    Repository testRepo("tester.in");
    vector <Club> _init;
    _init.push_back(Club("OK", "disco", 5));
    _init.push_back(Club("BiancoNero", "house", 4));
    _init.push_back(Club("LaNeaGicu", "manele", 1));
    _init.push_back(Club("Opera", "clasic", 3));
    _init.push_back(Club("NoName", "house", 1));
    assert(testRepo.getAll() == _init);
    testRepo.add(Club("Noa", "house", 6));
    _init.push_back(Club("Noa", "house", 6));
    assert(testRepo.getAll() == _init);

    Controller ctrl(testRepo);
    vector <Club> filterRes;
    filterRes.push_back(Club("Noa", "house", 6));
    filterRes.push_back(Club("BiancoNero", "house", 4));
    filterRes.push_back(Club("NoName", "house", 1));

    assert(ctrl.filter("house").size() == 3);
    assert(ctrl.filter("house") == filterRes);

    ctrl.add(Club("Dada", "house", 7));
    filterRes.insert(filterRes.begin(), Club("Dada", "house", 6));
    assert(ctrl.filter("house") == filterRes);

    /// cerr << "All test passed\n";
}
