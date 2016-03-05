#ifndef REPOSITORY_H_INCLUDED
#define REPOSITORY_H_INCLUDED

#include "../utils/vector.h"

/**
    Structure Repository:
        Contains an array of Medication, simulates a database of Medications
*/

typedef struct {
    vector *undo;
    vector *redo;
    vector *arr;
} Repository;

///Constructors and destructors
void repo_init(Repository *self);
void repo_destroy(Repository *self);

///Public
/// Method to return all the material in the repository (Some kind of `SELECT * FROM MATERIALS`)
vector *repo_getMaterials(Repository *self);
/// Method to add a Material to the repository
void repo_addMaterial(Repository *self, Material m);
/// Method to delete a Material from the repository
void repo_deleteMaterial(Repository *self, Material m);
/// Method to update the Material from the repository
void repo_updateMaterial(Repository *self, Material m);
/**
    Method to find the Material of the repository
    Returns 1 if the Material was found
            0 otherwise
*/
int repo_findMaterial(Repository *self, Material m);
/**
    Method for the Undo feature
    Returns 1 if Undo was done
            0 if it cannot be done
*/
int repo_undo(Repository ** self);
/**
    Method for the Redo feature
    Returns 1 if Redo was done
            0 if it cannot be don
*/
int repo_redo(Repository ** self);

/// private
/**
    Method to prepare the Undo and Redo feature. It makes a deep copy of the Repository
*/
void repo__saveRepo(Repository ** self);

#endif // REPOSITORY_H_INCLUDED
