import sys
from tree_search.frontier import  FrontierFactory
from solvers.tile_solver import TileSolver

print(f"Method passed in: {sys.argv[1]}")
print(f"Board passed in: {str(sys.argv[2])}")


board_as_list = sys.argv[2].split(",")
initial_board = tuple(map(int,board_as_list))

method = sys.argv[1]

factory = FrontierFactory()
frontier = factory.GetFrontier(method)
        

solver = TileSolver()
result = solver.go(frontier, initial_board)

print(result)
f = open("output.txt", "w")
f.write(str(result))


