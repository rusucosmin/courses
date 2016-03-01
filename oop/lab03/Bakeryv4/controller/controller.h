#ifndef CONTROLLER_H_INCLUDED
#define CONTROLLER_H_INCLUDED

#include "../repository/repository.h"

typedef struct {
    Repository *repo;
} Controller;

/// Constructors and destructors
void controller_init(Controller *self, Repository *repo);
void controller_destroy(Controller *self);

/// Public
vector *controller_getMaterials(Controller *self);
int controller_addMaterial(Controller *self, Material m);
int controller_deleteMaterial(Controller *self, Material m);
int controller_updateMaterial(Controller *self, Material m);

vector *controller_filterExpired(Controller *self, char *s);
vector *controller_filterSupplier(Controller *self, char *s, int bound);

#endif // CONTROLLER_H_INCLUDED
