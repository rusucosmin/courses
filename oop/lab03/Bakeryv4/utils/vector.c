#ifndef VECTOR_C_INCLUDED
#define VECTOR_C_INCLUDED

#include "vector.h"
#define VECTOR_INITIAL_CAPACITY 10

/// constructor & destructor
void vector_init(vector *self) {
    vector__setLen(self, 0);
    vector__setCapacity(self, VECTOR_INITIAL_CAPACITY);

    self->arr = (Material *) malloc(self->capacity * sizeof(Material));
}

void vector_distroy(vector *self) {
    vector__setLen(self, 0);
    vector__setCapacity(self, 0);

    /// Now, free the vector
    free(self->arr);
    self->arr = NULL;
}

/// private
void vector__incLen(vector *self) {
    self->len++;
}
void vector__setLen(vector *self, int len){
    self->len = len;
}

int vector__getCapacity(vector *self) {
    return self->capacity;
}

void vector__setCapacity(vector *self, int capacity) {
    self->capacity = capacity;
}

/// public
void vector_pushBack(vector *self, Material m) {
    if(vector__getCapacity(self) == vector_getLen(self))
    {
        vector__setCapacity(self, vector__getCapacity(self) * 2);
        self->arr = realloc(self->arr, self->capacity * sizeof(Material));
    }
    self->arr[self->len] = m;
    vector__incLen(self);
}

void vector_removeAt(vector *self, int pos) {
    int len = vector_getLen(self);

    if(pos > len - 1) {
        printf("Error: Attempt to remove from invalid position. Vector len (%d) at position: %d!\n", len, pos);
        return ;
    }
    int i;
    for(i = pos ; i < len - 1 ; ++ i)
        self->arr[i] = self->arr[i + 1];

    self->arr[i] = NULL_MATERIAL;
    vector__setLen(self, len - 1);
}

int vector_getLen(vector *self){
    return self->len;
}

Material vector_getAt(vector *self, int pos){
    int len = vector_getLen(self);
    if(pos > len - 1) {
        printf("Error: Attemt to acces invalit position. Vector size %d, position %d!\n", len, pos);
        return NULL_MATERIAL;;
    }
    return self->arr[pos];
}


void vector_setAt(vector *self, int pos, Material m) {
    int len = vector_getLen(self);
    if(pos > len - 1) {
        printf("Error: Attemt to acces invalit position. Vector size %d, position %d!\n", len, pos);
        return NULL_MATERIAL;;
    }
    self->arr[pos] = m;
}



#endif // VECTOR_C_INCLUDED
