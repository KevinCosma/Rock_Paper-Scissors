from player import Player
import random

class Computer:
    def __init__(self):
        self.score = 0
        
    def get_ai_choice(self):
        self.choice = random.randint(1, 5)
        if self.choice == 1:
            print("Rock")
        elif self.choice == 2:
            print("Paper")
        elif self.choice == 3:
            print("Scissors")
        elif self.choice == 4:
            print("Lizard")
        elif self.choice == 5:
            print("Spock")
        return self.choice
