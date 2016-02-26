#ifndef MATERIAL_H_INCLUDED
#define MATERIAL_H_INCLUDED

#include <time.h>
#include <stdio.h>

/**
    Object Material encapsulates all the information we need to store for each
        bakery ingredient (material).
    Properties:
        name, supplier: strings
        quantity: real number
        expiration: date
*/

typedef struct {
    char *name, *supplier;
    double quantity;
    time_t expiration;
} Material;

static const Material NULL_MATERIAL;

void material_init(Material* self, char* name, char* supplier, double quantity, time_t expiration);

void material_destroy(Material* self);

char* get_name(Material* self);

char* get_supplier(Material* self);

double get_quantity(Material* self);

time_t get_expiration(Material* self);

#endif // MATERIAL_H_INCLUDED
