#include "controller.h"
#include <repository.h>
#include <iostream>

Controller::Controller(Repository &repo, Repository &watchList): _repo(repo), _watchList(watchList) {
}

bool Controller::addTutorial(Tutorial t) {
    if(this->_repo.findTutorial(t))
        return false;
    this->_repo.addTutorial(t);
    return true;
}

bool Controller::removeTutorial(Tutorial t) {
    if(this->_repo.findTutorial(t) == false)
        return false;
    this->_repo.removeTutorial(t);
    return true;
}

bool Controller::updateTutorial(Tutorial t) {
    if(this->_repo.findTutorial(t) == false)
        return false;
    this->_repo.updateTutorial(t);
    return true;
}

/*
bool Controller::findTutorial(Tutorial t) {
    DynamicVector <Tutorial> &all = this->_repo.getAll();
    for(int i = 0 ; i < all.size() ; ++ i)
        if(all[i] == t)
            return true;
    return false;
}*/

DynamicVector <Tutorial> & Controller::getAll() {
    return this->_repo.getAll();
}

void Controller::saveToFile(string fileName) {
    this->_repo.saveToFile(fileName);
}

void Controller::filterActive(string presenter) {
    DynamicVector <Tutorial> all = this->_repo.getAll();
    this->_active.clear();
    this->_pos = 0;
    for(int i = 0 ; i < all.size() ; ++ i) {
        if(presenter == "*")
            this->_active.push_back(all[i]);
        else
            if(all[i].getPresenter() == presenter)
                this->_active.push_back(all[i]);
    }
}

DynamicVector <Tutorial> Controller::getActiveList() {
    return this->_active;
}

Tutorial Controller::getActiveTutorial() {
    return this->_active[this->_pos];
}

void Controller::nextTutorial() {
    ++ _pos;
    if(_pos == this->_active.size())
        _pos = 0;
}

bool Controller::addToWatch(Tutorial t) {
    if(this->_watchList.findTutorial(t))
        return 0;
    this->_watchList.addTutorial(t);
    return 1;
}

bool Controller::removeFromWatch(Tutorial t) {
    if(!this->_watchList.findTutorial(t))
        return 0;
    this->_watchList.removeTutorial(t);
    return 1;
}

void Controller::rate(Tutorial t) {
    DynamicVector <Tutorial> v = this->_repo.getAll();
    for(int i = 0 ; i < v.size() ; ++ i)
        if(v[i] == t)
            v[i].setLikes(v[i].getLikes() + 1);
    v = this->_watchList.getAll();
    for(int i = 0 ; i < v.size() ; ++ i)
        if(v[i] == t)
            v[i].setLikes(v[i].getLikes() + 1);
        v = this->_watchList.getAll();
    v = _active;
    for(int i = 0 ; i < v.size() ; ++ i)
        if(v[i] == t)
            v[i].setLikes(v[i].getLikes() + 1);
}
DynamicVector <Tutorial> & Controller::getWatchList() {
    return this->_watchList.getAll();
}



