#Graphs

###Required operations:

- get the number of vertices;
- given two vertices, find out whether there is an edge from the first one to the second one, and retrieve the Edge_id if there is an edge (the latter is not required if an edge is represented simply as a pair of vertex identifiers);
- get the in degree and the out degree of a specified vertex;
- iterate through the set of outbound edges of a specified vertex (that is, provide an iterator). For each outbound edge, the iterator shall provide the Edge_id of the curren edge (or the target vertex, if no Edge_id is used).
- iterate through the set of inbound edges of a specified vertex (as above);
- get the endpoints of an edge specified by an Edge_id (if applicable);
- retrieve or modify the information (the integer) attached to a specified edge.

###The operations must take no more than:
- `O(deg(x)+deg(y))` for: verifying the existence of an edge and for retrieving the edge between two given vertices.
- `O(1)` for: getting the first or the next edge, inbound or outbound to a given vertex; get the endpoints, get or set the attached integer for an edge (given by an Edge_id or, if no Edge_id is defined, then given by its source and target); get the total number of vertices or edges; get the in-degree or the out-degree of a given vertex.


###Optional operations (bonus)

- The property (cost) attached to the edges should be external to the graph. It shall be a template/generic class, parametrised on the property type. An instance of this Edge_property class shall behave like a map (dictionary) attaching a value to each edge of the graph. It shall be possible to create any number of instances, at any time, without modifying the graph.
- The graph shall be modifiable: it shall be possible to add and remove an edge, and to add and remove a vertex. Think about what should happen with the properties of existing edges and with the identification of remaining vertices. You may use an abstract Vertex_id instead of an int in order to identify vertices; in this case, provide a way of iterating the vertices of the graph.
- The graph shall be copyable, that is, it should be possible to make an exact copy of a graph, so that the original can be then modified independently of its copy. Think about the desirable behaviour of an Edge_property attached to the original graph, when a copy is made.
