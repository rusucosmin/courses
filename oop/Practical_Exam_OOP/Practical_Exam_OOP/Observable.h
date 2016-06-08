#pragma once
#include <Observer.h>
#include <vector>
using namespace std;
class Observable
{
public:
	Observable();
	void attach(Observer *_o) {
		o.push_back(_o);
	}
	void notify() {
		for (auto it : o)
			it->update();
	}
	~Observable();
private:
	vector <Observer *> o;
};

