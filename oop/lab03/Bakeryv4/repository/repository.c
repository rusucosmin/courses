#include "repository.h"
#include "../utils/vector.h"
#include "../model/material.h"

///Constructors and destructors
void repo_init(Repository *self) {
    self->arr = (vector *) malloc(sizeof(vector));
    self->redo = (vector *) NULL;
    self->undo = (vector *) NULL;
    vector_init(self->arr);
}

void repo_initFromFile(Repository *self, char *filename) {
    FILE *fin = fopen(filename, "r");
    int n;
    Material aux;
    fscanf(fin, "%d", &n);
    for(int i = 0 ; i < n ; ++ i) {
        char name[105], supplier[105];
        float quantity;
        m_time expDate;
        fscanf(fin, "%s%s%f%d%d%d", name, supplier, &quantity, &expDate.tm_year, &expDate.tm_mon, &expDate.tm_mday);
        material_init(&aux, name, supplier, quantity, expDate);
        repo_addMaterial(self, aux);
    }
    fclose(fin);
}

void repo_destroy(Repository *self, char *filename){
    Material *arr = repo_getMaterials(self);
    int n = vector_getLen(arr);
    FILE *fout = fopen(filename, "w");
    for(int i = 0 ; i < n ; ++ i) {
        Material m = vector_getAt(arr, i);
        fprintf(fout, "%s %s %f %d %d %d\n", material_getName(&m), material_getSupplier(&m), material_getQuantity(&m),
                material_getExpiration(&m).tm_year, material_getExpiration(&m).tm_mon, material_getExpiration(&m).tm_mday);
    }
    fclose(fout);
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
    repo__saveRepo(&self);
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
    repo__saveRepo(&self);
    int n = vector_getLen(self->arr), i;
    for(i = 0 ; i < n ; ++ i) {
        Material act;
        act = vector_getAt(self->arr, i);
        if(material_equal(&act, &m)) {
            vector_removeAt(self->arr, i);
            return ;
        }
    }
}

void repo_updateMaterial(Repository *self, Material m) {
    repo__saveRepo(&self);
    int n = vector_getLen(self->arr), i;
    for(i = 0 ; i < n ; ++ i) {
        Material act;
        act = vector_getAt(self->arr, i);
        if(material_equal(&act, &m))
            vector_setAt(self->arr, i, m);
    }
}

int repo_undo(Repository **self) {
    if((*self)->undo == (vector *)NULL)
        return 0;
    if((*self)->redo != (vector *) NULL)
        vector_distroy((*self)->redo);
    (*self)->redo = (vector *)malloc(sizeof(vector));
    vector_init((*self)->redo);
    for(int i = 0 ; i < vector_getLen((*self)->arr) ; ++ i)
        vector_pushBack((*self)->redo, vector_getAt((*self)->arr, i));
    vector_distroy((*self)->arr);
    (*self)->arr = (*self)->undo;
    (*self)->undo = (vector *)NULL;
    return 1;
}

int repo_redo(Repository **self) {
    if((*self)->redo == (vector *) NULL)
        return 0;
    if((*self)->undo != (vector *) NULL)
        vector_distroy((*self)->undo);
    (*self)->undo = (vector *)malloc(sizeof(vector));
    vector_init((*self)->undo);
    for(int i = 0 ; i < vector_getLen((*self)->arr) ; ++ i)
        vector_pushBack((*self)->undo, vector_getAt((*self)->arr, i));
    vector_distroy((*self)->arr);
    (*self)->arr = (*self)->redo;
    (*self)->redo = (vector * )NULL;
    return 1;
}

void repo__saveRepo(Repository **self) {
    if((*self)->redo != (vector *) NULL)
        vector_distroy((*self)->redo);
    (*self)->redo = (vector *)NULL;
    if((*self)->undo != (vector *) NULL)
        vector_distroy((*self)->undo);
    (*self)->undo = (vector *)malloc(sizeof(vector));
    vector_init((*self)->undo);
    for(int i = 0 ; i < vector_getLen((*self)->arr) ; ++ i)
        vector_pushBack((*self)->undo, vector_getAt((*self)->arr, i));
}
