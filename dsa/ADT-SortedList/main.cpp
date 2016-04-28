#include <iostream>

using namespace std;

template <class T>
class Node {
public:
    Node(): next(NULL) {};
    Node(T _element, Node <T>* _next = NULL): element(_element), next(_next) {};
    Node(const Node<T>& n) {
        this->element = n->element;
        this->next = n->next;
    }
private:
    T element;
    Node <T>* next;

};

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
    Node <T>* head;
    Node <T>* current;
    int length;
};

int main() {
}
