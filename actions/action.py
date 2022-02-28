
class Action():
    def simulate(self, state): raise NotImplementedError
    def is_possible(self,state): raise NotImplementedError
    def get_name(self): raise NotImplementedError
    def get_precedence(self): raise NotImplementedError


