#include <iostream>

using namespace std;

template <class T>
class SortedList {
public:
    SortedList();
    ~SortedList();
    bool isEmpty();
    int getLength();
    void add(T newEntry);
    void remove(T anEntry);
    int retrieve(T &anEttry, bool &found);
    void clear();
private:
    static const int MAXEL = 1000;
    T data[MAXEL];
};

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
