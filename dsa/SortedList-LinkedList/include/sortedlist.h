#ifndef SORTEDLIST_H
#define SORTEDLIST_H

using namespace std;


template <class T>
class SortedList {
public:
    struct Node {
        T data;
        Node* next;
        Node(const T& value = 0, Node* nxt = NULL): next(nxt), data(value) {};
    };
    class iterator {
    public:
        iterator(Node* head = NULL): act(head) {}
        bool isValid() { return act == NULL; }
        iterator operator ++() { Node* p = act ; act = act->next; return *this; }
        iterator operator ++(int junk) { act = act->next; return *this; }
        T& operator *() { return act->data; }
        Node* operator->() { return act; }
        Node* getCurrent() { return act; };
        iterator operator = (const Node* head) { act = head; return *this; }
        bool operator==(const iterator& rhs) { return act == rhs.act; }
        bool operator!=(const iterator& rhs) { return act != rhs.act; }
    private:
        Node* act;
    };
    SortedList(): head(NULL) {};
    ~SortedList() {
        clear();
    }
    iterator begin() { return iterator(head); }
    iterator end() { return NULL; }
    void clear() {
        Node *prev = NULL;
        while(head != NULL) {
            prev = head;
            head = head->next;
            delete prev;
        }
        head = NULL;
    }
    int count(const T& value) const {
        int cnt = 0;
        Node* act = head;
        while(act) {
            cnt += act->data == value;
            act = act->next;
        }
        return cnt;
    }
    bool empty() const {
        return head == NULL;
    }
    void insert(const T& value) {
        Node* act = head;
        Node* newNode = new Node(value);
        if(act == NULL || act->data >= value) {
            newNode->next = head;
            head = newNode;
            return ;
        }
        while(act->next != NULL && act->next->data < value)
            act = act->next;
        newNode->next = act->next;
        act->next = newNode;
    }
    void remove(const T& value) {
        Node* act = head;
        while(act != NULL && act->data == value)
            act = act->next;
        head = act;
        if(act == NULL)
            return ;
        while(act->next != NULL) {
            if(act->next->data == value) {
                delete act->next;
                act->next = act->next->next;
            }
            else
                act = act->next;
        }
    }
    void remove(iterator it) {
        iterator prev = NULL, act = begin();
        if(act == it) {
            Node *aux = head;
            head = head->next;
            delete aux;
            return ;
        }
        while(act->next != NULL) {
            prev = act;
            act = iterator(act->next);
            if(act == it) {
                prev->next = act->next;
                delete act.getCurrent();
                return;
            }
        }
    }
    void remove_after(iterator& it) {
        it->next = it->next->next;
    }
    iterator find(const T& value) {
        Node* act = head;
        while(act != NULL && act->data != value)
            act = act->next;
        return iterator(act);
    }
    int size() const {
        int cnt = 0;
        for(iterator it = begin() ; it != end() ; ++ it)
            cnt ++;
        return cnt;
    }
private:
    Node* head;
};
#endif // SORTEDLIST_H
