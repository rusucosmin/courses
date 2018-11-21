// An example worksheet, run it using the button above!

1 + 1

def foo(x: Int): Int  = x * 2

foo(21)

foo(21)

type NodeId = Int
type DirectedEdge = (NodeId, NodeId)
type DirectedGraph = List[DirectedEdge]

def triangles(edges: DirectedGraph): List[(NodeId, NodeId, NodeId)] = 
  for {
    (x1, y1) <- edges
    (x2, y2) <- edges if y1 == x2
    (x3, y3) <- edges if y2 == x3 && y3 == x1
    if x1 < y1 && y1 < y2
  } yield (x1, y1, y2)
def trianglesTrans(edges: DirectedGraph): List[(NodeId, NodeId, NodeId)] =
  edges.flatMap{(x1, y1) =>
    edges.filter((x2, _) => y1 == x2).flatMap{(x2, y2) => 
      edges.filter((x3, y3) => y2 == x3 && y3 == x1)
          .filter((_, _) => x1 < y1 && y1 < y2)
          .map((_, _) => (x1, y1, y2))
    }
  }
triangles(List((1, 2), (2, 3), (3, 1)))
trianglesTrans(List((1, 2), (2, 3), (3, 1)))
