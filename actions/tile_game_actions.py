from action import Action
from state import State

class NTileGameAction(Action):
    
    def __init__(self,exponent):
        self.new_position = None
        self.exponent = exponent
    
    def simulate(self, state):
                
        new_pos = self.calculate_new_position(state.blank_pos)
        
        board_as_list = list(state.board)
        temp = board_as_list[new_pos]
        board_as_list[new_pos] = board_as_list[state.blank_pos]
        board_as_list[state.blank_pos] = temp
        
        board = tuple(board_as_list)
        
        new_state = State(board, new_pos)
        
        return new_state

    def calculate_new_position(self,blank_pos):
        return int(self.calculate_new_position_internal(blank_pos))

    def calculate_new_position_internal(self,blank_pos): raise NotImplementedError
    
        
class Up(NTileGameAction):
    
    def __init__(self, exponent):
        super().__init__(exponent)
    
    def calculate_new_position_internal(self, blank_pos):
        return blank_pos - self.exponent
    
    def is_possible(self, state):
        return state.blank_pos >= self.exponent
    
    def get_name(self):
        return "Up"

    def get_precedence(self):
        return 1
    
    
class Down(NTileGameAction):
    
    nth_tile = 0
     
    def __init__(self, exponent, nth_tile):
        super().__init__(exponent)
        self.nth_tile = nth_tile
    
    def calculate_new_position_internal(self,blank_pos):
        return blank_pos + self.exponent
    
    def is_possible(self,state):
        return state.blank_pos <= self.nth_tile - self.exponent
    
    def get_name(self):
        return "Down"

    def get_precedence(self):
        return 2
    
class Left(NTileGameAction):
       
    def __init__(self, exponent):
        super().__init__(exponent)
    
    def calculate_new_position_internal(self, blank_pos):
        return blank_pos - 1
    
    def is_possible(self, state):
        return state.blank_pos % self.exponent  > 0

    def get_name(self):
        return "Left"

    def get_precedence(self):
        return 3
    
class Right(NTileGameAction):
    
       
    def __init__(self,exponent):
        super().__init__(exponent)
    
    def calculate_new_position_internal(self,blank_pos):
        return blank_pos + 1
    
    def is_possible(self,state):
        return state.blank_pos % self.exponent < (self.exponent-1)
    
    def get_name(self):
        return "Right"

    def get_precedence(self):
        return 4
        
class NTileGameActions():

    def __init__(self,nth_tile,exponent, reverse):
    
        self.actions = []
        
        if reverse:
            self.actions.append(Right(exponent))
            self.actions.append(Left(exponent))
            self.actions.append(Down(exponent, nth_tile))
            self.actions.append(Up(exponent))
        else:
            self.actions.append(Up(exponent))
            self.actions.append(Down(exponent, nth_tile))
            self.actions.append(Left(exponent))
            self.actions.append(Right(exponent))

        self.current = -1
        self.size = len(self.actions)

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 1
        if self.current < self.size:
            return self.actions[self.current]
        else:
            self.current = -1
            raise StopIteration