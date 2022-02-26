class State():

    def __init__(self, board, blank_pos):
        self.board = board
        self.blank_pos = blank_pos

    def __repr__(self):
        return f"board: {self.board}, blank_pos: {self.blank_pos}"