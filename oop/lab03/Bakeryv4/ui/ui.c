#ifndef UI_C_INCLUDED
#define UI_C_INCLUDED

#include <stdio.h>
#include "ui.h"


/**
    Constructors and destructors
*/

void ui_init(UI *self) {

}

void ui_destroy(UI *self) {
    free(self);
    self = NULL;
}

/// private methods
int ui__getInteger(const char *message) {
    char s[100];
    int ret = 0;
    int r = 0;
    int cnt = 0;
    printf(message);
    scanf("%s", s);
    while(sscanf(s, "%d", &ret) != 1) {
        printf(message);
        scanf("%s", s);
    }
    return ret;
}

void ui__printMenu() {
	printf("Menu:\n");
	printf("1. Show materials in bakery\n");
	printf("2. Add object in bakery\n");
	printf("3. Delete object from bakery\n");
	printf("4. Update object in bakery\n");
	printf("\n0. Exit\n");
}

int ui__getCmd() {
    int cmd = ui__getInteger("Give command: ");
    if ((Commands)cmd >= (Commands)MAX_COMMANDS || (Commands)cmd < EXIT_CMD)
		return ERROR_CMD;
    return cmd;
}

void ui_execCMDShowAll(UI *self) {
}

void ui_execCMDAddMaterial(UI *self) {
}

void ui_execCMDDeleteMaterial(UI *self) {
}

void ui_execCMDUpdateMaterial(UI *self) {
}

void ui__execCmd(UI *self, int cmd) {
    switch(cmd) {
        case CMD_SHOW_OBJECTS:
            ui_execCMDShowAll(self);
            break;
        case CMD_ADD_OBJECT:
            ui_execCMDAddMaterial(self);
            break;
        case CMD_DELETE_OBJECT:
            ui_execCMDDeleteMaterial(self);
            break;
        case CMD_UPDATE_OBJECT:
            ui_execCMDUpdateMaterial(self);
            break;
    }
}

void run(UI *self) {
    while(1) {
        ui__printMenu();
        int cmd = ui__getCmd();
        switch(cmd) {
            case EXIT_CMD:
                return ;
                break;
            case ERROR_CMD:
                printf("Error command!\n");
                break;
            default:
                ui__execCmd(self, cmd);
        }
    }
}


#endif
