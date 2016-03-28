#ifndef REPOSITORY_H
#define REPOSITORY_H

#include <string>
#include <club.h>
#include <vector>

using namespace std;

class Repository
{
    public:
        /** Default constructor */
        Repository(string filename);
        /**
            Method to add a club to the repository.
            Appends the club c to the end of the vector
            which stores all the clubs.
            It works on the precondition that the club
            does not exist. (from the controller)
        */
        void add(Club c);
        void remove(Club c);
        bool find(Club c);
        vector <Club> getAll();
    private:
        vector <Club> arr;
};

#endif // REPOSITORY_H
