from random import choice
class Borracho:
    def __init__(self,name):
        self.name = name

class BorrachoTradicional(Borracho):
    def __init__(self, name):
        super().__init__(name)
    def camina():
        return choice([(0,1),(0,-1),(1,0), (-1,0)])
    
    