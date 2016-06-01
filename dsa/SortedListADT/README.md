#ADT Project
- Student: Cosmin Rusu, gr. 917


##Statement
- ADT: **Sorted List**
    - Representation 1: **Linked List**
    - Representation 2: **Binary Search Tree**
- Problem:
    1. Consider n balloons that are moving vertically. Select the biggest number of balloons such that they will not touch between them. (Solution should also present the list of balloons.)


##ADT

```c++
/**
 _____________________________________________________________________________________________________
/ @Author: Cosmin Rusu, group 917, Faculty of Computer Science                                         \
| **************************************************************************************************** |
| Abstract Sorted List interface                                                                       |
| **************************************************************************************************** |
| Methods:                                                                                             |
|     - getAtIndex (index given)                                                                       |
|     - add (insert sorted)                                                                            |
|     - removeAtIndex (index given)                                                                    |
|     - contains (checks if list contains given data)                                                  |
|     - clear (list is empty after call)                                                               |
\     - size (returns list node count)                                                                 /
 ------------------------------------------------------------------------------------------------------
  \
   \   \_\_    _/_/
    \      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
*/

template <typename Object>
class AbstractSortedList {
public:
    /**
        Get Object from 'Index' in list (counting from 0)
        Index - The list element position
        @PRECOND: Index points between 0 and count, list is valid (nonempty)
        @POSTCOND:
        Return: Object contained at Index
    */
    virtual Object getAtIndex(const int& Index) = 0;

    /**
        Add element in the list (SORTED ASCENDING)
        Data - Element to be added in the list
        @PRECOND: Data is an object of 'Object' type (defined at declaration)
        @POSTCOND:
            List now contains T (sorted)
    */
    virtual void add(const Object& Key) = 0;

    /**
        Remove element from list at 'Index'
        Index - The list element position
        @PRECOND: Index points between 0 and count, list is valid (nonempty)
        @POSTCOND:
        Object at index 'Index' is now removed
    */
    virtual void removeAtIndex(const int& Index) = 0;

    /**
        Check if the list contains 'Data'
        Data - Data to be checked if it exists
        @PRECOND: Data is an object of 'Object' type (defined at declaration)
        @POSTCOND
        Return: True - if it exists
        Return: False - otherwise
    */
    virtual bool contains(const Object& Key) = 0;

    /**
        Clears the list
        @PRECOND: None
        @POSTCOND: this->count_ = 0;
    */
    virtual void clear() = 0;

    /**
        Returns the node count (this->count_)
        @PRECOND: None
        @POSTCOND:
        Return: count_ (element count in list)
    */
    virtual int size() = 0;

protected:
    int _count;

private:
};
```

###Linked List Implementation

