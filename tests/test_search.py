import os, sys
import pytest
from solvers.tile_solver import TileSolver
from solvers.result import Result
from graph_search.frontier import FrontierFactory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture
def factory():
    yield FrontierFactory()


@pytest.mark.parametrize ("number,method,board,expected", [\
    (1,"dfs",(6,1,8,4,0,2,7,3,5),Result(['Up','Left','Down','...','Up','Left','Up','Left'], 46142, 51015, 46142, 46142)),\
    (2,"bfs",(6,1,8,4,0,2,7,3,5),Result(['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], 20, 54094, 20, 21)),\
    (3,"ast",(6,1,8,4,0,2,7,3,5),Result(['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up','Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], 20, 711, 20, 20)),\
    
    (4,"bfs",(1,2,5,3,4,0,6,7,8),Result(['Up', 'Left', 'Left'], 3, 10, 3, 4)),\
    (5,"dfs",(1,2,5,3,4,0,6,7,8),Result(['Up', 'Left', 'Left'], 3, 181437, 3, 66125)),\
    (6,"ast",(1,2,5,3,4,0,6,7,8),Result(['Up', 'Left', 'Left'], 3, 3, 3, 3)),\

    (7,"dfs",(8,6,4,2,1,3,5,7,0),Result(['Up', 'Up', 'Left', '...',  'Up', 'Up', 'Left'], 9612, 9869, 9612, 9612)),\
    (8,"bfs",(8,6,4,2,1,3,5,7,0),Result(['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left'], 26, 166786, 26, 27)),\
    (9,"ast",(8,6,4,2,1,3,5,7,0),Result(['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up','Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left'], 26, 1801, 26, 26)),\
    
    (10,"bfs",(3,1,2,0,4,5,6,7,8),Result(['Up'], 1, 1, 1, 1)),\
    (11,"dfs",(3,1,2,0,4,5,6,7,8),Result(['Up'], 1, 1, 1, 1)),\
    (12,"ast",(3,1,2,0,4,5,6,7,8),Result(['Up'], 1, 1, 1, 1)),\

    (13,"bfs",(8,6,7,2,5,4,3,0,1),Result(['Up', 'Right', 'Down', 'Left', 'Up', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Right', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up'], 27, 176296, 27, 28)),\
    (14,"dfs",(8,6,7,2,5,4,3,0,1),Result(['Up', 'Up', 'Left', 'Down', 'Down', 'Right','...','Right', 'Right', 'Down', 'Down', 'Left', 'Up', 'Up', 'Left'], 63413, 111244, 63413, 66123)),\
    (15,"ast",(8,6,7,2,5,4,3,0,1),Result(['Up', 'Right', 'Down', 'Left', 'Up', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Right', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up'], 27, 4416, 27, 27)),\

    (16,"bfs",(8,1,2,0,4,3,7,6,5),Result([], 0, 181440, 0, 31)),\
    (17,"dfs",(8,1,2,0,4,3,7,6,5),Result([], 0, 181440, 0, 66056)),\
    (18,"ast",(8,1,2,0,4,3,7,6,5),Result([], 0, 181440, 0, 31))\
])
def test_search(number,method,board, expected,factory):
    solver = TileSolver()
    frontier = factory.GetFrontier(method)
    result = solver.go(frontier,board)
    validate_path_to_goal(expected, result)
    assert result.cost_of_path == expected.cost_of_path
    if method != "ast":
        assert result.nodes_expanded == expected.nodes_expanded
    assert result.search_depth == expected.search_depth
    assert result.max_search_depth == expected.max_search_depth

def validate_path_to_goal(expected, result):
    
    index_of_ellipses = find_ellipses_index(expected)
        
    if index_of_ellipses == -1:
        for i, action in enumerate(expected.path_to_goal):
            assert action == result.path_to_goal[i]
    else:
        for i, action in enumerate(expected.path_to_goal[0:index_of_ellipses]):
            assert action == result.path_to_goal[i]

        path_after_ellipses = expected.path_to_goal[index_of_ellipses + 1:]
        length = len(path_after_ellipses)

        for i, action in enumerate(path_after_ellipses):
            assert action == result.path_to_goal[-length + i]

def find_ellipses_index(expected):
    index_of_ellipses = -1
    try:
         index_of_ellipses = expected.path_to_goal.index('...')
    except ValueError:
        index_of_ellipses = -1
    
    return index_of_ellipses
