#ifndef VECTOR_H_INCLUDED
#define VECTOR_H_INCLUDED

#include "../model/material.h"


typedef struct {
    Material *arr;
    int len, capacity;
} vector;

/// emptyStruct

/// constructor & destructor
void vector_init(vector *self);
void vector_distroy(vector *self);

/// private
void vector__incLen(vector *self);
void vector__setLen(vector *self, int len);
int vector__getCapacity(vector *self);
void vector__setCapacity(vector *self, int capacity);

/// public
void vector_pushBack(vector *self, Material m);
void vector_removeAt(vector *self, int pos);
int vector_getLen(vector *self);
Material vector_getAt(vector *self, int pos);

#endif // VECTOR_H_INCLUDED
