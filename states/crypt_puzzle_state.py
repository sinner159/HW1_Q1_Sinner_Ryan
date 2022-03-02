from .state import State
class CryptPuzzleState(State):

    def __init__(self, words, letter_values, remainders, domain):
        self.domain = domain
        self.words = words
        self.letter_values = letter_values
        self.index = -1
        self.remainders = remainders #initial [0] either 0 or 1
        self.need_leading_1_in_result = len(words[2]) > len(words[0]) and len(words[2]) > len(words[1])
        if self.need_leading_1_in_result and 1 in self.domain:
            self.domain.remove(1)
            self.letter_values[words[2][0]] = 1
        
    def get_current_remainder(self):
        return self.remainders[abs(self.index) - 1]
    
    def set_current_remainder(self, value):
        self.remainders[abs(self.index) - 1] = value

    def get_current_letter(self, word):
        return self.words[word][self.index]

    def set_current_letter_value(self,word, value):
        self.letter_values[self.words[word][self.index]] = value

    def get_current_letter_value(self,word):
        return self.letter_values[self.words[word][self.index]]

    def get_remainder_index(self):
        return abs(self.index) - 1
    
    def __hash__(self):
        return hash(frozenset(self.letter_values.items())) + hash(self.index)


    