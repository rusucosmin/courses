#include <tutorial.h>
#include <vector>

#ifndef REPOSITORY_H
#define REPOSITORY_H

class Repository {
    public:
        /** Default constructor */
        Repository(string fileName = "");
        void addTutorial(Tutorial t);
        void removeTutorial(Tutorial t);
        void updateTutorial(Tutorial t);
        //vector <Tutorial> getAll();
        vector <Tutorial>& getAll();
        void saveToFile(string fileName);

    private:
        vector <Tutorial> _list;
};

vector <Tutorial> operator + (const vector <Tutorial> &a, const Tutorial &b);
vector <Tutorial> operator + (const Tutorial &b, const vector <Tutorial> &a);
vector <Tutorial> operator - (const vector <Tutorial> &a, const Tutorial &b);
#endif // REPOSITORY_H
