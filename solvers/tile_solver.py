import time
from actions.action import NTileGameActions
from node import Node
from search import TreeSearch
from frontier import DFSFrontier
from state import State
from result import Result

import sys


class TileSolver():

    def __init__(self, nth_tile, exponent):
        self.nth_tile = nth_tile
        self.exponent = exponent

    def go(self, frontier, initial_board):

        goal = self.get_goal_state(self.nth_tile)
        
        start_state = self.get_start_state(initial_board)

        actions = NTileGameActions(self.nth_tile, self.exponent, type(frontier) == DFSFrontier)

        search = TreeSearch(frontier, actions, goal)
        
        start = time.time()
        node = search.search(start_state)
        end = time.time()

        mem_usage = self.get_mem_usage()
        runtime = end - start

        result = None
        if node is not None:
            result = Result(node.get_path(), node.cost, search.nodes_expanded, node.depth, search.max_search_depth, runtime, mem_usage)
        else:
            result = Result([],0,search.nodes_expanded,0,search.max_search_depth, runtime, mem_usage)
        return result

    def get_mem_usage(self):
        mem_usage = 0.0
        if sys.platform == "win32":
            import psutil
            rss = psutil.Process().memory_info().rss
            mem_usage = rss / 1048576
        else:
            import resource
            mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        return mem_usage

    def get_goal_state(self, n: int):
        goal = []
        for i in range(n + 1):
            goal.append(i)
        return tuple(goal)

    def get_start_state(self, initial_board):
        blank_pos = initial_board.index(0)
        initial_state = State(initial_board,blank_pos)
        start_state = Node(initial_state, time.time())
        return start_state

