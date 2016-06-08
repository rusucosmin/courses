#pragma once
#include <string>
using namespace std;
class Task
{
public:
	Task(string _desc, string _status, int _prog = -1);
	~Task();
	inline string getDesc() const {
		return desc;
	}
	inline string getStatus() const {
		return status;
	}
	inline int getProg() const {
		return prog;
	}
	inline void setStatus(string _status) {
		status = _status;
	}
	inline void setProg(int _prog) {
		prog = _prog;
	}
	inline string toListItem() {
		return desc + "  |  " + status;
	}
	inline string toString() {
		return desc + "," + status + "," + to_string(prog);
	}
	inline bool operator == (const Task &other) {
		return desc == other.desc && status == other.status && prog == other.prog;
	}
private:
	string desc, status;
	int prog;
};

