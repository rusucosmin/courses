/**_____________________________________________________________________________________________________
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

#ifndef ABSTRACTSORTEDLIST_H
#define ABSTRACTSORTEDLIST_H

template <typename Object>
class AbstractSortedList {
public:
    /*
        Get Object from 'Index' in list (counting from 0)
        Index - The list element position
        @PRECOND: Index points between 0 and count, list is valid (nonempty)
        @POSTCOND:
        Return: Object contained at Index
    */
    virtual Object getAtIndex(const int& Index) = 0;

    /*
        Add element in the list (SORTED ASCENDING)
        Data - Element to be added in the list
        @PRECOND: Data is an object of 'Object' type (defined at declaration)
        @POSTCOND:
            List now contains T (sorted)
    */
    virtual void add(const Object& Key) = 0;
    /*
        Remove element from list at 'Index'
        Index - The list element position
        @PRECOND: Index points between 0 and count, list is valid (nonempty)
        @POSTCOND:
        Object at index 'Index' is now removed
    */
    virtual void removeAtIndex(const int& Index) = 0;
    /*
        Check if the list contains 'Data'
        Data - Data to be checked if it exists
        @PRECOND: Data is an object of 'Object' type (defined at declaration)
        @POSTCOND
        Return: True - if it exists
        Return: False - otherwise
    */
    virtual bool contains(const Object& Key) = 0;
    /*
        Clears the list
        @PRECOND: None
        @POSTCOND: this->count_ = 0;
    */
    virtual void clear() = 0;

    /*
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

#endif // ABSTRACTSORTEDLIST_H
