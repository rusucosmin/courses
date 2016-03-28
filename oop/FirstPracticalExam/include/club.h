#ifndef CLUB_H
#define CLUB_H

#include <string>
using namespace std;

class Club
{
    public:
        /** Default constructor */
        Club(string name, string type, int rating);
        string getName();
        string getType();
        int getRating();
        string repr();
        string reprHuman();
        bool operator == (const Club &other);
    private:
        string name, type;
        int rating;
};

#endif // CLUB_H
