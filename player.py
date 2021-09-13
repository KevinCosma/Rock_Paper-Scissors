from random import choice


class Player:
    def __init__(self,name):
        self.name = " "
        self.score = 0
        self.choice = None

          def choose(self):
            self.choice = int(raw_input("Rock [1] Paper [2] Scissors [3] Lizard [4] Spock [5]"))
            return self.choice
            
    
