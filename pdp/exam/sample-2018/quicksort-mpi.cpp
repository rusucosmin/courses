#include <iostream>
#include <mpi.h>
#include <vector>
#include <algorithm>
#include <time.h>
#include <stdint.h>

using namespace std;

const int tagDataSize = 1;
const int tagInput = 2;
const int tagOutput = 3;

// Tree exploration functions
bool hasChildren(unsigned nrProcs, unsigned /*myId*/, unsigned level)
{
    return ((nrProcs >> level) > 1);
}

unsigned rightChild(unsigned nrProcs, unsigned myId, unsigned level)
{
    return myId + (nrProcs >> (level+1));
}

void parentAndLevel(unsigned nrProcs, unsigned myId, unsigned& parentId, unsigned& level)
{
    level = 0;
    while(nrProcs > 1) {
        nrProcs >>= 1;
        ++level;
    }
    parentId = myId;
    while((parentId & 1) == 0) {
        parentId >>= 1;
        --level;
    }
    --parentId;
}

// Finds the pivot and splits the src vector into pivot, v1 and v2. Precondition: src must be non-empty.
void split(vector<int> const& src, int& pivot, vector<int>& v1, vector<int>& v2)
{
    // we try the first, the last and the middle elements, and we choose the middle value of those 3
    size_t n = src.size();
    size_t mid = n/2;
    size_t pivotIdx;
    if(src[0] < src[mid]) {
        if(src[mid] < src[n-1]) {
            pivotIdx = mid;
        } else if(src[n-1] < src[0]){
            pivotIdx = 0;
        } else {
            pivotIdx = n-1;
        }
    } else {
        if(src[mid] > src[n-1]) {
            pivotIdx = mid;
        } else if(src[n-1] > src[0]){
            pivotIdx = 0;
        } else {
            pivotIdx = n-1;
        }
    }
    v1.clear();
    v2.clear();
    pivot = src[pivotIdx];
    for(size_t i=0 ; i<src.size() ; ++i) {
        if(src[i] < pivot) {
            v1.push_back(src[i]);
        } else if(i != pivotIdx) {
            v2.push_back(src[i]);
        }
    }
}

// Merges back the two sorted vectors and the pivot.
void join(int& pivot, vector<int> const& v1, vector<int> const& v2, vector<int>& dest)
{
    dest.clear();
    dest.reserve(v1.size()+v2.size()+1);
    std::copy(v1.begin(), v1.end(), std::back_inserter(dest));
    dest.push_back(pivot);
    std::copy(v2.begin(), v2.end(), std::back_inserter(dest));
}

// Performs quicksort on the 'vec'. This is called on process 'myId' at level 'level'; it delegates to sub-processes if needed.
void quicksort(vector<int>& vec, unsigned nrProcs, unsigned myId, unsigned level)
{
    if(hasChildren(nrProcs, myId, level)) {
        unsigned childId = rightChild(nrProcs, myId, level);
        int dataSize;
        if(vec.empty()) {
            cout << "Process " << myId << " sending empty vector to " << childId << "\n";
            // just send a zero data size, so that the child knows it has nothing to do and ends
            dataSize = 0;
            MPI_Send(&dataSize, 1, MPI_INT, childId, tagDataSize, MPI_COMM_WORLD);
        } else {
            // We split the work, we give half to the right child, and we keep half and process it locally
            vector<int> v1;
            vector<int> v2;
            int pivot;
            split(vec, pivot, v1, v2);
            dataSize = v2.size();
            cout << "Process " << myId << " sending " << dataSize << " elements to " << childId << "\n";
            MPI_Send(&dataSize, 1, MPI_INT, childId, tagDataSize, MPI_COMM_WORLD);
            if(dataSize > 0) {
                MPI_Send(v2.data(), dataSize, MPI_INT, childId, tagInput, MPI_COMM_WORLD);
            }
            quicksort(v1, nrProcs, myId, level+1);
            if(dataSize > 0) {
                cout << "Process " << myId << " receiving " << dataSize << " elements from " << childId << "\n";
                MPI_Status status;
                MPI_Recv(v2.data(), dataSize, MPI_INT, childId, tagOutput, MPI_COMM_WORLD, &status);
            }
            join(pivot, v1, v2, vec);
        }
    } else {
        // we process locally
        if(!vec.empty()) {
            vector<int> v1;
            vector<int> v2;
            int pivot;
            split(vec, pivot, v1, v2);
            quicksort(v1, nrProcs, myId, level+1);
            quicksort(v2, nrProcs, myId, level+1);
            join(pivot, v1, v2, vec);
        }
    }
}

void readData(vector<int>& v, int argc, char** argv)
{
    unsigned n;
    if(argc != 2 || 1!=sscanf(argv[1], "%u", &n) ){
        fprintf(stderr, "usage: mergesort <n>\n");
        return;
    }

    v.reserve(n);
    for(size_t i=0 ; i<n ; ++i) {
        // v.push_back(rand());
        v.push_back((i*101011) % 123456);
    }
    cout << "generated\n";
}

bool isSorted(vector<int> const& v)
{
    size_t const n = v.size();
    for(size_t i=1 ; i<n ; ++i) {
        if(v[i-1]>v[i]) return false;
    }
    return true;
}

void writeData(vector<int> const& v)
{
    if(isSorted(v)){
        cout << "Ok\n";
    } else {
        cout << "NOT SORTED!!!\n";
    }
}

int main(int argc, char** argv)
{
    MPI_Init(0, 0);
    int myId;
    int nrProcs;
    MPI_Comm_size(MPI_COMM_WORLD, &nrProcs);
    MPI_Comm_rank(MPI_COMM_WORLD, &myId);

    vector<int> vec;
    unsigned level;
    unsigned parent;
    int dataSize;
    if(myId == 0) {
        readData(vec, argc, argv);
        level = 0;
    } else {
        parentAndLevel(nrProcs, myId, parent, level);
        cout << "Process " << myId << " of " << nrProcs << ", at level " << level <<", receiving initial data from " << parent << "\n";
        MPI_Status status;
        MPI_Recv(&dataSize, 1, MPI_INT, parent, tagDataSize, MPI_COMM_WORLD, &status);
        if(dataSize > 0) {
            vec.resize(dataSize);
            MPI_Recv(vec.data(), dataSize, MPI_INT, parent, tagInput, MPI_COMM_WORLD, &status);
        }
    }
    quicksort(vec, nrProcs, myId, level);
    if(myId == 0) {
        writeData(vec);
    } else if(!vec.empty()){
        cout << "Process " << myId << " sending final data to " << parent << "\n";
        MPI_Send(vec.data(), dataSize, MPI_INT, parent, tagOutput, MPI_COMM_WORLD);
    } else {
        cout << "Process " << myId << " had nothing to do and is about to end\n";
    }
    MPI_Finalize();
}
