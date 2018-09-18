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
    this->_list = this->_list + t;
}

void Repository::removeTutorial(Tutorial t) {
    this->_list = this->_list - t;
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
    for(int i = 0 ; i < this->_list.size() ; ++ i) {
        Tutorial it = this->_list[i];
        fout << it.getTitle() + "|" +
                it.getPresenter() + "|" +
                it.getLink() + "|" +
                to_string(it.getDuration()) + "|" +
                to_string(it.getLikes()) << '\n';
    }

}

vector <Tutorial> operator + (const vector <Tutorial> &a, const Tutorial &b) {
    vector <Tutorial> ret = a;
    ret.push_back(b);
    return ret;
}

vector <Tutorial> operator + (const Tutorial &b, const vector <Tutorial> &a) {
    vector <Tutorial> ret = a;
    ret.push_back(b);
    return ret;
}

vector <Tutorial> operator - (const vector <Tutorial> &a, const Tutorial &b) {
    vector <Tutorial> ret = a;
    //ret.remove(b);
    ret.erase(remove(ret.begin(), ret.end(), b), ret.end());
    return ret;
}

bool Repository::findTutorial(Tutorial t) {
    for(int i = 0 ; i < _list.size() ; ++ i)
        if(_list[i] == t)
            return 1;
    return 0;
}

