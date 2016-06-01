#ifndef SORTEDLISTBST_H
#define SORTEDLISTBST_H

#include <iostream>
#include <tester.h>
#include <abstractsortedlist.h>

template <class Object>
class SortedListBST : public AbstractSortedList <Object> {
public:
    /** Default constructor */
    SortedListBST();
    /** Destructor */
    ~SortedListBST();
    /** Get the 'data' at Index in BST */
    Object getAtIndex(const int& Index);
    /** Add into the BST sorted ascending */
    void add(const Object& Data);
    /** Remove the 'data' at Index in BST (actually it removes the element at position Index in a sorted list of element) */
    void removeAtIndex(const int& Index);
    /** Check if BST contains 'Data' */
    bool contains(const Object& Data);
    /** Clear BST */
    void clear();
    /** Return BST node count */
    int size();

protected:

private:
    friend class Tester;
    class BSTNode {
    private:
        friend class SortedListBST;
        BSTNode *_father, *_left, *_right;
        Object _data;
        int _cnt;
    public:
        /**Constructors**/
        BSTNode(): _father(NULL), _left(NULL), _right(NULL), _data(NULL), _cnt(0) {}
        BSTNode(BSTNode *father, BSTNode *left, BSTNode *right, Object data, int cnt = 0): _father(father), _left(left), _right(right), _data(data), _cnt(cnt) {}
    };
    /** Adds an object to the BST **/
    void _add(BSTNode *&act, BSTNode *dad, const Object& Data);
    /** Finds an object in the BST **/
    bool _find(BSTNode *act, const Object& Data);
    /** Returns the object at index 'Index' if the BST would be linearized (and sorted) **/
    Object _findIndex(BSTNode *act, const int &Index);
    /** Remove a node **/
    void _remove(BSTNode *&act);
    /** Free a node **/
    void _free(BSTNode *&act);
    /** DFS auxiliary function to print the tree **/
    void _dfs(BSTNode *node);
    /** Function to get the succesor of a BST**/
    BSTNode* _getSuc(BSTNode *node);
    /** Auxiliary function to update the size of a node: the number of nodes in it's subtree**/
    void update_sz(BSTNode *&node);
    /** Function to erase the element at index 'Index'**/
    void _erase(BSTNode *&node, const int& Index);
    /** Function to erase the element with value 'Value'**/
    void _erase_value(BSTNode *&node, const Object& Value);
    /** The root of the Tree **/
    BSTNode *_root;
    /** Number of elements (not neccesarry since we have root->cnt, but still..**/
    int _size;
};

/**
    Default constructor
    @PRECOND: None
    @POSTCOND:
        root = NULL
        count = 0
*/
template<class T>
SortedListBST<T>::SortedListBST() {
    _root = NULL;
    _size = 0;
}

template<typename T>
typename SortedListBST<T>::BSTNode* SortedListBST<T>::_getSuc(BSTNode *node) {
    assert(node != NULL);
    BSTNode *prec;
    if(node->_right) {
        prec = node->_right;
        while(prec->_left)
            prec = prec->_left;
        return prec;
    }
    prec = node;
    while(prec->_father && prec->_father->_right == prec)
        prec = prec->_father;
    return prec->_father;
}

template<class T>
SortedListBST<T>::~SortedListBST() {
    free(_root);
    _size = 0;
}

template<class T>
T SortedListBST<T>::getAtIndex(const int& Index) {
    assert(0 <= Index && Index < _size);
    return _findIndex(_root, Index);
}

template<class T>
void SortedListBST<T>::add(const T& Data) {
    _add(_root, NULL, Data);
    this->_size ++;
}

template<class T>
void SortedListBST<T> ::_erase(BSTNode *&node, const int& Index) {
    assert(node != NULL);
    int pos = 0;
    if(node->_left)
        pos += node->_left->_cnt;
    if(pos == Index) {
        _remove(node);
        return ;
    }
    else if(pos > Index)
        _erase(node->_left, Index);
    else
        _erase(node->_right, Index - pos - 1);
    update_sz(node->_left);
    update_sz(node->_right);
    update_sz(node);
}

