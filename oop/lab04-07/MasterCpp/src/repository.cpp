#include "repository.h"
#include <algorithm>
#include <fstream>
#include <cassert>
using namespace std;

Repository::Repository(string fileName) {
    ifstream fin(fileName.c_str());
    string line;
    while(getline(fin, line) && line != "") {
        this->addTutorial(Tutorial::fromString(line));
    }
    fin.close();
}

void Repository::addTutorial(Tutorial t) {
    this->_list.push_back(t);
}

void Repository::removeTutorial(Tutorial t) {
    this->_list.erase(remove(this->_list.begin(), this->_list.end(), t), this->_list.end());
}

void Repository::updateTutorial(Tutorial t) {
    for(unsigned int i = 0 ; i < this->_list.size() ; ++ i)
        if(this->_list[i] == t)
            this->_list[i] = t;
}

vector<Tutorial> &Repository::getAll() {
    return this->_list;
}
void Repository::saveToFile(string fileName) {
    ofstream fout(fileName.c_str());
    for(auto it : this->_list)
        fout << it.getTitle() + "|" +
                it.getPresenter() + "|" +
                it.getLink() + "|" +
                to_string(it.getDuration()) + "|" +
                to_string(it.getLikes()) << '\n';

}
