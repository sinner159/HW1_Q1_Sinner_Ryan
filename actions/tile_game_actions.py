from .action import Action
from states.tile_game_state import TileGameState

class NTileGameAction(Action):
    
    def simulate(self, state):
                
        new_pos = self.calculate_new_position(state)
        
        board_as_list = list(state.board)
        temp = board_as_list[new_pos]
        board_as_list[new_pos] = board_as_list[state.blank_pos]
        board_as_list[state.blank_pos] = temp
        
        board = tuple(board_as_list)
        
        new_state = TileGameState(board, new_pos)
        
        return new_state

    def calculate_new_position(self, state):
        return int(self.calculate_new_position_internal(state))

    def calculate_new_position_internal(self,blank_pos): raise NotImplementedError
    
        
class Up(NTileGameAction):
    
    def calculate_new_position_internal(self, state):
        return state.blank_pos - state.board_dimension
    
    def is_possible(self, state):
        return state.blank_pos >= state.board_dimension
    
    def get_name(self):
        return "Up"

    def get_precedence(self):
        return 1
    
    
class Down(NTileGameAction):

    def calculate_new_position_internal(self,state):
        return state.blank_pos + state.board_dimension
    
    def is_possible(self,state):
        return state.blank_pos < len(state.board) - state.board_dimension
    
    def get_name(self):
        return "Down"

    def get_precedence(self):
        return 2
    
class Left(NTileGameAction):
    
    def calculate_new_position_internal(self, state):
        return state.blank_pos - 1
    
    def is_possible(self, state):
        return state.blank_pos % state.board_dimension  > 0

    def get_name(self):
        return "Left"

    def get_precedence(self):
        return 3
    
class Right(NTileGameAction):
    
    def calculate_new_position_internal(self,state):
        return state.blank_pos + 1
    
    def is_possible(self,state):
        return state.blank_pos % state.board_dimension < (state.board_dimension - 1)
    
    def get_name(self):
        return "Right"

    def get_precedence(self):
        return 4
    