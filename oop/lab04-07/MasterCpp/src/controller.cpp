#include "controller.h"
#include <repository.h>
#include <iostream>

Controller::Controller(Repository &repo): _repo(repo) {
}

bool Controller::addTutorial(Tutorial t) {
    if(this->findTutorial(t))
        return false;
    this->_repo.addTutorial(t);
    return true;
}

bool Controller::removeTutorial(Tutorial t) {
    if(this->findTutorial(t) == false)
        return false;
    this->_repo.removeTutorial(t);
    return true;
}

bool Controller::updateTutorial(Tutorial t) {
    if(this->findTutorial(t) == false)
        return false;
    this->_repo.updateTutorial(t);
    return true;
}

bool Controller::findTutorial(Tutorial t) {
    vector <Tutorial> &all = this->_repo.getAll();
    for(auto it : all)
        if(it == t)
            return true;
    return false;
}

vector <Tutorial> & Controller::getAll() {
    return this->_repo.getAll();
}

void Controller::saveToFile(string fileName) {
    this->_repo.saveToFile(fileName);
}
