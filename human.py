from player import Player

class Human(Player):
    def __init__(self):
        self.score = 0  
        super().__init__()  
    
    def get_user_input(self):
      self.user_action = input("Enter 'rock', 'paper', 'scissors', 'lizard', or 'spock'")