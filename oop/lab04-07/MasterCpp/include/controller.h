#include <repository.h>

#ifndef CONTROLLER_H
#define CONTROLLER_H


class Controller {
    public:
        /** Default constructor */
        Controller(Repository &repo);
        bool addTutorial(Tutorial t);
        bool removeTutorial(Tutorial t);
        bool updateTutorial(Tutorial t);
        bool findTutorial(Tutorial t);
        vector <Tutorial> &getAll();
        void saveToFile(string fileName);
    private:
        Repository &_repo;
};

#endif // CONTROLLER_H
