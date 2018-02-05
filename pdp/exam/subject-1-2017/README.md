# Exam to Parallel and Distributed Programming `jan-feb 2017, subject no. 1`

1. (3.5p) Write a parallel (distributed or local, at your choice) program for solving the k-coloring
problem. That is, you are given a number k, and n objects and some pairs among them that have
distinct colors. Find a solution to color them with at most n colors in total, if one exists.
Assume you have a function that gets a vector with n integers representing the assignment of colors
to objects and checks if the constraits are obeyed or not.

2. (2.5p) Consider the following code for inserting a new value into a linked list at a given
position. We assume that insertions can be called concurrently, but not for the same position.
Find and fix the concurrency issue. Also, describe a function for parsing the linked list.

```cpp
struct Node {
    unsigned payload;
    Node* next;
    Node* prev;
    mutex mtx;
};

void insertAfter(Node* before, unsigned value) {
    Node* node = new Node;
    node->payload = value;
    Node* after = before->next;
    before->mtx.lock();
    before->next = node;
    before->mtx.unlock();
    after->mtx.lock();
    after->prev = node;
    after->mtx.unlock();
    node->prev = before;
    node->next = after;
}
```

3. (3p) We have n servers that can communicate to each other. There are events producing on each of
them; each event has an associated information. Each server must write a history of all events
(server and event info) produced on all servers, and, furthermore, the recorded history must be the
same for all servers. Write a distributed algorithm that accomplishes that. Consider the case n = 2
for starting.

