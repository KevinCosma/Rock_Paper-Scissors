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
        self.player_vs_ai()
        self.player_vs_human()
           

    def player_choice(self):
        self.ai_game = Game()
        self.human_game = Game()
        input("Are you playing single player or multiplayer? Type 'single player' or 'multiplayer'")
        if input == "single player":
            return self.ai_game.player_vs_ai()
        if input == "multiplayer":
            return self.human_game.player_vs_human()

    def player_vs_ai(self):
        self.player1 = Player()
        self.ai = Computer()
        self.player1.get_selection()
        self.ai.get_selection()
        if self.player1.choice == "rock" and (self.ai.choice == "lizard" or self.ai.choice == "scissors"):
            print("Player 1 Wins!")
            self.player1.score += 1
        elif self.player1.choice == "scissors" and (self.ai.choice == "lizard" or self.ai.choice == "paper"):
            print("Player 1 Wins!")
            self.player1.score += 1
        elif self.player1.choice == "paper" and (self.ai.choice == "rock" or self.ai.choice == "spock"):
            print("Player 1 Wins!")
            self.player1.score += 1
        elif self.player1.choice == "spock" and (self.ai.choice == "scissors" or self.ai.choice == "rock"):
            print("Player 1 Wins!")
            self.player1.score += 1
        elif self.player1.choice == "lizard" and (self.ai.choice == "spock" or self.ai.choice == "paper"):
            print("Player 1 Wins!")
            self.player1.score += 1   
        elif self.player1.choice == self.ai.choice:
            print("Its a tie!")
        elif self.ai.choice == "rock" and (self.player1.choice == "lizard" or self.player1.choice ==  "scissors"):
            print("Computer Wins!")
            self.ai.score += 1
        elif self.ai.choice == "scissors" and (self.player1.choice == "lizard" or self.player1.choice == "paper"):
            print("Computer Wins!")
            self.ai.score += 1
        elif self.ai.choice == "paper" and (self.player1.choice == "rock" or self.player1.choice == "spock"):
            print("Computer Wins!")
            self.ai.score += 1
        elif self.ai.choice == "spock" and (self.player1.choice == "scissors" or self.player1.choice == "rock"):
            print("Computer Wins!")
            self.ai.score += 1
        elif self.ai.choice == "lizard" and (self.player1.choice == "spock" or self.player1.choice == "paper"):
            print("Computer Wins!")
            self.ai.score += 1
        elif self.player1.choice != "rock" "paper" "scissors" "lizard" or "spock":
            print("Please enter valid input!")
    
    def player_vs_human(self):
        self.player1 = Player()
        self.player2 = Human()
        self.player1.get_selection()
        self.player2.get_selection()

    def determine_winner(self):
        if Player.score == 2:
            print("You are the winner")
        if Human.score == 2:
            print("You are the winner")
        if Computer.score == 2:
            print ("You are the winner") 