template<class T>
void SortedListBST<T> ::_erase_value(BSTNode *&node, const T& value) {
    assert(node != NULL);
    if(node->_data == value) {
        _remove(node);
        return ;
    }
    else if(node->_data > value)
        _erase_value(node->_left, value);
    else
        _erase_value(node->_right, value);
    update_sz(node->_left);
    update_sz(node->_right);
    update_sz(node);
}

template<class T>
void SortedListBST<T> :: _remove(BSTNode *&node) {
    if(node->_left == NULL && node->_right == NULL) {
        delete node;
        node = NULL;
    }
    else if(node->_right == NULL) { /// only _left
        BSTNode *aux = node;
        node = node->_left;
        delete aux;
    }
    else if(node->_left == NULL) {
        BSTNode *aux = node;
        node = node->_right;
        delete aux;
    }
    else {
        BSTNode *aux = _getSuc(node);
        node->_data = aux->_data;
        _erase_value(node->_right, aux->_data);
    }
}

template<class T>
void SortedListBST<T> :: update_sz(BSTNode *&node) {
    if(!node)
        return ;
    node->_cnt = 1;
    if(node->_left)
        node->_cnt += node->_left->_cnt;
    if(node->_right)
        node->_cnt += node->_right -> _cnt;
}

template<class T>
void SortedListBST<T> ::_add(BSTNode *&node, BSTNode *dad, const T& Data) {
    if(node == NULL) {
        node = new BSTNode(dad, NULL, NULL, Data, 1);
        return ;
    }
    if(node->_data > Data)
        _add(node->_left, node, Data);
    else
        _add(node->_right, node, Data);
    node->_cnt = 1;
    if(node->_left)
        node->_cnt += node->_left->_cnt;
    if(node->_right)
        node->_cnt += node->_right->_cnt;
}

template<class T>
void SortedListBST<T> ::_dfs(BSTNode *node) {
    if(node == NULL)
        return;
    std::cerr << "Node: " << node->_data << ' ' << node->_cnt << ' ';
    if(node->_left)
        std::cerr << "Left: " << node->_left->_data << ' ' << node->_left->_cnt << ' ';
    if(node->_right)
        std::cerr << "Right: " << node->_right->_data << ' ' << node->_right->_cnt << ' ';
    std::cerr << '\n';
    _dfs(node->_left);
    _dfs(node->_right);
}

template<class T>
bool SortedListBST<T> ::_find(BSTNode *node, const T& Data) {
    if(node == NULL)
        return false;
    if(node->_data == Data)
        return true;
    if(node->_data > Data)
        return _find(node->_left, Data);
    else
        return _find(node->_right, Data);
}

template<class T>
T SortedListBST<T> ::_findIndex(BSTNode *node, const int& Index) {
    int pos = 0;
    if(node->_left)
        pos += node->_left->_cnt;
    if(pos == Index)
        return node->_data;
    if(pos > Index)
        return _findIndex(node->_left, Index);
    else
        return _findIndex(node->_right, Index - pos - 1);
}

template<class T>
void SortedListBST<T> ::_free(BSTNode *&node) {
    if(node == NULL)
        return ;
    free(node->_left);
    free(node->_right);
    delete node;
    node = NULL;
}
template<class T>
void SortedListBST<T>::removeAtIndex(const int& Index) {
    assert(0 <= Index && Index < _size);
    _erase(_root, Index);
    -- this->_size;
}

template<class T>
bool SortedListBST<T>::contains(const T& Data) {
    return _find(_root, Data);
}

template<class T>
void SortedListBST<T>::clear() {
    _free(_root);
    _root = NULL;
    _size = 0;
}

template<class T>
int SortedListBST<T>::size() {
    return this->_size;
}

#endif // SORTEDLISTBST_H
