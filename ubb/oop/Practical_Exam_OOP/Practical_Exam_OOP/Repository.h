#pragma once
#include <Programmer.h>
#include <Task.h>
#include <vector>
#include <Observable.h>
using namespace std;
class Repository: public Observable
{
public:
	Repository(string filename = "tasks.in");
	~Repository();
	inline vector <Programmer> getProgrammers() {
		return p;
	}
	inline vector <Task> getTask() {
		return t;
	}
	/*
		addTask(Task t): method to add a new task to the Repository
		The Task t given by a parameter is automatically added to the list of
		tasks.
		PostCond: t is in the list of tasks
	*/
	void addTask(Task t);
	/*
		removeTask(Task t): method to remove the task having the description as the one
		of the parameter t
		PostCond: t doesn't exist anymore in the repository
	*/
	void removeTask(Task t);
	/*
		updateTask(Task t): method to replace the task with the description of t
		with all the componenets of t
	*/
	void updateTask(Task t);
private:
	void readFromFile(string);
	void sortData();
	void writeToFile();
	vector <Programmer> p;
	vector <Task> t;
};

