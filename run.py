# Your code goes here.
import random

# Constants for Battleships Board Representation
MISS_CELL = 'O'
HIT_CELL = 'X'
SHIP_CELL ='S'
EMPTY_CELL = '~'

class BattleshipGame:

    """ Main battleships board class. Sets the board size, the number of ships, the players name 
    and the board type ( player board or the computer) Has methods for adding ships, hits, misses and printing the scores,
    for each round as well as printing the board when the game is over """

    
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

        def initialize_board(self):
            """Creates an empty grid based on size set by user."""
            return [[EMPTY_CELL for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        
        def print_board(self, board, hide_ships=False):
            """Prints the game board."""
            for row in board:
                if hide_ships:
                    print(''.join([EMPTY_CELL if cell == SHIP_CELL else cell for cell in row]))
                else:
                    print('  '.join(row))
                print()

        def place_computer_ships(self):
            """This places ships randomly on the computer's board (playable grid)"""
            for _ in range(self.num_ships):
                 while True:
                    x = random.randint(0,self.grid_size - 1)
                    y = random.randint(0,self.grid_size - 1)
                    if 
                    self.computer_board[x][y] == EMPTY_CELL:

                    self.computer_board[x][y] = SHIP_CELL 
                    break

                def get_user_input(self):
                    """ Gets the row and column guess from the player with input validation."""
                    while True:
                        try:
                            x = int(input(f"Enter row (0 to {self.grid_size - 1})"))
                            y = int(input(f"Enter column (0 to {self.grid_size - 1})"))
                            if 0 <= x <
                            self.grid_size and 0 <= y <
                            self.grid_size:
                            return x, y 
                            else:
                                print ("These coordinates are off the grid. Please try again")
                                except ValueError:
                                    print("Please enter valid integers")

                
        

# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
