from .goal_state import Goal
from graph_search.node import Node

class TileGameGoal(Goal):

    def __init__(self, n: int):
        g = []
        for i in range(n):
            g.append(i)
        self.goal = tuple(g)

    def is_goal_state(self,node: Node):
        return node.state.board == self.goal