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
    char *name, supplier;
    double quantity;
    time_t expiration;
} Material;

void productInit(Material* self, char* name, char* supplier, double quantity, time_t expiration);

void productDestroy(Material* self);

char* getName(Material* self);

char* getSupplier(Material* self);

double getQuantity(Material* self);

time_t getExpiration(Material* self);

#endif // MATERIAL_H_INCLUDED