```c++
#include <abstractsortedlist.h>
#include <cassert>

template <typename Object>
class SortedSLList : public AbstractSortedList<Object> {
public:
    /** Constructors */
    SortedSLList();
    SortedSLList(const Object& Data);
    /** Destructor */
    ~SortedSLList();
    /** Get the 'data' at Index in list */
    Object getAtIndex(const int& Index);
    /** Get the 'data' at front in list */
    Object getFront();
    /** Get the 'data' at back in list */
    Object getBack();
    /** Add into the list sorted ascending */
    void add(const Object& Data);
    /** Remove the 'data' at Index in list */
    void removeAtIndex(const int& Index);
    /** Remove the 'data' at front in list */
    void removeFront();
    /** Remove the 'data' at back in list */
    void removeBack();
    /** Check if list contains 'Data' */
    bool contains(const Object& Data);
    /** Clear list */
    void clear();
    /** Return list node count */
    int size();
private:
    class SLNode {
    private:
        friend class SortedSLList;
        Object _data;
        SLNode *_next;
    public:
        /** Constructor */
        SLNode(const Object& data = NULL, const SLNode* next = NULL): _data(data), _next(next) {}
        /** Destructor */
        ~SLNode() {}
        /** Assignment oprator */
        SLNode& operator=(const SLNode& other);
        /** Getter for the data - useless */
        Object& getData();
    };
    /** Begin and end of the Linked List*/
    SLNode *_begin, *_end;
};

/**
    Default constructor
    @PRECOND: None
    @POSTCOND:
        begin = NULL
        end = NULL
        count = 0
    @COMPLEXITY:
        O(1) - it takes constant time to initialize a singly-liked list
*/
template <typename Object>
SortedSLList<Object>::SortedSLList() {
    this->_begin = NULL;
    this->_end = NULL;
    this->_count = 0;
}

/**
    Constructor when one Objects is given
    Create a single-element linked list
    @PRECOND: Node
    @POSTCOND:
        begin = end = node containing the given argument
        count = 1
    @COMPLEXITY:
        O(1) - it takes constant time to initialize a singly-liked list
*/
template <typename Object>
SortedSLList<Object>::SortedSLList(const Object& Data) {
    this->_begin = new SLNode(Data);
    this->_end = this->_begin;
    this->_count = 1;
}

/**
    Destructor: release the memory (works exactly like the clear() method)
    @PRECOND: None
    @POSTCOND:
        List is destroyed
        front = NULL
        back = NULL
        count = 0
    @COMPLEXITY:
        O(N) - where N is the number of nodes in the Singly-Liked List
*/
template <typename Object>
SortedSLList<Object>::~SortedSLList() {
    SLNode *prevNode = NULL, *node = this->_begin;
    while(node != NULL) {
        prevNode = node;
        node = node->_next;
        delete prevNode;
    }
    this->_count = 0;
    this->_begin = this->_end = NULL;
}

/**
    getAtIndex(const int& Index): Method to get the element from a given Index
    Index - the required element position
    @PRECOND: Index between 0 and count - 1
    @POSTCOND:
        Return: Object contained at Index
    @COMPLEXITY:
        We are always making exactly 'Index' steps ahead in the Liked List, so in the
        worst scenario we will execute exactly N steps.
        O(N) where N is the number of nodes in the Singly-Liked List
*/
template <typename Object>
Object SortedSLList<Object>::getAtIndex(const int& Index) {
    /// todo, give up on assertion
    assert(0 <= Index && Index < this->_count);
    SLNode *act = this->_begin;
    int i = 0;
    while(i < Index) {
        act = act->_next;
        ++ i;
    }
    return act->_data;
}

/**
    getFront(): Method to get the first element in the list (aka the smallest one since the ADT is sorted by the Object's < operator)
    @PRECOND: List is valid (not empty)
    @POSTCOND:
        Return: Object contained in front
    @COMPLEXITY:
        O(1) since we store the front node of the Singly-Liked List
*/
template <typename Object>
Object SortedSLList<Object>::getFront() {
    if(this->_begin == NULL)
        return NULL;
    return this->_begin->_data;
}

/**
    getBack(): Method to get the last element in the list (aka the biggest one since the ADT is sorted by the Object's < operator)
    @PRECOND: List is valid (not empty)
    @POSTCOND:
        Return: Object contained at the end of the list
*/
template <typename Object>
Object SortedSLList<Object>::getBack() {
    if(this->_end == NULL)
        return NULL;
    return this->_end->_data;
}

/**
    add(const Object& Data): Method to add an object to the last, while maintaining the sorted property
    Data - Element to be added to the list
    @PRECOND: Data is an object of type 'Object' (defined at the declaration of the SortedSLList)
    @POSTCOND:
        Return: The list now contains Data (and still sorted)
    @COMPLEXITY:
        We first, see where we need to insert the new node, then we do the insert.
        The first part requires O(N) time since in the worst case we look at all the nodes (here N - number
        of nodes of SLList).
        The second part required O(1) time since we only change some pointers.
*/
template <typename Object>
void SortedSLList<Object>::add(const Object& Data) {
    if(this->_begin == NULL)
        this->_begin = this->_end = new SLNode(Data);
    else {
        if(this->_begin->_data >= Data) {
            SLNode *newNode = new SLNode(Data);
            newNode->_next = this->_begin;
            this->_begin = newNode;
        } else {
            SLNode *node = this->_begin, *prevNode = NULL;
            while(node != NULL && node->_data < Data) {
                prevNode = node;
                node = node->_next;
            }
            prevNode->_next = new SLNode(Data);
            prevNode->_next->_next = node;
            if(node == NULL)
                this->_end = prevNode->_next;
        }
    }
    this->_count ++;
}


/**
    removeAtIndex(const int& Index): Method to remove the element from a given Index
    Index - the required element position
    @PRECOND: Index between 0 and count - 1
    @POSTCOND:
        Object at index Index is not removed
    @COMPLEXITY:
        We are always making exactly 'Index' steps ahead in the Liked List, so in the
        worst scenario we will execute exactly N steps.
        O(N) where N is the number of nodes in the Singly-Liked List
*/
template <typename Object>
void SortedSLList<Object>::removeAtIndex(const int& Index) {
    assert(0 <= Index && Index < this->_count);
    if(Index == 0) {
        SLNode *aux = this->_begin;
        this->_begin = this->_begin->_next;
        delete aux;
        this->_count --;
        return ;
    }
    SLNode *prevNode = NULL, *node = this->_begin;
    int i = 0;
    while(i < Index) {
        prevNode = node;
        node = node->_next;
        ++ i;
    }
    prevNode->_next = node->_next;
    this->_count --;
    delete node;
}

/**
    removeFront(): Method to remove front element
    @PRECOND: List is valid (nonempty)
    @POSTCOND:
        Object at index 0 is now removed
    @COMPLEXITY:
        O(1)
*/
template <typename Object>
void SortedSLList<Object>::removeFront() {
    if(this->_begin == NULL)
        return ;
    SLNode *lastFront = this->_begin;
    this->_begin = this->_begin->_next;
    this->_count --;
    delete lastFront;
}

/**
    removeBack(): Method to remove back element
    @PRECOND: List is valid (nonempty)
    @POSTCOND:
        Object at index 'count - 1' is now removed
    @COMPLEXITY:
        O(N) since we first have to get the node ahead of the last element, then to remove the second one.
        Here N - number of elements in the SLList.
*/
template <typename Object>
void SortedSLList<Object>::removeBack() {
    if(this->_begin == NULL)
        return ;
    SLNode *prevNode = NULL, *node = this->_begin;
    while(node->_next != NULL) {
        prevNode = node;
        node = node->_next;
    }
    if(prevNode != NULL) {
        delete prevNode->_next;
        prevNode->_next = NULL;
        this->_end = prevNode;
    } else {
        delete this->_begin;
        this->_begin = this->_end = NULL;
    }
    this->_count --;
}
/**
    contains(const Object& Data): Method to check if the list contains 'Data'
    Data - Data to be checked if it exists
    @PRECOND: Data is an object of 'Object' type (defined at declaration)
    @POSTCOND
        Return: True - if it exists, False - otherwise
    @COMPLEXITY:
        O(N) where N - the number of nodes in the SLList
*/
template <typename Object>
bool SortedSLList<Object>::contains(const Object& Data) {
    SLNode *node = this->_begin;
    while(node != NULL) {
        if(node->_data == Data)
            return true;
        node = node->_next;
    }
    return false;
}

/**
    clear*(): Method to clear the list
    @PRECOND: None
    @POSTCOND: count = 0
    @COMPLEXITY:
        O(N) where N is the number of nodes in the SLList
*/
template <typename Object>
void SortedSLList<Object>::clear() {
    SLNode *prevNode = NULL, *node = this->_begin;
    while(node != NULL) {
        prevNode = node;
        node = node->_next;
        delete prevNode;
    }
    this->_count = 0;
    this->_begin = this->_end = NULL;
}

/**
    size(): Method to return the node count
    @PRECOND: None
    @POSTCOND:
        Return: count (number of nodes in the Linked List)
    @COMPLEXITY:
        O(1)
*/
template <typename Object>
int SortedSLList<Object>::size() {
    return this->_count;
}

/**
    '=' operator for the SLNode class
*/
template <typename Object>
typename SortedSLList<Object>::SLNode& SortedSLList<Object>::SLNode::operator=(const SLNode& other) {
    this->_data = other._data;
    this->_next = other._next;
}

/**
    getData(): Getter for the data of a SLNode
    @POSTCOND: None
    @PRECOND:
        Return: the data stored in the current node
    @COMPLEXITY:
        O(1)
*/
template <typename Object>
Object& SortedSLList<Object>::SLNode::getData() {
    return this->_data;
}
```

