#ifndef VECTOR_H_INCLUDED
#define VECTOR_H_INCLUDED

#include "../model/material.h"

/**
    My own implementation of a dynamically allocated array.
    The idea is that, when the array reaches it's capacity, we double its size,
        reallocate another memory and copy the content to that memory.
*/

typedef struct {
    Material *arr;
    int len, capacity;
} vector;

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
void vector_setAt(vector *self, int i, Material m);
Material vector_getAt(vector *self, int pos);

void vector_sort(vector *self, int (*cmp)(Material a, Material b), int reversed);

#endif // VECTOR_H_INCLUDED
