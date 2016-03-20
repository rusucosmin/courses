#include "tutorial.h"
#include <string>
#include <vector>
using namespace std;

Tutorial::Tutorial() {
}

Tutorial::Tutorial(string title, string presenter, string link, int duration, int likes = 0) {
    this->_title = title;
    this->_presenter = presenter;
    this->_link = link;
    this->_duration = duration;
    this->_likes = likes;
}

string Tutorial::getTitle() {
    return this->_title;
}

string Tutorial::getPresenter() {
    return this->_presenter;
}

string Tutorial::getLink() {
    return this->_link;
}

int Tutorial::getDuration() {
    return this->_duration;
}

int Tutorial::getLikes() {
    return this->_likes;
}

void Tutorial::setTitle(string title) {
    this->_title = title;
}

void Tutorial::setPresenter(string presenter) {
    this->_presenter = presenter;
}

void Tutorial::setLink(string link) {
    this->_link = link;
}

void Tutorial::setDuration(int duration) {
    this->_duration = duration;
}

void Tutorial::setLikes(int likes) {
    this->_likes = likes;
}

static Tutorial Tutorial::fromString(string obj) {
    vector <string> aux;
    aux.push_back("");
    for(int i = 0 ; i < obj.size() ; ++ i) {
        if(obj[i] == '|')
            aux.push_back("");
        else
            aux.back() += obj[i];
    }
    return Tutorial(aux[0], aux[1], aux[2], stoi(aux[3]), stoi(aux[4]));
}

string Tutorial::repr() {
    return "Title: " + this->_title + "\n" +
            "Presenter: " + this->_presenter + "\n" +
            "Link: " + this->_link + "\n" +
            "Duration: " + to_string(this->_duration) + "\n" +
            "Likes: " + to_string(this->_likes) + "\n";
}
