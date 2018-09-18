#include <assert.h>
#include "../model/material.h"
#include "../controller/controller.h"
#include "../repository/repository.h"

void test_material() {
    Material m;
    m_time exp;
    exp.tm_year = 2016;
    exp.tm_mday = 15;
    exp.tm_mon = 3;
    material_init(&m, "faina", "romania", (float)12.05, exp);
    assert(strcmp(material_getName(&m), "faina") == 0);
    assert(strcmp(material_getSupplier(&m), "romania") == 0);
    assert(material_getQuantity(&m) == (float)12.05);
    assert(material_getExpiration(&m).tm_year == 2016);
    assert(material_getExpiration(&m).tm_mday == 15);
    assert(material_getExpiration(&m).tm_mon == 3);
}

Material doMaterial(char *name, char *supplier, float quantity, int year, int mon, int day) {
    Material m;
    m_time exp;
    exp.tm_year = year;
    exp.tm_mon = mon;
    exp.tm_mday = day;
    material_init(&m, name, supplier, quantity, exp);
    return m;
}

int test_equal(Material a, Material b) {
    return strcmp(a.name, b.name) == 0 && strcmp(a.supplier, b.supplier) == 0
    && a.quantity == b.quantity && a.expiration.tm_year == b.expiration.tm_year
    && a.expiration.tm_mday == b.expiration.tm_mday && a.expiration.tm_mon == b.expiration.tm_mon;
}

void test_repository() {
    Repository *repo = (Repository *) malloc(sizeof(Repository));
    repo_init(repo);
    repo_initFromFile(repo, "test.db");
    vector *arr = repo_getMaterials(repo);
    assert(vector_getLen(arr) == 15);
    assert(test_equal(vector_getAt(arr, 0), doMaterial("rodii", "spania", (float)10, 2016, 3, 3)));
    assert(test_equal(vector_getAt(arr, 1), doMaterial("banane", "india", (float)200, 2015, 4, 1)));
    assert(test_equal(vector_getAt(arr, 2), doMaterial("rosii", "romania", (float)200, 2016, 3, 4)));
    assert(test_equal(vector_getAt(arr, 3), doMaterial("capsuni", "spania", (float)100, 2016, 4, 1)));
    assert(test_equal(vector_getAt(arr, 4), doMaterial("masline", "italia", (float)1000, 2016, 2, 28)));
    assert(test_equal(vector_getAt(arr, 5), doMaterial("paine", "romania", (float)2, 2016, 2, 27)));
    assert(test_equal(vector_getAt(arr, 6), doMaterial("ton", "sua", (float)100, 2017, 1, 1)));
    assert(test_equal(vector_getAt(arr, 7), doMaterial("morcovi", "franta", (float)10, 2016, 12, 1)));
    assert(test_equal(vector_getAt(arr, 8), doMaterial("faina", "romania", (float)11, 2018, 12, 1)));
    assert(test_equal(vector_getAt(arr, 9), doMaterial("drojdie", "romania", (float)12, 2015, 1, 1)));
    assert(test_equal(vector_getAt(arr, 10), doMaterial("orez", "china", (float)0, 2016, 3, 7)));
    assert(test_equal(vector_getAt(arr, 11), doMaterial("unt_de_arahide", "sua", (float)2, 2016, 3, 8)));
    assert(test_equal(vector_getAt(arr, 12), doMaterial("margarina", "norvegia", (float)150, 2016, 3, 4)));
    assert(test_equal(vector_getAt(arr, 13), doMaterial("paste_fainoase", "romania", (float)2, 2016, 3, 10)));
    assert(test_equal(vector_getAt(arr, 14), doMaterial("peste_crud", "romania", (float)0, 2016, 3, 6)));
    repo_destroy(repo, "backup_test.db");
}

void test_controller() {
    Repository *repo = (Repository *) malloc(sizeof(Repository));
    repo_init(repo);
    Controller *ctrl = (Controller *) malloc(sizeof(Controller));
    controller_init(ctrl, repo);
    controller_addMaterial(ctrl, doMaterial("rodii", "spania", (float)10, 2016, 3, 3));
    assert(test_equal(vector_getAt(controller_getMaterials(ctrl), 0), doMaterial("rodii", "spania", (float)10, 2016, 3, 3)));
    controller_updateMaterial(ctrl, doMaterial("rodii", "testspania", (float)20, 2016, 3, 3));
    assert(test_equal(vector_getAt(controller_getMaterials(ctrl), 0), doMaterial("rodii", "testspania", (float)20, 2016, 3, 3)));
    controller_deleteMaterial(ctrl, doMaterial("rodii", "testspania", (float)20, 2016, 3, 3));
    assert(vector_getLen(controller_getMaterials(ctrl)) == 0);
    repo_destroy(repo, "backup_test.db");
}

void test(){
    test_material();
    test_repository();
    test_controller();
}
