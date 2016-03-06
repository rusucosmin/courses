#ifndef CONTROLLER_H_INCLUDED
#define CONTROLLER_H_INCLUDED

#include "../repository/repository.h"

/**
    Structure Controller;
    Propertis:
        Repository *repo -> pointer to the Medication Repository
*/
typedef struct {
    Repository *repo;
} Controller;

/// Constructors and destructors
void controller_init(Controller *self, Repository *repo);
void controller_destroy(Controller *self);

/// Public
/// Method returns all the available Materials
vector *controller_getMaterials(Controller *self);
/// Method adds a Material to the Repository
int controller_addMaterial(Controller *self, Material m);
/**
    Method to delete a Material
    Returns 0 if the material to be deleted it is not in the Repository
            1 otherwise
*/
int controller_deleteMaterial(Controller *self, Material m);
/**
    Method to update a Material
    Returns 0 if the material to be updated it is not in the Repository
            1 otherwise
*/
int controller_updateMaterial(Controller *self, Material m);
/**
    Method to get the expired Materials that contains a given string
*/
vector *controller_filterExpired(Controller *self, char *s);
/**
    Method to get the Materials from a specific supplier which are in quantity less than bound
*/
vector *controller_filterSupplier(Controller *self, char *s, float bound, int reversed);

/**
    Method to filter the Materials
    Returns a new vector with all the Materials that passed the filter function (passed by argument)
*/
vector* controller_filter(Controller *self, int (*material_filter)(Material a));

/**
    Method to undo the last performed operation
*/
int controller_undo(Controller *self);
/**
    Method to redo the last performed undo
*/
int controller_redo(Controller *self);

/// Filters

int material_cmp_quantity(Material a, Material b);

int material_filter_expired(Material a);

int material_filter_expireIn7Days(Material a);

int material_filter_emptyStock(Material a);

int material_filter_expired_and_contains_string(Material a, char *s);

int material_filter_supplier_and_bound_quantity(Material a, char *s, float bound);

#endif // CONTROLLER_H_INCLUDED
