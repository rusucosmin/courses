#include <iostream>
#include <vector>
#include <tutorial.h>
#include <controller.h>
#include <repository.h>
#include <ui.h>

using namespace std;

int main() {
    Repository repo("database.in");
    Controller ctrl(repo);
    UI ui(ctrl);
    ui.run();
    return 0;
}
