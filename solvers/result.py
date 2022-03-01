class Result():

    def __init__(self,path_to_goal, cost_of_path, nodes_expanded, search_depth, max_search_depth,runtime = 0.0, mem_usage = 0.0):
        self.path_to_goal = path_to_goal
        self.cost_of_path = cost_of_path
        self.nodes_expanded = nodes_expanded
        self.search_depth = search_depth
        self.max_search_depth = max_search_depth
        self.runtime = runtime
        self.mem_usage = mem_usage

    def __str__(self):
        return f"path_to_goal: {str(self.path_to_goal)}\n\
cost_of_path: {str(self.cost_of_path)}\n\
nodes_expanded: {str(self.nodes_expanded)}\n\
search_depth: {str(self.search_depth)}\n\
max_search_depth: {str(self.max_search_depth)}\n\
running_time: {str(round(self.runtime,8))}\n\
max_ram_usage: {str(round(self.mem_usage,8))}\n" 
    
    #def get_path_to_goal_str(self):
