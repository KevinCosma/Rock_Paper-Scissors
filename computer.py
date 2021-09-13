from player import Player
import random

class Computer:
    def __init__(self):
        self.choice = " "
        
    def get_ai_choice(ai):
        ai.choice = random.randrange(0, 5)
        if ai.choice == 1:
            print("Rock")
        elif ai.choice == 2:
            print("Paper")
        elif ai.choice == 3:
            print("Scissors")
        elif ai.choice == 4:
            print("Lizard")
        elif ai.choice == 5:
            print("Spock")
        return ai.choice
