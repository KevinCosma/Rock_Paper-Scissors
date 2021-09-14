from human import Human
from computer import Computer
from player import Player
class Game:
    def __init__(self):
        print("Welcome to RPSLS!")
    
        print("Rock crushes Scissors, " 
        "Scissors cuts Paper, "
        "Paper covers Rock, " 
        "Rock crushes Lizard, " 
        "Lizard poisons Spock, "
        "Spock smashes Scissors, "
        "Scissors decapitates Lizard, "
        "Lizard eats Paper, " 
        "Paper disproves Spock, "
        "Spock vaporizes Rock.")

    def run_game(self):
        self.player_choice()
        self.player_vs_human()
           
    
    def player_choice(self):
        self.ai_game = Game()
        self.human_game = Game()
        input("Are you playing single player or multiplayer? Type 'single player' or 'multiplayer'")
        if input == "single player":
            return self.ai_game.player_vs_ai()
        if input == "multiplayer":
            return self.human_game.player_vs_human()
        else:
            return input
        
    
    def gestures(self):
        self.rock = "rock"
        self.paper = "paper"
        self.scissors = "scissors"
        self.lizard = "lizard"
        self.spock = "spock"        
        "rock" > "scissors"
        "scissors" > "paper"
        "paper" > "rock"
        "rock" > "lizard"
        "lizard" > "spock"
        "spock" > "scissors"
        "scissors" > "lizard"
        "lizard" > "paper"
        "paper" > "spock"
        "spock" > "rock"

    def player_vs_ai(self):
        self.player1 = Player()
        self.ai = Computer()
        self.player1.get_selection()
        self.ai.get_selection()
        if self.player1.get_selection > self.ai.get_selection:
            self.player_score = Player()
            self.player_score.score()
            self.player_score += 1
        elif self.ai.get_selection > self.player1.get_selection:
            self.computer_score = Computer()
            self.computer_score.score()
            self.computer_score += 1

    def player_vs_human(self):
        self.player1 = Player()
        self.player2 = Human()
        self.player1.get_selection()
        self.player2.get_selection()
        if self.player1 > self.player2:
            self.player_score = Player()
            self.player_score.score()
            self.player_score += 1
        elif self.player2 > self.player1:
            self.human_score = Human()
            self.human_score.score()
            self.human_score += 1

    def determine_winner(self):
        if Player.score == 2:
            print("You are the winner")
        if Human.score == 2:
            print("You are the winner")
        if Computer.score == 2:
            print ("You are the winner") 
