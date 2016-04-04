#include <repository.h>

#ifndef CONTROLLER_H
#define CONTROLLER_H


class Controller {
    public:
        /** Default constructor */
        Controller(Repository &repo, Repository &watchList);
        /** Method to add tutorial to the Repository*/
        bool addTutorial(Tutorial t);
        bool removeTutorial(Tutorial t);
        bool updateTutorial(Tutorial t);
        //bool findTutorial(Tutorial t);
        DynamicVector <Tutorial> &getAll();
        DynamicVector <Tutorial> &getWatchList();
        void saveToFile(string fileName);
        void filterActive(string presenter);
        DynamicVector <Tutorial> getActiveList();
        Tutorial getActiveTutorial();
        void nextTutorial();
        bool addToWatch(Tutorial t);
        bool removeFromWatch(Tutorial t);
        void rate(Tutorial t);

    private:
        Repository &_repo, &_watchList;
        DynamicVector <Tutorial> _active;
        int _pos;
};

#endif // CONTROLLER_H
