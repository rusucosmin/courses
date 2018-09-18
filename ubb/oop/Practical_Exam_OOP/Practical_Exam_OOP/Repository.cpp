#include "Repository.h"
#include <sstream>
#include <fstream>
#include <algorithm>

Repository::Repository(string filename)
{
	readFromFile(filename);
}

Repository::~Repository()
{
	writeToFile();
}

void Repository::addTask(Task act) {
	t.push_back(act);
	sortData();
	notify();
}

void Repository::removeTask(Task act) {
	vector <Task> newt;
	for (auto it : t)
		if (it.getDesc() != act.getDesc())
			newt.push_back(it);
	t = newt;
	sortData();
	notify();
}

void Repository::updateTask(Task act) {
	for (int i = 0; i < t.size(); ++i)
		if (t[i].getDesc() == act.getDesc())
			t[i] = act;
	sortData();
	notify();
}

void Repository::readFromFile(string filename) {
	ifstream fin("programmers.in");
	string line;
	while (getline(fin, line)) {
		stringstream get(line);
		vector <string> all;
		string act;
		while(getline(get, act, ',')) {
			all.push_back(act);
		}
		p.push_back(Programmer(all[0], stoi(all[1])));
	}
	fin.close();
	fin.open(filename);
	while (getline(fin, line)) {
		stringstream get(line);
		vector <string> all;
		string act;
		while (getline(get, act, ',')) {
			all.push_back(act);
		}
		if (all.size() < 3)
			all.push_back("-1");
		t.push_back(Task(all[0], all[1], stoi(all[2])));
	}
	sortData();
}

void Repository::writeToFile() {
	ofstream fout("tasks_.in");
	for (auto it : t)
		fout << it.toString() << '\n';
}

void Repository::sortData() {
	sort(t.begin(), t.end(), [](const Task &a, const Task &b) {
		return a.getStatus() < b.getStatus() || (a.getStatus() == b.getStatus() && a.getDesc() < b.getDesc());
	});
}