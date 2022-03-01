from argparse import ArgumentError
from data_structures.linked_list import LinkedList
from data_structures.min_heap import MinHeap
from .node import Node


class Frontier():
    
    def __init__(self):
        self.previously_visited = set()

    def pop(self): raise NotImplementedError
   
    def empty(self): raise NotImplementedError
    
    def insert(self,node): raise NotImplementedError

    def node_previously_visited(self,node):
        return node.state in self.previously_visited
    
    def add_to_previously_visited(self,node):
        self.previously_visited.add(node.state)

class BFSFrontier(Frontier):
        
    def __init__(self):
        super().__init__()
        self.nodes = LinkedList()
    
    def pop(self):
        return self.nodes.pop()
        
    def empty(self):
        return self.nodes.empty()
    
    def insert(self, node):
        self.nodes.append(node)
        self.add_to_previously_visited(node)
        
class DFSFrontier(Frontier):

    def __init__(self):
        super().__init__()
        self.nodes = LinkedList()

    def pop(self):
        return self.nodes.pop()
        
    def empty(self):
        return self.nodes.empty()
    
    def insert(self,node):
        self.nodes.prepend(node)
        self.add_to_previously_visited(node)

        

class AStarFrontier(Frontier):
    
    def __init__(self):
        super().__init__()
        self.nodes = MinHeap()

    def pop(self):
        return self.nodes.extract_min()
        
    def empty(self):
        return len(self.nodes.heap) == 0

    def insert(self, node: Node):
        
        estimated_cost_to_goal = node.state.h_value()
        node.f_value = node.cost + estimated_cost_to_goal
        self.nodes.insert(node)
        self.add_to_previously_visited(node)


class FrontierFactory():

    def GetFrontier(self, method):
        frontier = None
        if method == "bfs":
            frontier = BFSFrontier()
        if method == "dfs":
            frontier = DFSFrontier()
        if method == "ast":
            frontier = AStarFrontier()

        if frontier == None:
            raise ArgumentError
        
        return frontier