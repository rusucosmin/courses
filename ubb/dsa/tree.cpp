#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

template <class T>
class Tree {
public:
    class Node {
    public:
        vector <Node*> childs;
        T key;
        Node (): key(NULL) { childs.clear(); }
        Node (T _key): key(_key) { childs.clear(); }
    };
    class iterator {
    public:
        iterator(): act(NULL) {}
        iterator(iterator &it): act(it.act) {}
    private:
        friend class Tree;
        Node *act;
    };
    Tree(): root(NULL) {}
    Tree(Node *_root): root(_root) {}
    void add(iterator it, T key) {
        Node *current = new Node(key);
        current->p = it.act;
        it.act->childs.push_back(current);
    }
    Node *root;
};

int main() {
}
