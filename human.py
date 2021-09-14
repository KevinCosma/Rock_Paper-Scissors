from player import Player

class Human:
    def __init__(self): 
        super().__init__()

    def get_user_input(self):
      self.user_action = input("Enter 'rock', 'paper', 'scissors', 'lizard', or 'spock'").lower()
