#include <iostream>
#include <vector>
#include <tutorial.h>
#include <controller.h>
#include <repository.h>
#include <ui.h>
#include <dynamicvector.h>
#include <tester.h>

using namespace std;

int main() {
    Tester t;
    Repository repo("database.in");
    Repository watchList("watchlist.in");
    Controller ctrl(repo, watchList);
    UI ui(ctrl);
    ui.run();
    return 0;
}
