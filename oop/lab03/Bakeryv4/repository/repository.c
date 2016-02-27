#include "repository.h"
#include "../utils/vector.h"

///Constructors and destructors
void repo_init(Repository *self) {
    self->arr = (vector *) malloc(sizeof(vector));
    vector_init(self->arr);
}

void repo_destroy(Repository *self){
    free(self->arr);
    self->arr = NULL;
    free(self);
    self = NULL;
}

///Public
vector *repo_getMaterials(Repository *self) {
    return self->arr;
}

void repo_addMaterial(Repository *self, Material m) {
    vector_pushBack(self->arr, m);
}

int repo_findMaterial(Repository *self, Material m) {
    int n = vector_getLen(self->arr), i;
    for(i = 0 ; i < n ; ++ i) {
        Material act;
        act = vector_getAt(self->arr, i);
        if(material_equal(&act, &m))
            return 1;
    }
    return 0;
}

void repo_deleteMaterial(Repository *self, Material m) {
    int n = vector_getLen(self->arr), i;
    for(i = 0 ; i < n ; ++ i) {
        Material act;
        act = vector_getAt(self->arr, i);
        if(material_equal(&act, &m))
            vector_removeAt(self->arr, i);
    }
}

void repo_updateMaterial(Repository *self, Material m) {
    int n = vector_getLen(self->arr), i;
    for(i = 0 ; i < n ; ++ i) {
        Material act;
        act = vector_getAt(self->arr, i);
        if(material_equal(&act, &m))
            vector_setAt(self->arr, i, m);
    }
}
