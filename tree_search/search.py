import time
from .node import Node
from .frontier import Frontier

class TreeSearch:
    
    def __init__(self, frontier, actions, goal):
        self.nodes_expanded = 0
        self.max_search_depth = 0

        self.frontier : Frontier = frontier
        self.actions = actions
        self.goal = goal

    def search(self, root):

        if root.state == self.goal:
            return root

        self.frontier.add_to_previously_visited(root)
        self.expand(root)

        while not self.frontier.empty():
            
            node = self.frontier.pop()
            
            if node.state == self.goal:
                return node
            else:
                self.expand(node)
        
        return 

    def expand(self, node):
        
        self.nodes_expanded += 1
        
        for action in self.actions:
            if action.is_possible(node.state):
                new_state = action.simulate(node.state)
                new_node = Node(new_state,time.time(), action.get_name(), action.get_precedence(), node)
                
                if not self.frontier.node_previously_visited(new_node):
                    if new_node.depth > self.max_search_depth:
                        self.max_search_depth = new_node.depth
                    
                    self.frontier.insert(new_node)