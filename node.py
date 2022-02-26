from functools import total_ordering

@total_ordering
class Node():
    
    def __init__(self, state, time_of_creation, action_name = "", action_precedence = 0, previous_node = None):
        
        self.cost = 1
        self.depth = 0
        self.f_value = 0

        self.time_of_creation = time_of_creation
        self.action_name = action_name
        self.action_precedence = action_precedence
        self.state = state
        
        self.previous_node = previous_node

        if self.previous_node != None:
            self.depth = previous_node.depth + 1
            self.cost += previous_node.cost
        else:
            self.cost = 0

    def __repr__(self):
        return f"f_value: {self.f_value} action: {self.action_precedence}, depth: {self.depth}, state: {self.state}"

    def get_path(self):
        path = []
        temp_node = self

        while(temp_node is not None and temp_node.previous_node is not None):
            path.insert(0, temp_node.action_name)
            temp_node = temp_node.previous_node
        return path
    

    def __lt__(self, other):
        if  other is None: return False
        if self.f_value < other.f_value: return True
        elif self.f_value == other.f_value and self.depth < other.depth : return True
        elif self.f_value == other.f_value and self.depth == other.depth and self.action_precedence < other.action_precedence: return True
        elif self.f_value == other.f_value and self.depth == other.depth and self.action_precedence == other.action_precedence and  self.time_of_creation < other.time_of_creation : return True
        
        else: return False

    def __eq__(self, other):
        return type(other) == type(self) and self.f_value == other.f_value and self.action_precedence == other.action_precedence