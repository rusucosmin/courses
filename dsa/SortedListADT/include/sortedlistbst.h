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
    /** Number of elements (not necessary since we have root->cnt, but still..**/
    int _size;
};

/**
    Default constructor
    @PRECOND: None
    @POSTCOND:
        root = NULL
        count = 0
    @COMPLEXITY: O(1) - it takes constant time to initialize a BST
*/
template<class T>
SortedListBST<T>::SortedListBST() {
    _root = NULL;
    _size = 0;
}

/**
    _getSuc(BSTNode *node): method to return the successor of a node in the BST
    @PRECOND: node != NULL
    @POSTCOND:
        Return: successor(node) - the node which comes right after 'node'
    @COMPLEXITY:
        O(N) where N - number of nodes in the BST
    @IDEA:
        We have two cases:
            - 'node' have a right son, which means that all the values in the right subtree are > the data
                in 'node', and to take the smallest one, we keep going left until we get to a node without a left son.
            - node doesn't have a right son, which means we have to go up to the father until the node we are now is
                a left son of it's parent.
*/
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

/**
    Destructor: release the memory (works exactly like the clear() method)
    @PRECOND: None
    @POSTCOND:
        Tree is destroyed
            root = NULL
            count = 0
    @COMPLEXITY: O(N) where N - number of nodes in the Tree
*/
template<class T>
SortedListBST<T>::~SortedListBST() {
    free(_root);
    _size = 0;
}

/**
    getAtIndex(const int& Index): method to retrieve the element on the position
    'Index' if we consider all the elements in the BST in a sorted order
    according to the '<' operator.
    @PRECOND: 0 <= 'Index' and 'Index" < count
    @POSTCOND:
        Node
    @COMPLEXITY: O(N) where N - number of nodes in the BST
    The idea is to keep a variable 'cnt' for each node representing the number of nodes
    in its subtree. This way we know on which way we take when we are looking for a specific
    index, so the complexity is O(Height of tree). It is known that the BST has O(N) height on worst case.
    (Try to insert the values in increasing or decreasing order in the BST)
*/
template<class T>
T SortedListBST<T>::getAtIndex(const int& Index) {
    assert(0 <= Index && Index < _size);
    return _findIndex(_root, Index);
}

/**
    add(const T& Data): method to insert a new element in the BST
    @PRECOND:
    @POSTCOND:
        root != NULL
        Data is in the BST (if it was already inserted, then duplicates are allowed)
    @COMPLEXITY: O(N) where N - number of nodes in the BST
    Again, the time complexity is actually O(height of Tree), so O(N) in the case of BST.
*/
template<class T>
void SortedListBST<T>::add(const T& Data) {
    _add(_root, NULL, Data);
    this->_size ++;
}

/**
    _erase(BSTNode *&node, const int& Index): method to erase the node which corresponds to
    the element on position Index in the list of all the elements of the BST, sorted.
    @PRECOND:
        node != NULL
        0 <= Index and Index < count
    @POSTCOND:
        The element at 'Index' is removed.
    @COMPLEXITY:
        O(Height(T)) = O(N) where N - number of nodes in the BST
*/
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

/**
    _erase_value(BSTNode *&node, const T& Data): method to erase the node containing
    'Data'.
    @PRECOND:
        node != NULL
        Data must be in the BST
    @POSTCOND:
        One occurrence of Data is removed.
        Warning! Duplicates are allowed, so it is not guaranteed that the BST will not
        contain any node with Data.
    @COMPLEXITY:
        O(Height(T)) = O(N) where N - number of nodes in the BST
*/
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

