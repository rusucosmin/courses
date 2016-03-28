#ifndef CONTROLLER_H
#define CONTROLLER_H

#include <repository.h>
#include <club.h>

using namespace std;

class Controller
{
    public:
        /** Default constructor */
        Controller(Repository &repo);
        bool add(Club c);
        bool remove(Club c);
        vector <Club> getAll();
        /**
            Method to filter the clubs.
            Input: string type:
                the type of clubs we want to filter
            Output: a vector <Club> containing all
                the club whose type is TYPE,
                sorted by their rating.
            TODO: sort ascending/descending
        */
        vector <Club> filter(string type);
        void save(string filename);

    private:
        Repository _repo;
};

#endif // CONTROLLER_H
