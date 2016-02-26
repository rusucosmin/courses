#include <stdio.h>
#include <stdlib.h>
#include "ui/ui.h"
#include "utils/vector.h"
#include "model/material.h"

void test() {
   /**Test *t = malloc(sizeof(Tester));
    testInit(t);
    testRun(t);
    testDistroy(t);*/
}

void app() {
    UI * ui = malloc(sizeof(UI));
    ui_init(ui);
    run(ui);
}

void materialPrint(Material a) {
    printf("Material name: %s\nSupplier: %s\nQuality %2f\n", a.name, a.supplier, a.quantity);
}

void vectorTest() {
    vector v;
    vector_init(&v);

    Material m;
    time_t aux;
    time(&aux);
    material_init(&m, "Pita", "Sandana", 100.0, aux);
    vector_pushBack(&v, m);

    material_init(&m, "Faina", "Cineva, cine nu-i de mutra ta!", 11.0, aux);
    vector_pushBack(&v, m);


    material_init(&m, "Bolovani", "SC Bolovani SRL", 15.5, aux);
    vector_pushBack(&v, m);


    material_init(&m, "Orez", "Bunatati de la bunica", 14.2, aux);
    vector_pushBack(&v, m);

    int i = 0;
    for(i = 0 ; i < vector_getLen(&v) ; ++ i)
        materialPrint(vector_getAt(&v, i));

    vector_removeAt(&v, 2);

    for(i = 0 ; i < vector_getLen(&v) ; ++ i)
        materialPrint(vector_getAt(&v, i));
}

int main() {
    vectorTest();
    test();
    //app();
    return 0;
}
