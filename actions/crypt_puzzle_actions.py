from actions.action import Action
from states.crypt_puzzle_state import CryptPuzzleState

class CryptPuzzleAction(Action):

    def simulate(self, state): 
        new_state = CryptPuzzleState(state.words, state.letter_values, state.remainders, state.domain)
        return state
        
    def internal_simulate(self,state): raise NotImplementedError

    def is_possible(self, state):
        state = self.internal_simulate(state)

        left_letter = state.get_current_letter(0)
        right_letter = state.get_current_letter(1)
        result_letter = state.get_current_letter(2)
        domain = state.domain
        
        if state.get_current_remainder() > 1:
            return False
        
        remainder = state.get_current_remainder()
        if remainder == 0:
            # right most can't be 0 if same and result is diff
            if left_letter == right_letter and right_letter != result_letter and state.get_current_letter_value(0) == 0:
                return False
            elif left_letter == result_letter and state.get_current_letter_value(1) != 0:
                return False
            elif right_letter == result_letter and state.state.get_current_letter_value(0) != 0:
                return False
        
        if left_letter not in state.letter_values or right_letter not in state.letter_values or result_letter not in state.letter_values:
            return False
        
        #select values
        temp_dict = dict()
        for letter in set([left_letter,right_letter, result_letter]):
            temp_dict[letter] = 0
        value1 = temp_dict[left_letter]
        value2 = temp_dict[right_letter]
        result = temp_dict[result_letter]

        if remainder + value1 + value2 == result % 10:
            state.remainders.append(result//10)
            state.index -= 1
            return True

        return False  
                
    def get_name(self): raise NotImplementedError
    def get_precedence(self): raise NotImplementedError

    def assign_values(self,state):
