#Requirements

Given a directed graph, find a Hamiltonean cycle, if one exists. Use multiple threads to
parallelize the search.

#Documentation

I solved the problems in `C++`.
The performance is measured on my personal computer with the following config:
```
MacBook Pro (13-inch, 2017)
Processor: 2.3 GHz Intel Core i5
Memory: 16 GB 2133 MHZ LPDDR3
Graphics: Intel Iris Plus GRaphics 640 1536 MB
```

##Algorithm

`In general, the problem of finding a Hamiltonian cycle is NP-complete (Karp 1972; Garey and
Johnson 1983, p. 199), so the only known way to determine whether a given general graph has a
Hamiltonian cycle is to undertake an exhaustive search.`
More about this [here](http://mathworld.wolfram.com/HamiltonianCycle.html).

First, a hamiltonian cycle is actually a permutation `p(0), p(1),..,p(n-1)` such that from there
is an edge between `p(i) and p(i + 1 mod n)` for every `0 <= i < n`.
Another observation comes from the fact that it does not matter from which node you start looking
for a hamiltonian cycles, because eventually you will reach that node.
An important fact is that the number of edges in the cycles will always be `n`. In other words,
we are looking for a subset of exactly `n` edges that forms a hamiltonian cycle.

We start with the basic solution (backtracking). The solution basically starts with the first
node, `1`, and recursively tries to add new nodes to the current path (based on the neighbours of
the current node). When reached `n` nodes, we check if the there is an edge between the first
and the last node in the path.
Insted of having one thread, we introduce two threads, when choosing which next node to append
from the list of nodes of current node.
We also need to keep track of the nodes which we selected so far.


##Synchronization

Each thread makes two children threads, so it must wait for them in order to solve it's current
problem.
Apart from that, each thread is independent, which makes this implementation `blazingly fast`.
