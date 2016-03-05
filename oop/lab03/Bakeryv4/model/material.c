#ifndef MATERIAL_C_INCLUDED
#define MATERIAL_C_INCLUDED

#include <string.h>
#include <time.h>
#include "material.h"

void material_init(Material *self, char* name, char* supplier, float quantity, m_time expiration) {
    if(!self) {
        printf("Error: Material is NULL at creation, ABORT CREATION\n");
        return ;
    }

    self->name = (char *)malloc(sizeof(char) * (1 + strlen(name)));
    strcpy(self->name, name);
    self->name[strlen(name)] = '\0';

    self->supplier = (char *)malloc(sizeof(char) * (1 + strlen(supplier)));
    strcpy(self->supplier, supplier);
    self->supplier[strlen(supplier)] = '\0';

    self->quantity = quantity;
    self->expiration = expiration;
}

int material_cmp_quantity(Material a, Material b) {
    return material_getQuantity(&a) < material_getQuantity(&b);
}

int material_filter_expired(Material a) {
    return !material_expired(&a);
}

int material_filter_expired_and_contains_string(Material a, char *s) {
    return strstr(material_getName(&a), s) != NULL && material_expired(&a);
}

int material_filter_supplier_and_bound_quantity(Material a, char *s, float bound) {
    return strcmp(material_getSupplier(&a), s) == 0 && material_getQuantity(&a) <= bound;
}

void material_destroy(Material *self) {
    if(!self) {
        printf("Error - Material is NULL at destroy! ABORT DESTROY!\n");
        return ;
    }
    free(self->name);
    self->name = NULL;

    free(self->supplier);
    self->supplier = NULL;

    self->quantity = -1;
}

char* material_getName(Material* self) {
    return self->name;
}

char* material_getSupplier(Material* self) {
    return self->supplier;
}

float material_getQuantity(Material *self) {
    return self->quantity;
}

m_time material_getExpiration(Material *self) {
    return self->expiration;
}

int material_equal(Material *a, Material *b) {
    if(strcmp(a->name, b->name) == 0)
        return 1;
    return 0;
}

int material_expired(Material *a) {
    time_t raw_time;
    m_time tmp;
    time ( &raw_time );
    tmp = *gmtime ( &raw_time );
    time_t start_time, end_time;
    double seconds;

    m_time exp = a->expiration;

    exp.tm_hour = 0;
    exp.tm_min = 0;
    exp.tm_sec = 0;
    exp.tm_year -= 1900;
    exp.tm_mon -= 1;

    tmp.tm_hour = 0;
    tmp.tm_min = 0;
    tmp.tm_sec = 0;

    start_time = mktime(&exp);
    end_time = mktime(&tmp);

    seconds = difftime(start_time, end_time);

    if(seconds < 0)
        return 1;
    return 0;
}

#endif // MATERIAL_C_INCLUDED
