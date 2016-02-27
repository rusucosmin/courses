#include <stdio.h>
#include <stdlib.h>
#include "ui/ui.h"
#include "utils/vector.h"
#include "model/material.h"
#include "repository/repository.h"
#include "controller/controller.h"

void test() {
   /**Test *t = malloc(sizeof(Tester));
    testInit(t);
    testRun(t);
    testDistroy(t);*/
}

void app() {
    Repository *repo = (Repository *) malloc(sizeof(Repository));
    Controller *ctrl = (Controller *) malloc(sizeof(Controller));
    repo_init(repo);
    controller_init(ctrl, repo);
    UI * ui = (UI *) malloc(sizeof(UI));

    ui_init(ui, ctrl);
    run(ui);
    ui_destroy(ui);
    controller_destroy(ctrl);
    repo_destroy(repo);
}

int main() {
    app();
    return 0;
}
