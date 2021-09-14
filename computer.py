from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
        
    def get_selection(self):
        self.choice = random.randint(1,5)
        if self.choice == 1:
            self.choice = "Rock"
            print("Rock")
        elif self.choice == 2:
            self.choice = "Paper"
            print("Paper")
        elif self.choice == 3:
            self.choice = "Scissors"
            print("Scissors")
        elif self.choice == 4:
            self.choice = "Lizard"
            print("Lizard")
        elif self.choice == 5:
            self.choice = "Spock"
            print("Spock")
        return self.choice
