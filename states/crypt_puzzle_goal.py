from states.crypt_puzzle_state import CryptPuzzleState
from .goal_state import Goal
from graph_search.node import Node

class CryptPuzzleGoal(Goal):

    # def is_goal_state(self, node: Node):

    #     state:  CryptPuzzleState = node.state
    #     word1 = state.words[0]
    #     word2 = state.words[1]
    #     word3 = state.words[2]
    #     smaller_word = word1 if len(word1) < len(word2) else word2
    #     index = -1
    #     remainder = 0
    #     while abs(index) <= len(smaller_word):
    #         letter1 = word1[index]
    #         letter2 = word2[index]
    #         result_letter = word3[index]
        
    #         state.remainders[abs(index) - 1] + state.letter_values[letter1] + state.letter_values[letter2] == state.letter_values[result_letter] + state.remainders[abs(index)]
        
    #         remainder = sum // 10
    #         result_digit = sum % 10 

    #         if state.letter_values[result_letter] != result_digit:
    #             return False
        
    #         index -= 1

    #     while abs(index) <= len(word1):
    #         letter1 = word1[index]
    #         sum = remainder + state.letter_values[letter1]
        
    #         remainder = sum // 10
    #         result_digit = sum % 10 

    #         if d[result_letter] != result_digit:
    #             return False
        
    #         index -= 1

    #     while abs(index) <= len(word2):
    #         letter2 = word2[index]
    #         sum = remainder + state.letter_values[letter2]
        
    #         remainder = sum // 10
    #         result_digit = sum % 10 

    #         if state.letter_values[result_letter] != result_digit:
    #             return False
        
    #         index -= 1
        
    #     if remainder != state.letter_values[word3[0]]:
    #         return False

    #     return True
    def is_goal_state(self,node: Node):
        state:  CryptPuzzleState = node.state
        if len(state.letter_values) == 0:
            return False
        word1 = state.words[0]
        word2 = state.words[1]
        word3 = state.words[2]
        smaller_word = word1 if len(word1) < len(word2) else word2
        index = -1
        remainder = 0
        while abs(index) <= len(smaller_word):
            letter1 = word1[index]
            letter2 = word2[index]
            result_letter = word3[index]
            if letter1 not in state.letter_values or letter2 not in state.letter_values or result_letter not in state.letter_values:
                return False
            sum = remainder + state.letter_values[letter1] + state.letter_values[letter2]
        
            remainder = sum // 10
            result_digit = sum % 10 

            if state.letter_values[result_letter] != result_digit:
                return False
        
            index -= 1

        while abs(index) <= len(word1):
            letter1 = word1[index]
            sum = remainder + state.letter_values[letter1]
        
            remainder = sum // 10
            result_digit = sum % 10 

            if d[result_letter] != result_digit:
                return False
        
            index -= 1

        while abs(index) <= len(word2):
            letter2 = word2[index]
            sum = remainder + state.letter_values[letter2]
        
            remainder = sum // 10
            result_digit = sum % 10 

            if state.letter_values[result_letter] != result_digit:
                return False
        
            index -= 1
        
        if remainder != state.letter_values[word3[0]]:
            return False

        return True