###Binary Search Tree Implementation

```c++
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
```

###Testing
I created a seaparate class for testing, called generically `tester.h`. From the methods, I think only the randomTest() method is relevand. The other methods can be seen in the source file.

```c++
#include <sortedsllist.h>
#include <sortedlistbst.h>
#include <iostream>
#include <time.h>
#include <set>
#include <algorithm>
#include <stdlib.h>

class Tester {
public:
    /** Default constructor */
    Tester();
    /** Unit tests for all the SortedListBST methods */
    void unitTestSortedListBSTAdd();
    void unitTestSortedListBSTRemove();
    void unitTestSortedListBSTGet();
    void unitTestSortedListBSTContains();
    void unitTestSortedListBSTClear();

    /** Unit tests for all the SortedSLList methods */
    void unitTestSortedSLListAdd();
    void unitTestSortedSLListRemove();
    void unitTestSortedSLListGet();
    void unitTestSortedSLListContains();
    void unitTestSortedSLListClear();

    void randomTest();
};

Tester::Tester() {
    srand(time(NULL));

    randomTest();
    unitTestSortedSLListAdd();
    unitTestSortedSLListRemove();
    unitTestSortedSLListGet();
    unitTestSortedSLListContains();
    unitTestSortedSLListClear();

    unitTestSortedListBSTAdd();
    unitTestSortedListBSTRemove();
    unitTestSortedListBSTGet();
    unitTestSortedListBSTContains();
    unitTestSortedListBSTClear();
}

void Tester::randomTest() {
    int m = 1000;
    int maxval = 1000000000;
    std::multiset <int> s;
    SortedListBST<int> bstList;
    SortedSLList<int> slList;
    for(int i = 1; i <= m; ++ i) {
        assert(slList.size() == s.size());
        assert(bstList.size() == s.size());
        int op = rand() % 3;
        if(op == 0) { /// insert
            int val = rand() % maxval;
            s.insert(val);
            slList.add(val);
            bstList.add(val);
        }
        else if(op == 1) {
            if(!s.size())  /// they are empty
                continue;
            int ind = rand() % s.size();
            auto it = s.begin();
            std::advance(it, ind);
            s.erase(it);
            slList.removeAtIndex(ind);
            bstList.removeAtIndex(ind);
        }
        else {
            std::vector <int> v;
            std::vector <int> a, b;
            for(int i = 0; i < v.size(); ++ i) {
                a.push_back(slList.getAtIndex(i));
                b.push_back(bstList.getAtIndex(i));
            }
            assert(v == a); /// and implictly, a == b
            assert(v == b);
        }
    }
}
```

