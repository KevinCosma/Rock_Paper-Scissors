from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
        
    def get_selection(self):
        self.choice = random.randint(1,5)
        if self.choice == 1:
            self.choice = "rock"
            print("rock")
        elif self.choice == 2:
            self.choice = "paper"
            print("paper")
        elif self.choice == 3:
            self.choice = "scissors"
            print("scissors")
        elif self.choice == 4:
            self.choice = "lizard"
            print("lizard")
        elif self.choice == 5:
            self.choice = "spock"
            print("spock")
        return self.choice
