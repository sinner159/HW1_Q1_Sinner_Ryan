from action import Action
from states.crypt_puzzle_state import CryptPuzzleState

class CryptPuzzleAction(Action):

    def __init__(self, constraints):
        a=0

    def simulate(self, state): 
        new_state = CryptPuzzleState(state.words, state.letter_values, state.remainders, state.domain)
        return state
        
    def internal_simulate(self,state): raise NotImplementedError

    def is_possible(self,state: CryptPuzzleState):
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
        else:
            value1 = state.letter_values[left_letter] 
            value2 = state.letter_values[right_letter]
            result = state.letter_values[result_letter]

            if remainder + value1 + value2 == result % 10:
                state.remainders.append(result//10)
                state.index -= 1
                return True

        return False  
                
    def get_name(self): raise NotImplementedError
    def get_precedence(self): raise NotImplementedError

class IncrementLeftOperand(CryptPuzzleAction):
   def internal_simulate(self, state):
        state.set_current_letter_value(0,state.domain[0])
        return state

class IncrementRightOperand(CryptPuzzleAction):
  def internal_simulate(self, state):
        state.set_current_letter_value(1,state.domain[0])
        return state

class IncrementResult(CryptPuzzleAction):
    def internal_simulate(self, state):
        state.set_current_letter_value(2,state.domain[0])
        return state

class IncrementRemainderValue(CryptPuzzleAction):
    def internal_simulate(self, state):
        state.remainders[state.get_remainder_index()] += 1
        return state