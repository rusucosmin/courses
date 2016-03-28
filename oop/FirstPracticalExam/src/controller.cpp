#include "controller.h"

#include <fstream>
#include <algorithm>
using namespace std;

Controller::Controller(Repository &repo): _repo(repo)
{
}
bool Controller::add(Club c)
{
    if(!this->_repo.find(c)) {
        this->_repo.add(c);
        return 1;
    }
    return 0;
}

bool Controller::remove(Club c)
{
    if(this->_repo.find(c)) {
        this->_repo.remove(c);
        return 1;
    }
    return 0;
}

vector <Club> Controller::getAll()
{
    return this->_repo.getAll();
}

inline bool cmp(Club c1, Club c2) {
    return c1.getRating() > c2.getRating();
}

vector <Club> Controller::filter(string type)
{
    vector <Club> fil;
    for(auto it : this->_repo.getAll())
        if(it.getType() == type)
            fil.push_back(it);
    sort(fil.begin(), fil.end(), cmp);
    return fil;
}

void Controller::save(string filename)
{
    ofstream fout(filename);
    for(auto it: this->_repo.getAll())
        fout << it.repr() << '\n';
    fout.close();
}
