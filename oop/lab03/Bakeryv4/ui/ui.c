#ifndef UI_C_INCLUDED
#define UI_C_INCLUDED

#include <stdio.h>
#include "ui.h"
#include "../model/material.h"
#include "../controller/controller.h"


/**
    Constructors and destructors
*/

void ui_init(UI *self, Controller * ctrl) {
    self->ctrl = ctrl;
}

void ui_destroy(UI *self) {
    free(self);
    self = NULL;
}

/// private methods
int ui__getInteger(const char *message) {
    char s[100];
    int ret = 0;
    printf(message);
    scanf("%s", s);
    while(sscanf(s, "%d", &ret) != 1) {
        printf(message);
        scanf("%s", s);
    }
    return ret;
}

float ui__getDouble(const char *message) {
    char s[100];
    float ret = 0;
    printf(message);
    scanf("%s", s);
    while(sscanf(s, "%f", &ret) != 1) {
        printf(message);
        scanf("%s", s);
    }
    return ret;
}

void ui__getString(char *s, const char *message) {
    printf(message);
    scanf("%s", s);
}

void ui__printMenu() {
	printf("Menu:\n");
	printf("1. Show materials in bakery\n");
	printf("2. Add object in bakery\n");
	printf("3. Delete object from bakery\n");
	printf("4. Update object in bakery\n");
	printf("\n0. Exit\n");
}

int ui__getCmd(UI *ui) {
    int cmd = ui__getInteger("Give command: ");
    if ((Commands)cmd >= (Commands)MAX_COMMANDS || (Commands)cmd < EXIT_CMD)
		return ERROR_CMD;
    return cmd;
}

Material ui__getMaterial(UI *ui, int readName, int readSupplier, int readQuantity, int readTime) {
    Material act;
    char name[100];
    char supplier[100];
    float quantity;
    if(readName)
        ui__getString(name, "Please input the name of the material: ");
    if(readSupplier)
        ui__getString(supplier, "Please input the name of the supplier: ");
    if(readQuantity)
        quantity = ui__getDouble("Please input the quntity: ");
    time_t cosmin;
    material_init(&act, name, supplier, quantity, cosmin);
    return act;
}

void ui_execCMDShowAll(UI *self) {
    vector *arr;
    arr = controller_getMaterials(self->ctrl);
    int i, n = vector_getLen(arr);
    if(n == 0)
        printf("There are no material to show!\n");
    else {
        printf("These are the materials:\n");
        for(i = 0 ; i < n ; ++ i) {
            Material act;
            act =  vector_getAt(arr, i);
            printf("Material #%d\n", i);
            printf("Name: %s\n", material_getName(&act));
            printf("Supplier: %s\n", material_getSupplier(&act));
            printf("Quantity: %f\n", material_getQuantity(&act));
            printf("\n");
        }
    }
}

void ui_execCMDAddMaterial(UI *self) {
    Material m;
    m = ui__getMaterial(self, 1, 1, 1, 1);
    if(controller_addMaterial(self->ctrl, m) == 0)
        printf("It seems we have a duplicate, we have added the quantities together!\n");
}

void ui_execCMDDeleteMaterial(UI *self) {
    Material m;
    m = ui__getMaterial(self, 1, 0, 0, 0);
    if(controller_deleteMaterial(self->ctrl, m) == 0)
        printf("The material you want to delete does not exist!\n");
}

void ui_execCMDUpdateMaterial(UI *self) {
    Material m;
    m = ui__getMaterial(self, 1, 1, 1, 1);
    if(controller_updateMaterial(self->ctrl, m) == 0)
        printf("The material you want to update does not exist!\n");
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
        int cmd = ui__getCmd(self);
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
