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

#endif // REPOSITORY_H
