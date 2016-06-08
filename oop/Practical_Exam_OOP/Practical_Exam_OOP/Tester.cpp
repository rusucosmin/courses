#include "Tester.h"
#include <Exception.h>
#include <cassert>
#include <Repository.h>
#include <Programmer.h>
#include <Task.h>
#include <qmessagebox.h>
#include <Controller.h>
#include <qstring.h>
using namespace std;


Tester::Tester()
{
	/*
add,done,3
find,in progress,1
start,open
update,done,2
	*/
	Repository *r = new Repository("Text.txt");
	Controller *c = new Controller(r);
	//for (auto it : c->getTasks())
	//	QMessageBox::critical(Q_NULLPTR, "titlu", QString::fromStdString(it.toString()), QMessageBox::Ok, QMessageBox::Ok);
	assert(c->getTasks()[0] == Task("add", "done", 3));
	assert(c->getTasks()[1] == Task("update", "done", 2));
	assert(c->getTasks()[2] == Task("find", "in progress", 1));
	assert(c->getTasks()[3] == Task("start", "open", -1));

	c->addTask(Task("undo", "open", -1));
	assert(c->getTasks()[0] == Task("add", "done", 3));
	assert(c->getTasks()[1] == Task("update", "done", 2));
	assert(c->getTasks()[2] == Task("find", "in progress", 1));
	assert(c->getTasks()[3] == Task("start", "open", -1));
	assert(c->getTasks()[4] == Task("undo", "open", -1));

	c->remove(Task("add", "done", 3));

	assert(c->getTasks()[0] == Task("update", "done", 2));
	assert(c->getTasks()[1] == Task("find", "in progress", 1));
	assert(c->getTasks()[2] == Task("start", "open", -1));
	assert(c->getTasks()[3] == Task("undo", "open", -1));

	try {
		c->doneTask(Task("find", "in progress", 1), Programmer("Andra Pop", 3));
		assert(false); /// shit
	}
	catch (Exception &e) {
		;
	}

	c->doneTask(Task("find", "in progress", 1), Programmer("Rusu Cosmin", 1));
	assert(c->getTasks()[0] == Task("find", "done", 1));
	assert(c->getTasks()[1] == Task("update", "done", 2));
	assert(c->getTasks()[2] == Task("start", "open", -1));
	assert(c->getTasks()[3] == Task("undo", "open", -1));

	c->startTask(Task("start", "open", -1), Programmer("Rusu Cosmin", 1));
	assert(c->getTasks()[0] == Task("find", "done", 1));
	assert(c->getTasks()[1] == Task("update", "done", 2));
	assert(c->getTasks()[2] == Task("start", "in progress", 1));
	assert(c->getTasks()[3] == Task("undo", "open", -1));

	delete c;
	delete r;
}


Tester::~Tester()
{
}
