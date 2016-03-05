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

typedef struct tm m_time;

typedef struct {
    char *name, *supplier;
    float quantity;
    m_time expiration;
} Material;

static const Material NULL_MATERIAL;

/// Constructor and destructor
void material_init(Material* self, char* name, char* supplier, float quantity, m_time expiration);
void material_destroy(Material* self);

/// Method to return the name of a material (getter for the name of the Material)
char* material_getName(Material* self);

/// Method to return the supplier of a Material (getter for the supplier of the Material)
char* material_getSupplier(Material* self);
/// Method to return the quantity of a Material (getter for the quantity of the Material)
float material_getQuantity(Material* self);
/// Method to return the expiration date of a Material (getter for the expiration date of the Material
m_time material_getExpiration(Material* self);
/// Method to check if two materials are equal
int material_equal(Material *a, Material *b);
/**
    Method to check if a material has expired (based on the date of the computer)
    Returns 1 if the material has expire
            0 otherwise
*/
int material_expired(Material *a);

#endif // MATERIAL_H_INCLUDED
