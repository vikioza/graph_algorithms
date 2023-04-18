from __future__ import annotations
from dataclasses import dataclass, field
from string import ascii_lowercase
from random import randrange, choices
from sys import maxsize


@dataclass(init=False)
class Edge:
    weight: int
    connecting_nodes: list[Node]
    
    def __init__(self, node1: Node = None, node2: Node = None) -> None:
        self.weight = randrange(-10, 10, 1)
        if node1 is not None and node2 is not None:
            self.connecting_nodes = [node1, node2]


@dataclass(init=False, repr=False)
class DirectedEdge(Edge):
    starting_node: Node
    destination_node: Node
    
    def __init__(self, start: Node, destination: Node) -> None:
        super().__init__()
        self.starting_node = start
        self.destination_node = destination
        
    def __repr__(self):
        return f"\n\tEdge {self.weight} | Start: {self.starting_node.designation} | Dest: {self.destination_node.designation}"


@dataclass()
class Node:
    designation: str = None
    previous: Node = None
    shortest_path: int = maxsize
    visited: bool = False
    edges: list[Edge] = field(default_factory=list)
    
    def generate_designation(self):
        # printing lowercase
        letters = ascii_lowercase
        self.designation = ''.join(choices(letters, k=1)[0] for i in range(10))
            

@dataclass      
class DirectedNode(Node):
    edges: list[DirectedEdge] = field(default_factory=list)
    
    def get_all_destinations(self) -> list[DirectedNode]:
        return [edge.destination_node for edge in self.edges]
    
    def edge_to(self, target_node):
        for edge in self.edges:
            if edge.destination_node == target_node:
                return edge
        return None


@dataclass(init=False, repr=False)
class Graph:
    nodes: list[DirectedNode]
    
    def __init__(self, node_count: int, edge_count: int = None) -> None:
        if edge_count is None:
            edge_count = 2*(node_count - 1)
        
        self.nodes = []
        self._generate_graph(node_count, edge_count)
    
    def _generate_graph(self, node_count: int, edge_count: int, node_type: type[Node] = Node, edge_type: type[Edge] = Edge) -> None:
        unvisited_nodes = []
        for i in range(node_count):
            n = node_type()
            n.generate_designation()
            unvisited_nodes.append(n)            
        connected_nodes: list[node_type] = []
        
        while unvisited_nodes:
            current = choices(unvisited_nodes, k=1)[0]
            unvisited_nodes.remove(current)
            
            if connected_nodes:  # add edge from random visited node:
                origin: node_type = choices(connected_nodes, k=1)[0]
                origin.edges.append(edge_type(origin, current))
                edge_count -= 1
            
            connected_nodes.append(current)
        
        self.nodes = connected_nodes
        self.__random_edges(edge_count, edge_type=edge_type)
            
    def __random_edges(self, edge_count: int, self_loop: bool = False, edge_type: type[Edge] = Edge) -> Node:
        while edge_count:
            origin, destination = choices(self.nodes, k=2)
            if not self_loop:
                while origin == destination:
                    destination = choices(self.nodes, k=1)[0]
            origin.edges.append(edge_type(origin, destination))
            edge_count -= 1
    
    def __repr__(self):
        rep = ""
        for node in self.nodes:
            rep += str(node) + "\n\n"
        return rep
    
    def adjacency_matrix(self):
        matrix: list[list[int]] = [[None for node in self.nodes] for node in self.nodes]
        
        for idx, starting_node in enumerate(self.nodes):
            for jdx, destination_node in enumerate(self.nodes):
                edge = starting_node.edge_to(destination_node)
                matrix[idx][jdx] = edge.weight if edge is not None else None
        return matrix
    

@dataclass(init=False, repr=False)
class DirectedGraph(Graph):
    nodes: list[DirectedNode]
    
    def __init__(self, node_count: int, edge_count: int = None) -> None:
        if edge_count is None:
            edge_count = 2*(node_count - 1)
        
        self.nodes = []
        self._generate_graph(node_count, edge_count, DirectedNode, DirectedEdge)
        
    def __repr__(self):
        return super().__repr__()
            
    
if __name__ == "__main__":
    n = 30
    g = DirectedGraph(n)
    
    print(g)
    
    adj = g.adjacency_matrix()
    letters = [f"{num:04d}" for num in range(n)]
    letters = ["_____"] + letters
    
    def list_to_formatted_str(target: list) -> str:
        ret = ""
        for element in target:
            ret += f"{element: 4}|" if type(element) == int else str(element) + "|"
        return ret
    
    print(list_to_formatted_str(letters))
    for i, row in enumerate(adj):
        print(f"|{letters[i+1]}|{list_to_formatted_str(row)}")
