import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import actions.action as Actions
from state import State

up = Actions.Up(3)
down = Actions.Down(3, 8)
left = Actions.Left(3)
right = Actions.Right(3)

def get_state(board: tuple):
    state = State(board, board.index(0))
    return state

def test_up():
    state = get_state((3,1,2,0,4,5,6,7,8))
    assert up.simulate(state).board == (0,1,2,3,4,5,6,7,8)
    state = get_state((3,1,2,8,4,5,6,7,0))
    assert up.simulate(state).board == (3,1,2,8,4,0,6,7,5)

def test_up_is_possible():
    state = get_state((0,1,2,3,4,5,6,7,8))
    assert up.is_possible(state) == False
    state = get_state((1,0,2,3,4,5,6,7,8))
    assert up.is_possible(state) == False
    state = get_state((1,2,0,3,4,5,6,7,8))
    assert up.is_possible(state) == False
    state = get_state((1,2,3,0,4,5,6,7,8))
    assert up.is_possible(state) == True

def test_down():
    state = get_state((0,1,2,3,4,5,6,7,8))
    assert down.simulate(state).board == (3,1,2,0,4,5,6,7,8)
    state = get_state((3,1,2,8,4,0,6,7,5))
    assert down.simulate(state).board == (3,1,2,8,4,5,6,7,0)

def test_down_is_possible():
    state = get_state((7,1,2,3,4,5,6,0,8))
    assert down.is_possible(state) == False
    state = get_state((1,6,2,3,4,5,0,7,8))
    assert down.is_possible(state) == False
    state = get_state((1,2,3,0,4,5,6,7,8))
    assert down.is_possible(state) == True
    state = get_state((1,2,5,3,4,0,6,7,8))
    assert down.is_possible(state) == True
    state = get_state((1,4,2,0,7,5,3,6,8))
    assert down.is_possible(state) == True


def test_left():
    state = get_state((1,0,2,3,4,5,6,7,8))
    assert left.simulate(state).board == (0,1,2,3,4,5,6,7,8)
    state = get_state((3,1,2,8,4,0,6,7,5))
    assert left.simulate(state).board == (3,1,2,8,0,4,6,7,5)

def test_left_is_possible():
    state = get_state((0,1,2,3,4,5,6,7,8))
    assert left.is_possible(state) == False
    state = get_state((1,6,2,3,4,5,0,7,8))
    assert left.is_possible(state) == False
    state = get_state((1,2,3,4,0,5,6,7,8))
    assert left.is_possible(state) == True

def test_right():
    state = get_state((0,1,2,3,4,5,6,7,8))
    assert right.simulate(state).board == (1,0,2,3,4,5,6,7,8)
    state = get_state((1,6,2,3,4,5,0,7,8))
    assert right.simulate(state).board == (1,6,2,3,4,5,7,0,8)

def test_right_is_possible():
    state = get_state((1,2,0,3,4,5,6,7,8))
    assert right.is_possible(state) == False
    state = get_state((1,2,0,3,4,5,6,7,8))
    assert right.is_possible(state) == False
    state = get_state((1,6,2,3,4,5,0,7,8))    
    assert right.is_possible(state) == True
