#include <iostream>
#include "domain/material.h"
#include "domain/material.c"

#include "ui/ui.h"
#include "ui/ui.c"
#include <stdio.h>
#include <malloc.h>

using namespace std;

void app() {
    Material *m = (Material *) malloc(sizeof(Material));
    #ifdef MATERIAL_C_INCLUDED
    printf("MaterialCINclude");
    getName(m);
    #endif
    UI *ui = (UI *) malloc(sizeof(UI));
    uiDestroy(ui);
 //   uiInit(ui);
  //  run(ui);
 //   uiDestroy(ui);
}

int main()
{
    app();
    return 0;
}
