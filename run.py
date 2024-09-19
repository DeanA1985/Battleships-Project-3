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
                    x = random.randint(0,
                    self.grid_size - 1)
                    y = random.randint(0,
                    self.grid_size - 1)
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
                                    print("Please enter valid integers.")

                            def make_guess(self, x, y):
                                """ When the player makes a guess the result is updated on the board"""
                                if (x, y) in self.hits or (x, y) in self.misses:
                                    print("This spot has been guessed already!")
                                    return False

                                    if self.computer_board[x][y]== SHIP_CELL:
                                        print("Hit!!!")
                                        self.player_board[x][y] = HIT_CELL
                                        self.hits.add((x, y))
                                        return True
                                    else:
                                        print("Miss!!!")
                                        self.player_board[x][y] = MISS_CELL
                                        self.misses.add((x, y))
                                        return False       

                            def check_win_condition(self):
                                """This function checks to see if all the ships have been hit."""
                                return len(self.hits) == self.num_ships

                            def play_round(self):
                                """Play one round of the game."""
                            print(f"\n{self.player_name}'s
                            board:")

                            self.print_board(self.player_board)

                                 print("\nComputer's board (your progress):")
                            
                            self.print_board(self.computer_board, hide_ships=True)

                            x, y = self.get_user_input()

                            if self.make_guess(x, y):
                                self.player_score += 1
                                else:
                                    self.player_score -= 1

                                    # Shows the updated player board
                                    print(f"\n{self.player_name}'s
                                    updated board:")

                                    self.print_board(self.player_board)

                                    def ask_play_again(self):
                                        """Ask the player if they would like to play again"""
                                    while True:
                                        answer = input("Woulld you like to play another game? (yes/no):").lower()
                                        if answer == 'yes':
                                            return True
                                            elif answer == 'no':
                                                return False
                                            else:
                                                print("Please enter 'yes' or 'no' .")

                                    def setup_game(self):
                                        """Setup the game grid and number of ships"""
                                    while True:
                                        try:
                                            self.grid_size =
                                            int(input("Enter the grid size (5-10): "))
                                            if 5 <=
                                            self.grid_size <= 10:
                                            break 
                                        else:
                                            print("Grid size must be between 5 and 10.")
                                            except ValueError:
                                                print("Please enter a valid integer.")

                                                while True:
                                                    try:
                                                        self.num_ships = int(input(f"Enter the number of ships(1-{self.grid_size}): "))
                                                        if 1 <=
                                                        self.num_ships <= self.grid_size:
                                                        break
                                                    else:
                                                        print(f"Number of ships must be between 1 and {self.grid_size}.")
                                                        except ValueError:
                                                            print("Please enter a valid integer")          

                                                    
                                                



                
        

# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
