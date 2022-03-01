from .state import State
class TileGameState(State):

    board_dimension = 0

    #board is an array of ints each indice is a space on the board 
    # and the value at each indice is the number tile occupying that space
    #using blank_pos to keep track of the blank tile so i don't have to keep calling index(0)
    def __init__(self, board : tuple, blank_pos):
        self.board = board
        self.blank_pos = blank_pos

    def __repr__(self):
        return f"board: {self.board}, blank_pos: {self.blank_pos}"
    
    def __hash__(self):
        return hash(self.board)

    def __eq__(self, other):
       return self.board == other.board

    def h_value(self):
        #sum of distances of each tile to their correct spot
        #can change by 1 don't need to iterate the whole board
        #probably should use some kind of x,y system for board representation to make this part more efficient
        sum = 0
        for i, tile in enumerate(self.board):
            if tile != 0:
                y1 = i // self.board_dimension
                x1 = i % self.board_dimension

                y2 = tile // self.board_dimension
                x2 = tile % self.board_dimension

                sum += abs(y1 - y2) + abs(x1 - x2)
        return sum