##Problem
Consider n balloons that are moving vertically. Select the biggest number of balloons such that they will not touch between them. (Solution should also present the list of balloons.)

**The solution is as follows:**

The ballons are moving only vertically. Each circle will stay on a fixed interval `[xst, xdr]` on the `OX` axis. So, each circle will be 'translated' as a closed interval, and the problem is reduced to the Activity Selection Problem. http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/

For simplicity, I will assume we will read the interval `[xst, xdr]` for each circle.
If the input will be `(r, x, y)` - denoting the center `(x, y)` of the circle and `r` - the radius, it's easy to get the `OX` interval:
    `[x-r, x+r]`
Also, I will asume that the circles [1, 2] and [2, 3] do not touch.

**Here is the solution for the activity selection problem:**

The greedy choice is to always pick the next activity whose finish time is least among the remaining activities and the start time is more than or equal to the finish time of previously selected activity. We can sort the activities according to their finishing time so that we always consider the next activity as minimum finishing time activity.
    1) Sort the activities according to their finishing time
    2) Select the first activity from the sorted array and print it.
    3) Do following for remaining activities in the sorted array.
        a) If the start time of this activity is greater than the finish time of previously selected activity then select this activity and print it.

**How does Greedy Choice work for Activities sorted according to finish time?**

Let the give set of activities be S = {1, 2, 3, ..n} and activities be sorted by finish time. The greedy choice is to always pick activity 1. How come the activity 1 always provides one of the optimal solutions. We can prove it by showing that if there is another solution B with first activity other than 1, then there is also a solution A of same size with activity 1 as first activity. Let the first activity selected by B be k, then there always exist A = {B – {k}} U {1}.(Note that the activities in B are independent and k has smallest finishing time among all. Since k is not 1, finish(k) >= finish(1)).


###Tests structure
The intervals are fully random in some spcific interval, depending on the test.
Here is how they are generated: T[i] is the number of intervals for the i<sup>th</sup> test, and [0, v[i]] is the i<sup>th</sup> range interval.

```python
from random import randint

T = [10, 100, 1000, 2500, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 250000, 300000, 400000, 500000, 500000, 500000, 500000, 500000, 500000]
v = [2 ** (i + 11) for i in range(20)]

print(v)
for i in range(len(T)):
    print("> Generating test" + str(i) + ".in <")
    f = open("test" + str(i) + ".in", "w");
    n = T[i]
    f.write(str(n) + "\n")
    for j in range(n):
        x = randint(0, v[i])
        y = randint(0, v[i])
        if x > y:
            (x, y) = (y, x)
        f.write(str(x) + " " + str(y) + "\n")
    f.close()
```
