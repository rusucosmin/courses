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
        BSTNode(): _father(NULL), _left(NULL), _right(NULL), _data(NULL), _cnt(0) {}
        BSTNode(BSTNode *father, BSTNode *left, BSTNode *right, Object data, int cnt = 0): _father(father), _left(left), _right(right), _data(data), _cnt(cnt) {}
    };
    void _add(BSTNode *&act, BSTNode *dad, const Object& Data);
    bool _find(BSTNode *act, const Object& Data);
    Object _findIndex(BSTNode *act, const int &Index);
    void _remove(BSTNode *&act);
    void _free(BSTNode *&act);
    void _dfs(BSTNode *node);
    BSTNode* _getPrec(BSTNode *node);
    void update_sz(BSTNode *&node);
    void _erase(BSTNode *&node, const int& Index);
    BSTNode *_root;
    int _size;
};

template<class T>
SortedListBST<T>::SortedListBST() {
    _root = NULL;
    _size = 0;
}

template<typename T>
typename SortedListBST<T>::BSTNode* SortedListBST<T>::_getPrec(BSTNode *node) {
    assert(node != NULL);
    BSTNode *prec;
    if(node->_right) {
        prec = node->_right;
        while(prec->_left)
            prec = prec->_left;
        return prec;
    }
    prec = node;
    while(prec->father && prec->father->_right == prec)
        prec = prec->father;
    return prec->father;
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
        /// done
        _remove(node);
        return ;
    }
    if(pos > Index)
        _erase(node->_left, Index);
    else
        _erase(node->_right, Index - pos - 1);
    node->_cnt = 1;
    if(node->_left)
        node->_cnt += node->_left->_cnt;
    if(node->_right)
        node->_cnt += node->_right->_cnt;
}

template<class T>
void SortedListBST<T> :: _remove(BSTNode *&node) {
    if(node == _root) {
        BSTNode *aux = _root;
        if(aux->_left)
            node = aux->_left;
        else
            node = aux->_right;
        delete aux;
    }
    else if(node->_left && node->_right) {
        BSTNode *aux = node->_right, *prev = NULL;
        while(aux -> _left) {
            prev = aux;
            aux = aux->_left;
        }
        swap(node->_data, aux->_data);
        if(prev)
            prev->_left = NULL;
        delete aux;
    }
    else if(node->_left) {
        if(node->_father->_left == node)
            node->_father->_left = node->_left;
        else
            node->_father->_right = node->_left;
    }
    else if(node->_right) {
        if(node->_father->_left == node)
            node->_father->_left = node->_right;
        else
            node->_father->_right = node->_right;
    }
    else {
        if(node->_father->_left == node)
            node->_father->_left = NULL;
        else
            node->_father->_right = NULL;
        delete node;
    }
}

template<class T>
void SortedListBST<T> :: update_sz(BSTNode *&node) {
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
    std::cerr << node->_data << ' ' << node->_cnt << '\n';
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
    _size = 0;
}

template<class T>
int SortedListBST<T>::size() {
    return this->_size;
}

#endif // SORTEDLISTBST_H
