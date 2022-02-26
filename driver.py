from math import log2
import sys
from frontier import  FrontierFactory
from solver import Solver

print(f"Method passed in: {sys.argv[1]}")
print(f"Board passed in: {str(sys.argv[2])}")


board_as_list = sys.argv[2].split(",")
initial_board = tuple(map(int,board_as_list))

method = sys.argv[1]


num_tiles = len(initial_board)
nth_tile =  num_tiles - 1

#Getting n in 2^n which helps with boundary calculation later
exponent = log2(nth_tile)

factory = FrontierFactory(exponent)
frontier = factory.GetFrontier(method)
        

solver = Solver(nth_tile,exponent)
result = solver.go(frontier, initial_board)

print(result)
f = open("output.txt", "w")
f.write(str(result))


