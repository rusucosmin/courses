#ifndef REPOSITORY_H
#define REPOSITORY_H

#include <tutorial.h>
#include <vector>
#include <dynamicvector.h>

class Repository {
    public:
        /** Default constructor */
        Repository(string fileName = "");
        void addTutorial(Tutorial t);
        void removeTutorial(Tutorial t);
        void updateTutorial(Tutorial t);
        //vector <Tutorial> getAll();
        DynamicVector <Tutorial>& getAll();
        void saveToFile(string fileName);

    private:
        DynamicVector <Tutorial> _list;
};

DynamicVector <Tutorial> operator + (const DynamicVector <Tutorial> &a, const Tutorial &b);
DynamicVector <Tutorial> operator + (const Tutorial &b, const DynamicVector <Tutorial> &a);
DynamicVector <Tutorial> operator - (const DynamicVector <Tutorial> &a, const Tutorial &b);
#endif // REPOSITORY_H
