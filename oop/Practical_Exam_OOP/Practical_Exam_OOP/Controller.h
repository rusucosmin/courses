#pragma once
#include <Repository.h>
#include <Exception.h>
class Controller
{
public:
	Controller(Repository *_r);
	~Controller();
	inline void addTask(Task act) {
		r->addTask(act);
	}
	void remove(Task act) {
		r->removeTask(act);
	}
	inline Programmer getProgrammer(int id) {
		for (auto it : r->getProgrammers())
			if (it.getId() == id)
				return it;
		return Programmer("", -1);
	}
	void startTask(Task act, Programmer p) {
		if (act.getStatus() != "open")
			throw Exception("Task is already taken!");
		act.setStatus("in progress");
		act.setProg(p.getId());
		update(act);
	}
	void doneTask(Task act, Programmer p) {
		if (act.getStatus() != "in progress")
			throw Exception("Task is not in progress!");
		if (act.getProg() != p.getId())
			throw Exception("Task is not yours!");
		act.setStatus("done");
		update(act);
	}
	void update(Task act) {
		r->updateTask(act);
	}
	inline vector <Task> getTasks() {
		return r->getTask();
	}
	Repository *r;
};

