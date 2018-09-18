#ifndef DYNAMICVECTOR_H
#define DYNAMICVECTOR_H

#include <iostream>

using namespace std;

template <typename T>
class DynamicVector
{
    public:
        /** Default constructor */
        DynamicVector() {
            capacity = 2;
            length = 0;
            arr = new T[capacity];
        }
        /** Default destructor */
        ~DynamicVector() {
            capacity = 0;
            length = 0;
            delete [] arr;
        }
        /** Copy constructor
         *  \param other Object to copy from
         */
        DynamicVector(const DynamicVector& other) {
            capacity = other.capacity;
            length = other.length;
            arr = new T[capacity];
            for(int i = 0 ; i < other.length; ++ i)
                arr[i] = other.arr[i];
        }
        /** Assignment operator
         *  \param other Object to assign from
         *  \return A reference to this
         */
        DynamicVector& operator=(const DynamicVector& other) {
            capacity = other.capacity;
            length = other.length;
            arr = new T[capacity];
            for(int i = 0 ; i < other.length; ++ i)
                arr[i] = other.arr[i];
            return *this;
        }
        void push_back(T el) {
            if(length == capacity) {
                capacity *= 2;
                T* newarr = new T[capacity];
                for(int i = 0 ; i < capacity / 2 ; ++ i)
                    newarr[i] = arr[i];
                delete [] arr;
                arr = newarr;
            }
            arr[length] = el;
            ++ length;
        }
        void remove(T el) {
            for(int i = 0 ; i < length ; ++ i)
                if(arr[i] == el) {
                    swap(arr[i], arr[length - 1]);
                    -- length;
                }
        }
        int size() const {
            return length;
        }
        inline T& operator [] (int pos) {
            return arr[pos];
        }
        void clear() {
            capacity = 2;
            length = 0;
            delete []arr;
            arr = new T[capacity];
        }
    protected:

    private:
        T *arr;
        int capacity, length;
};

#endif // DYNAMICVECTOR_H
