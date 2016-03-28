#include "repository.h"

#include <fstream>
#include <vector>
#include <iostream>
#include <club.h>
#include <algorithm>

using namespace std;

Repository::Repository(string filename = "")
{
    //ctor
    if(filename != "") {
        ifstream fin(filename);
        string line;
        while(getline(fin, line)) {
            vector <string> v;
            v.push_back("");
            for(int i = 0 ; i < line.size() ; ++ i) {
                if(line[i] != '|')
                    v.back() += line[i];
                else
                    v.push_back("");
            }
            int rating = 0;
            for(int i = 0 ; i < v[2].size() ; ++ i)
                rating = rating * 10 + v[2][i] - '0';
            this->add(Club(v[0], v[1], rating));
        }
    }
}
void Repository::add(Club c)
{
    this->arr.push_back(c);
}

void Repository::remove(Club c)
{
    arr.erase(std::remove(arr.begin(), arr.end(), c), arr.end());
}

bool Repository::find(Club c)
{
    for(auto it : arr)
        if(it == c)
            return 1;
    return 0;
}

vector <Club> Repository::getAll()
{
    return arr;
}
