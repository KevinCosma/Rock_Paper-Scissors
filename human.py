from player import Player

class Human(Player):
    def __init__(self): 
        super().__init__()

    def get_selection(self):
      self.choice = input("Enter 'rock', 'paper', 'scissors', 'lizard', or 'spock'").lower()
