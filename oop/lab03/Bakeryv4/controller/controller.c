#include "controller.h"
#include "../model/material.h"

/// Constructors and destructors
void controller_init(Controller *self, Repository *repo) {
    self->repo = repo;
}

void controller_destroy(Controller *self){
    free(self);
    self = NULL;
}

/// Public
vector *controller_getMaterials(Controller *self) {
    return repo_getMaterials(self->repo);
}

int controller_addMaterial(Controller *self, Material m){
    if(repo_findMaterial(self->repo, m) == 1) {
        vector *arr;
        arr = controller_getMaterials(self);
        int n = vector_getLen(arr), i;
        for(i = 0 ; i < n ; ++ i) {
            Material act = vector_getAt(arr, i);
            if(material_equal(&act, &m)) {
                act.quantity += m.quantity;
                vector_setAt(arr, i, act);
                return 0;
            }
        }
    }
    repo_addMaterial(self->repo, m);
    return 1;
}

int controller_deleteMaterial(Controller *self, Material m) {
    if(repo_findMaterial(self->repo, m) == 0)
        return 0;
    repo_deleteMaterial(self->repo, m);
    return 1;
}

int controller_updateMaterial(Controller *self, Material m) {
    if(repo_findMaterial(self->repo, m) == 0)
        return 0;
    repo_updateMaterial(self->repo, m);
    return 1;
}

static int material_cmp_quantity(Material a, Material b) {
    return material_getQuantity(&a) < material_getQuantity(&b);
}

static int material_filter_expired(Material a) {
    return !material_expired(&a);
}

static int material_filter_expired_and_contains_string(Material a, char *s) {
    return strstr(material_getName(&a), s) != NULL && material_expired(&a);
}

static int material_filter_supplier_and_bound_quantity(Material a, char *s, float bound) {
    return strcmp(material_getSupplier(&a), s) == 0 && material_getQuantity(&a) <= bound;
}

vector* controller_filter(Controller *self, int (*material_filter)(Material a)) {
    vector *ret = (vector *) malloc(sizeof(vector));
    vector_init(ret);
    vector *all = repo_getMaterials(self->repo);
    int n = vector_getLen(all);
    for(int i = 0 ; i < n ; ++ i) {
        Material m = vector_getAt(all, i);
        if(material_filter(m))
            vector_pushBack(ret, m);
    }
    return ret;
}

vector *controller_filterExpired(Controller *self, char *s) {
    vector *ret = (vector *) malloc(sizeof(vector));
    vector_init(ret);
    vector *all = repo_getMaterials(self->repo);
    int n = vector_getLen(all);
    s[strlen(s)] = '\0';
    for(int i = 0 ; i < n ; ++ i) {
        Material m = vector_getAt(all, i);
        if(material_filter_expired_and_contains_string(m, s))
            vector_pushBack(ret, m);
    }
    return ret;
}

vector *controller_filterSupplier(Controller *self, char *s, float bound) {
    vector *ret = (vector *) malloc(sizeof(vector));
    vector_init(ret);
    vector *all = repo_getMaterials(self->repo);
    int n = vector_getLen(all);
    s[strlen(s)] = '\0';
    for(int i = 0 ; i < n ; ++ i) {
        Material m = vector_getAt(all, i);
        if(material_filter_supplier_and_bound_quantity(m, s, bound))
            vector_pushBack(ret, m);
    }
    vector_sort(ret, &material_cmp_quantity, 0);
    return ret;
}

int controller_undo(Controller *self) {
    return repo_undo(self->repo);
}

int controller_redo(Controller *self) {
    return repo_redo(self->repo);
}
