import random 
import math 

class player:
    def __init__(self,letter):
        self.letter = letter
    
    def get_move(self,game):
        pass

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_spaces())
        return square 

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        #firstly we will ask for a place 
        # will check that no other value is there and it is part of the availablespaces 
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn . Input move (0-9): ")
            try: 
                val = int(square)
                if val not in game.available_spaces():
                    raise ValueError
                valid_square = True
            except ValueError:
                print(f"Invalid square. Make sure to input a number between 0-8 and choose an empty square.")

        return val 
     