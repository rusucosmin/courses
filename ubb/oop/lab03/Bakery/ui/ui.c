#ifndef UI_C_INCLUDED
#define UI_C_INCLUDED

#include <stdio.h>
#include "ui.h"

/// private methods

int ui__getInteger(const char *message) {
    char s[15];
    int ret = 0;
    int r = 0;
    printf(message);
    scanf("%15s", s);
    while(sscanf(s, "%d", &ret) != 1) {
        printf(message);
        scanf("%15s", s);
    }
    return ret;
}

int ui__getCmd() {
    int cmd = ui__getInteger("Give command: ");
    return cmd;
}

void ui__printMenu() {
	printf("Menu:\n");
	printf("1. Show materials in bakery\n");
	printf("2. Add object in bakery\n");
	printf("3. Delete object from bakery\n");
	printf("4. Update object in bakery\n");
	printf("\n0. Exit\n");
}

void run(UI *self) {
    while(1) {
        ui__printMenu();
        ui__getCmd();
    }
}

void uiInit(UI *self) {
    ;
}

void uiDestroy(UI *self) {
    free(self);
    self = NULL;
}


#endif