/**
    _remove(BSTNode *&node): method to remove a specific node from the BST
    @PRECOND:
        node != NULL
    @POSTCOND:
        node is removed from BST
    @COMPLEXITY:
        O(N) where N - number of nodes in BST
    @IDEA:
        We have 3 cases:
            - the node is a leaf:
                - simply delete it from the BST
            - the node has only one child (left or right, doesn't matter):
                - replace the node with it's unique son
            - the node has exactly two sons:
                - in this case, swap the current node with its successor, and then delete that node from the BST.
                - it is easy to see that the successor will always be in case 1 or 2 of our algorithm.
*/
template<class T>
void SortedListBST<T> :: _remove(BSTNode *&node) {
    if(node->_left == NULL && node->_right == NULL) {
        delete node;
        node = NULL;
    }
    else if(node->_right == NULL) { /// only _left
        BSTNode *aux = node;
        node = node->_left;
        node->_father = aux->_father;
        delete aux;
    }
    else if(node->_left == NULL) {
        BSTNode *aux = node;
        node = node->_right;
        node->_father = aux->_father;
        delete aux;
    }
    else {
        BSTNode *aux = _getSuc(node);
        node->_data = aux->_data;
        _erase_value(node->_right, aux->_data);
    }
}

/**
    update_sz(BSTNode *&node):
        - method to update the 'cnt' variable of a BSTNode.
        - this 'cnt' variable refers to the number of nodes in the subtree rooted at 'node'
    @POSTCOND:
        None
    @PRECOND:
        'cnt' for 'node' is correctly computed (updated)
    @COMPLEXITY:
        O(1) - constant time, we count the number of nodes by using the information already
        known in sons
*/
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

/**
    _add(BSTNode *&node, BSTNode *dad, const T& Data): auxiliary method to insert a new element in the BST
    @PRECOND:
        - None
    @POSTCOND:
        - root != NULL
        - Data is in the BST (if it was already inserted, then duplicates are allowed)
    @COMPLEXITY: O(N) where N - number of nodes in the BST
*/
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

/**
    _find(BSTNode *&node, const T& Data): method to find if an element is in the BST
    @PRECOND: None
    @POSTCOND:
        Return: true if an only if Data is in BST, false otherwise
    @COMPLEXITY: O(N) where N - number of nodes in the BST
*/
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

/**
    _findIndex(BSTNode *&node, const int& Index): method to find the element at the position 'Index'
    in the list of all the nodes sorted according
    @PRECOND: 0 <= 'Index' and 'Index' < count
    @POSTCOND:
        Return: the element we were searching for
    @COMPLEXITY: O(N) where N - number of nodes in the BST
*/
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

/**
    _free(BSTNode *&node): release the memory
    @PRECOND: None
    @POSTCOND:
        BST is destroyed
        root = NULL
        count = 0
    @COMPLEXITY: O(N) where N - number of nodes in the Tree
*/
template<class T>
void SortedListBST<T> ::_free(BSTNode *&node) {
    if(node == NULL)
        return ;
    free(node->_left);
    free(node->_right);
    delete node;
    node = NULL;
}

/**
    removeAtIndex(const int& Index): method to erase the node which corresponds to
    the element on position Index in the list of all the elements of the BST, sorted.
    @PRECOND:
        node != NULL
        0 <= Index and Index < count
    @POSTCOND:
        The element at 'Index' is removed.
    @COMPLEXITY:
        O(Height(T)) = O(N) where N - number of nodes in the BST
*/
template<class T>
void SortedListBST<T>::removeAtIndex(const int& Index) {
    assert(0 <= Index && Index < _size);
    _erase(_root, Index);
    -- this->_size;
}

/**
    contains(const T& Data): method to check if an object is in the BST
    @PRECOND: None
    @POSTCOND:
        Return: true if and only if Data is in BST, false otherwise
    @COMPLEXITY:
        O(Height(T)) = O(N) where N - number of nodes in the BST
*/
template<class T>
bool SortedListBST<T>::contains(const T& Data) {
    return _find(_root, Data);
}

/**
    clear(): release the memory
    @PRECOND: None
    @POSTCOND:
        BST is destroyed
        root = NULL
        count = 0
    @COMPLEXITY: O(N) where N - number of nodes in the Tree
*/
template<class T>
void SortedListBST<T>::clear() {
    _free(_root);
    _root = NULL;
    _size = 0;
}

/**
    size(BSTNode *&node): method to get the number of elements in the BST
    @PRECOND: None
    @POSTCOND:
        Return: count - the number of elements inside the Tree
    @COMPLEXITY: O(1) where N - number of nodes in the Tree
*/
template<class T>
int SortedListBST<T>::size() {
    return this->_size;
}

#endif // SORTEDLISTBST_H
