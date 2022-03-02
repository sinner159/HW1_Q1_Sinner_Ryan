
import time
from graph_search.node import Node
import sys
from graph_search.frontier import BFSFrontier
from graph_search.search import GraphSearch
import actions.crypt_puzzle_actions as cpa
from states.crypt_puzzle_state import CryptPuzzleState
from states.crypt_puzzle_goal import CryptPuzzleGoal

def get_letters_set(words):
    s = set()
    for word in words:
        for letter in word:
            s.add(letter)
    return list(s)

def get_input():
    words = []
    if len(sys.argv) < 2:
        words.append(input())
        words.append(input())
        words.append(input())
    else:
        words = sys.argv[1:4]
    return words

words = get_input()

s = get_letters_set(words)

letter_values = {}

actions = [cpa.IncrementLeftOperand(),cpa.IncrementRightOperand(),cpa.IncrementResult(),cpa.IncrementRemainderValue()]
search = GraphSearch(BFSFrontier(),actions)

initial_state = CryptPuzzleState(words,{},[0],[0,1,2,3,4,5,6,7,8,9])
root = Node(initial_state, time.time())

goal = CryptPuzzleGoal()
node = search.search(root, goal)
print(words)

# for r in previous_results:
#     json_string = r.replace("'","\"")
#     result_dict = json.loads(json_string)
#     equation = ""
#     for word in words:
#         for letter in word:
#             equation += str(result_dict[letter])
#         equation += "\n"
    
#     print(result_dict)
#     print(equation)