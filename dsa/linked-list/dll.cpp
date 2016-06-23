#include <iostream>

using namespace std;

template <class T>
class DLL {
struct Node {
    T key;
    Node *next, *prev;
    Node(): key(NULL), next(NULL), prev(NULL) {}
    Node(T _key, Node *_prev, Node *_next): key(_key), next(_next), prev(_prev) {}
};
public:
class iterator {
private:
    Node *act;
public:
    iterator(): act(NULL) {}
    iterator(Node *_act): act(_act) {
    }
    iterator& operator ++ () {
        act = act->next;
        return *this;
    }
    T& operator *() {
        return act->key;
    }
    iterator& operator -- () {
        act = act->prev;
        return *this;
    }
    inline bool operator == (const iterator &other) const {
        return act == other.act;
    }
    inline bool operator != (const iterator &other) const {
        return act != other.act;
    }
    inline bool isValid() {
       return act != NULL;
    }
};
private:
    Node *head, *tail;
    int cnt;
public:
    DLL() {
        head = tail = NULL;
    }
    iterator begin() {
        return iterator(head);
    }
    iterator end() {
        return NULL;
    }
    void insertFront(T key) {
        if(!remove(key))
            ++ cnt;
        Node *act = new Node(key, NULL, NULL);
        if(head == NULL) {
            head = tail = act;
            return ;
        }
        act->next = head;
        head->prev = act;
        head = act;
    }
    void insertBack(T key) {
        if(!remove(key))
            ++ cnt;
        Node *act = new Node(key, NULL, NULL);
        if(head == NULL) {
            head = tail = act;
            return ;
        }
        tail->next = act;
        act->prev = tail;
        tail = act;
    }
    inline bool remove(T key) {
        Node *act = head;
        while(act) {
            if(act->key == key) {
                if(act->prev == NULL) { // then act is head
                    head = act->next;
                    if(!head)
                        head = tail = NULL;
                }
                else {
                    act->prev->next = act->next;
                    if(act->next == NULL) // then act is tail
                        tail = act->prev;
                    if(!tail)
                        head = tail = NULL;
                }
                delete act;
                return 1;
            }
            act = act->next;
        }
        return 0;
    }
    inline int size() {
        return cnt;
    }
    inline bool isEmpty() {
        return head == tail == NULL;
    }
    inline void print() {
        cerr << "list contains:\n";
        for(iterator it = this->begin(); it != this->end(); ++ it) {
            cerr << *it << ' ';
        }
        cerr << '\n';
    }
};

int main() {
    DLL <int> l;
    l.insertBack(3);
    l.insertFront(2);
    l.insertBack(4);
    l.insertFront(1);
    l.insertBack(5);
    l.print();
    l.insertBack(1);
    l.print();
    l.insertFront(1);

    DLL <int> v;
    v.insertBack(1);
    v.print();
    v.insertBack(1);
    v.print();
    v.insertFront(1);
    v.insertBack(2);
    v.insertFront(3);
    v.print();
}
