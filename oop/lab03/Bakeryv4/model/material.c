#ifndef MATERIAL_C_INCLUDED
#define MATERIAL_C_INCLUDED

#include <string.h>
#include "material.h"

void material_init(Material *self, char* name, char* supplier, double quantity, time_t expiration) {
    if(!self) {
        printf("Error: Material is NULL at creation, ABORT CREATION\n");
        return ;
    }

    self->name = malloc(sizeof(char) * (strlen(name) + 1));
    strcpy(self->name, name);

    self->supplier = malloc(sizeof(char) * (strlen(supplier) + 1));
    strcpy(self->supplier, supplier);

    self->quantity = quantity;
    self->expiration = expiration;
}

void material_destroy(Material *self) {
    if(!self) {
        printf("Error - Material is NULL at destroy! ABORT DESTROY!\n");
        return ;
    }
    free(self->name);
    self->name = NULL;

    free(self->supplier);
    self->supplier = NULL;

    self->quantity = -1;
}

char* get_name(Material* self) {
    return self->name;
}

char* get_supplier(Material* self) {
    return self->supplier;
}

double get_quantity(Material *self) {
    return self->quantity;
}

time_t get_expiration(Material *self) {
    return self->expiration;
}


#endif // MATERIAL_C_INCLUDED
