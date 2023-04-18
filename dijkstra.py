import sys
from dataclasses import dataclass
from graph import Node, Graph
    
    
class DijHeap:

    def insert(self):
        pass
    
    def pop(self):
        pass
    
    def heapify(self):
        pass
    
    
class Dijkstra:
    initial_node_idx: int
    target_node_idx: int
    
    nodes: list[Node] = []
    node_connections: list[list[int]]
    
    heap = DijHeap()
    
    def __init__(self, node_connections: list[list[int]], initial_node_idx: int = 0, target_node_idx: int = 0) -> None:
        self.node_connections = node_connections
        self.initial_node_idx = initial_node_idx
        self.target_node_idx = target_node_idx
        
        for idx, _ in enumerate(self.node_connections):
            if idx == self.initial_node_idx:
                self.nodes.append(Node(idx, shortest_path=0))
                continue
            self.nodes.append(Node(idx))
        
        self.heap.insert(self.nodes[self.initial_node_idx])
    
    
    def visit_node(self):
        pass