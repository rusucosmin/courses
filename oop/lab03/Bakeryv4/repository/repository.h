#ifndef REPOSITORY_H_INCLUDED
#define REPOSITORY_H_INCLUDED

#include "../utils/vector.h"

typedef struct {
    vector *arr;
} Repository;

///Constructors and destructors
void repo_init(Repository *self);
void repo_destroy(Repository *self);

///Public
vector *repo_getMaterials(Repository *self);
void repo_addMaterial(Repository *self, Material m);
void repo_deleteMaterial(Repository *self, Material m);
void repo_updateMaterial(Repository *self, Material m);
int repo_findMaterial(Repository *self, Material m);

#endif // REPOSITORY_H_INCLUDED
