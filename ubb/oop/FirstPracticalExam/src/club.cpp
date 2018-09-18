#include "club.h"

Club::Club(string name, string type, int rating)
{
    //ctor
    this->name = name;
    this->type = type;
    this->rating = rating;
}

string Club::getName()
{
    return this->name;
}

string Club::getType()
{
    return this->type;
}

int Club::getRating()
{
    return this->rating;
}

bool Club::operator == (const Club& other)
{
    return this->name == other.getName();
}
string Club::repr()
{
    return this->name + "|" + this->type + "|" + to_string(this->rating);
}
string Club::reprHuman()
{
    return this->name + " " + this->type + " " + to_string(this->rating);
}

