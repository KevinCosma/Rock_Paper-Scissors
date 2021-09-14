from player import Player

class Game:
    def __init__(self):
        print("Welcome to RPSLS!")
    
        print("Rock crushes Scissors" 
        "Scissors cuts Paper"
        "Paper covers Rock" 
        "Rock crushes Lizard" 
        "Lizard poisons Spock"
        "Spock smashes Scissors"
        "Scissors decapitates Lizard"
        "Lizard eats Paper" 
        "Paper disproves Spock"
        "Spock vaporizes Rock")
    
    def player_choice(self):
        input("Are you playing single player or multiplayer? Type 'single player' or 'multiplayer'")
        if input == "single player":

    def run_game(self):
        pass

    def determine_winner(self):
        pass
    
    def compare_gestures(self):
        pass

    def play_again():
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
