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
    float quantity;
    time_t expiration;
} Material;

static const Material NULL_MATERIAL;

void material_init(Material* self, char* name, char* supplier, float quantity, time_t expiration);

void material_destroy(Material* self);

char* material_getName(Material* self);

char* material_getSupplier(Material* self);

double material_getQuantity(Material* self);

time_t material_getExpiration(Material* self);

int material_equal(Material *a, Material *b);

#endif // MATERIAL_H_INCLUDED
