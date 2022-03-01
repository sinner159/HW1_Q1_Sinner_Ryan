
import json
from random import random, randrange
import sys
from tree_search.frontier import BFSFrontier
from tree_search.search import TreeSearch
import actions.crypt_puzzle_actions as cpa

word1 = ""
word2 = ""
word3 = ""
if len(sys.argv) < 2:
    word1 = input()
    word2 = input()
    word3 = input()
else:
    word1 = str(sys.argv[1])
    word2 = str(sys.argv[2])
    word3 = str(sys.argv[3])

words = [word1,word2,word3]
s = set()

for word in words:
    for letter in word:
        s.add(letter)

set_letters = list(s)

d = {}
for i, e in enumerate(s):
    d[e] = i

actions = [cpa.IncrementLeftOperand,cpa.IncrementRightOperand,cpa.IncrementResult,cpa.IncrementRemainderValue]
search = TreeSearch(BFSFrontier(),actions,)
print(f"{word1}\n{word2}\n{word3}\n")

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