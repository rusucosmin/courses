#include <iostream>
#include <controller.h>
#include <repository.h>
#include <ui.h>
#include <tester.h>

using namespace std;

int main()
{
    Tester t;
    Repository repo("database.in");
    Controller ctrl(repo);
    UI ui(ctrl);
    ui.run();
    return 0;
}
