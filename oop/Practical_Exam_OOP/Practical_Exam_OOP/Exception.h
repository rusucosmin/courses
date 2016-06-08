#pragma once
#include <exception>
#include <string>

using namespace std;

class Exception :
	public exception
{
public:
	Exception(string);
	~Exception();
	const char * what() { return str.c_str(); }
private:
	string str;
};

