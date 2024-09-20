# Your code goes here.
import random

# Constants for Battleships Board Representation
EMPTY_CELL, SHIP_CELL, HIT_CELL, MISS_CELL = '~','S','X','O'

"""EMPTY_CELL: Represented by '~', indicates a cell that has not been occupied by a ship or hit.
SHIP_CELL: Represented by 'S', indicates a cell that contains a ship.
HIT_CELL: Represented by 'X', indicates a cell that has been hit by a player's attack.
MISS_CELL: Represented by 'O', indicates a cell that has been targeted but does not contain a ship."""

class BattleshipGame:
    
    """Initial setup for game, initialises several attributes that manage the games state. These
    attributes include the players name, the size of the playable grid, the number of ships, two boards
    one for the player and the computer, it also initialises sets to track hits and misses and a running score
    for the player"""

    def __init__(self):
        self.player_name = ""
        self.grid_size = 0
        self.num_ships = 0
        self.player_board = []
        self.computer_board = []
        self.hits, self.misses = set(), set()
        self.player_score = 0
        
        def initialize_board(self):
            """Creates an empty grid filled with "~" empty cells, the size of the grid is determined by
            the grid size attribute"""
            return [[EMPTY_CELL for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        
        def print_board(self, board, hide_ships=False):
            """Print the game board, for printing a game board,
            which is represented as a 2-dimensional list, 'hide_ships' determines whether the ships should be hidden when 
            printing the board if hide_ships is set to true the method replaces ship cells with a value of EMPTY cell"""
            for row in board: print (''.join([EMPTY_CELL if cell == SHIP_CELL and hide_ships else cell for cell in row]))
            print()

        def place_computer_ships(self): 
            """This places ships randomly on the computer's board (playable grid)
            The method uses a loop to place each ship at a random coordinate
            on the grid until a valid position (an empty cell) is found. 
            Once a valid position is identified, the ship is placed,
            and the loop continues until all ships are placed."""
        for _ in range(self.num_ships):
            while True:
                x, y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
                if self.computer_board[x][y] == EMPTY_CELL:
                    
                    self.computer_board[x][y] = SHIP_CELL 
                    break

                def get_user_input(self):
                    """This method uses input validation to ensure that the entered coordinates
                    are within the valid range defined by self.grid_size. If the input is invalid,
                    the user is told to try again until valid coordinates are provided.
                    The method handles exceptions to catch non-integer inputs like text "abc" and informs
                    the user accordingly.."""
                    while True:
                        try:
                            x, y = int(input(f"Row (0-{self.grid_size - 1}): ")), int(input(f"Column (0-{self.grid_size - 1}): "))
                            if 0 <= x < self.grid_size and 0 <= y < self.grid_size: 
                                return x, y 
                            print("Coordinates are off the grid. Try Again.")
                        except ValueError:
                            print("Invalid input. Please enter integers.")

                def make_guess(self, x, y):
                    """Player makes a guess and the result is updated on the board
                    it checks to see if coordinates have been guessed and prevents you
                    from making repeat guesses"""
                    
                    if (x, y) in self.hits or (x, y) in self.misses:
                        print("You have already guessed this spot!")
                        return False
                    if self.computer_board[x][y] == SHIP_CELL: print("Hit!") 
                    self.player_board[x][y] = HIT_CELL
                    self.hits.add((x, y)) 
            else:
                    print("Miss!")
                    self.player_board[x][y]= MISS_CELL
                    self.misses.add((x, y))
                    return True
                                   
            def play_round(self):
             """Play one round of the game: this method executes a single round of the game
             It prints both boards for the player and the computer while hiding the position of the ships
             on the computers board, indicating the player cannot see the computers ships. It also retrieves
             user input for the coordinates of the players guess using the "get user input" method"""
             self.print_board(self.player_board)
             
             self.print_board(self.computer_board, hide_ships=True)
             x, y = self.get_user_input()
             self.make_guess(x ,y)
             
            def setup_game(self):
              """Sets up the game grid and number of ships. Prompts the user for input to set up the game.
              Initializes the game boards.Calls another method to place ships on the computer's board which is 
              'self.place_computer_ships'."""
            self.grid_size = int(input("Enter the grid size (5-10): "))
            self.num_ships = int(input(f"Enter number of ships (1- {self.grid_size}): "))
            self.player_board = self.initialize_board()
            self.computer_board = self.initialize_board()
            self.place_computer_ships()
            
            def play(self):
                """Main game loop. The method serves as the main game loop, which continues
                to execute rounds of play until a certain condition is met (all ships are sunk). Specifically, 
                it checks if the number of hits (successful attacks on ships) is less than
                the total number of ships (self.num_ships). Once all ships are sunk, it prints
                a congratulatory message to the player telling them they have sunk all the ships."""
                while len(self.hits) < self.num_ships:
                    self.play_round()
                    print(f"Well Done {self.player_name}, you sunk all the ships!")
                    
                    
            def print_game_instructions():
                """ Defines a function named print_game_instructions, which is designed to display the instructions
                for the game. This function prints a welcome message followed by a set of instructions that
                guide the player on how to play the game. The instructions outline the gameplay mechanics, 
                including the grid setup, how to make guesses, and the symbols used to indicate hits and misses"""
                
                print("Welcome to Battleships!\n")
                print("Instructions:")        
                print("1. Play on a custom grid")
                print("2. Guess the location of the computer's ships by entering row and column values.")
                print("3 Hits ('X'), Misses ('O'). Sink all ships to win.\n")
                    
            def main ():
                """Main function to start the game 
                The function begins by printing game instructions,
                then creates an instance of the BattleshipGame class, prompts the user to enter their name,
                sets up the game, and finally starts the game."""


                print_game_instructions()
                game = BattleshipGame()
                game.player_name = input("Please enter your name: ")
                game.setup_game()
                game.play()
                
                if __name__ == "__main__":
                    main()
                    
            
            
                                            
                                            

                                                           



# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
