import sys
from graph_search.frontier import  FrontierFactory
from solvers.tile_solver import TileSolver

print(f"Method passed in: {sys.argv[1]}")
print(f"Board passed in: {str(sys.argv[2])}")


board_as_list = sys.argv[2].split(",")
initial_board = tuple(map(int,board_as_list))

method = sys.argv[1]

#I implemented each search strategy as the frontier class since 
# the actual search algorthm doesn't really differ between the 3
factory = FrontierFactory()
frontier = factory.GetFrontier(method)

solver = TileSolver()
result = solver.go(frontier, initial_board)

print(result)
f = open("output.txt", "w")
f.write(str(result))


