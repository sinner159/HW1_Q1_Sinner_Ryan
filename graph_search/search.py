import time
from .node import Node
from .frontier import Frontier
from states.goal_state import Goal
from actions.action import Action
#Graph Search because we are keeping track of previously visited nodes
class GraphSearch:
    
    def __init__(self, frontier, actions):
        self.nodes_expanded = 0
        self.max_search_depth = 0

        self.frontier : Frontier = frontier
        self.actions = actions

    def search(self, root, goal: Goal):

        if goal.is_goal_state(root):
            return root

        self.frontier.add_to_previously_visited(root)
        self.expand(root)

        while not self.frontier.empty():
            
            node = self.frontier.pop()
            
            if goal.is_goal_state(node):
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