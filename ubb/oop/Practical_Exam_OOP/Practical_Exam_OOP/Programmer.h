#pragma once
#include <string>
using namespace std;
class Programmer
{
public:
	Programmer(string _name, int _id);
	~Programmer();
	inline string getName() {
		return name;
	}
	inline int getId() {
		return id;
	}
private:
	string name;
	int id;
};

