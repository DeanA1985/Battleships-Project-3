# Your code goes here.
import random

# Constants for Battleships Board Representation
MISS_CELL = 'O'
HIT_CELL = 'X'
SHIP_CELL ='S'
EMPTY_CELL = '~'

class BattleshipGame:

    """ Main battleships board class. Sets the board size, the number of ships, the players name 
    and the board type ( player board or the computer) Has methods for adding ships, hits, misses and printing
    the board when the game is over """

    
    def __init__(self):
        self.player_name = ""
        self.grid_size = 0
        self.num_ships = 0
        self.player_board = []
        self.computer_board = []
        self.hits = set()
        self.misses = set()
        self.player_score = 0
        self.computer_score = 0 
        self.game_over = False 

# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
