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
            """Creates an empty grid filled with "~" empty cells the size of the grid is determined by
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
             """Play one round of the game."""
             self.print_board(self.player_board)
             
             self.print_board(self.computer_board, hide_ships=True)
             x, y = self.get_user_input()
             self.make_guess(x ,y)
             
            

                            def setup_game(self):
                                        """Setup the game grid and number of ships"""
                            while True:
                                        try:
                                            self.grid_size = int(input("Enter the grid size (5-10): "))
                                            if 5 <= self.grid_size <= 10:
                                               break
                                            else:
                                             print("Grid size must be between 5 and 10.")
                                        except ValueError:
                                                print("Please enter a valid integer.")

                                                while True:
                                                    try:
                                                        self.num_ships = int(input(f"Enter the number of ships(1-{self.grid_size}): "))
                                                        if 1 <= self.num_ships <= self.grid_size:
                                                           break
                                                        else:
                                                             print(f"Number of ships must be between 1 and {self.grid_size}.")
                                                    except ValueError:
                                                            print("Please enter a valid integer.")

                                                            # Intitalize the boards (grids) for the player and the computer
                                                            self.player_board = self.initialize_board()
                                                            self.computer_board = self.initialize_board()

                                                            #Place ships on the computer's board
                                                            self.place_computer_ships()

                                                            def show_computer_board(self):
                                                                """Show the computer's board with ships visible."""
                                                                print("\nComputer's board (Ships revealed):")

                                                            self.print_board(self.computer_board)

                                                            #Play Game 
                                                            def play(self):
                                                                """ Main Game Loop."""
                                                                print(f"Welcome, {self.player_name}! Let's start the game!")
                                                                self.game_over = False

                                                                while not self.game_over:
                                                                    self.play_round()

                                                            if self.check_win_condition():

                                                                print(f"Congratulations, {self.player_name}! You sunk all the ships!") 
                                                                self.game_over = True
                                                                self.computer_score += self.num_ships

                                                                if self.game_over:
                                                                    print(f"Your final score: {self.player_score} | Computer score: {self.computer_score}")

                                                                    #Shows the computer's board at the end of the game

                                                                    self.show_computer_board()
                                                                    if not self.ask_play_again():
                                                                                    print ("Thanks for playing Battleships! Goodbye!")
                                                                    break 
                                                                else:
                                                                    self.game_over = False
                                                                    self.setup_game()

                                                            def print_game_instructions():
                                                                """Prints the game instructions for the player."""
                                                            print("Welcome to Battleships!")
                                                            print("\nInstructions:")
                                                            print("1. You will be playing on a customizable grid.")    
                                                            print("2. You can choose how many ships to play with (within the grid size).")  
                                                            print("3. Guess the location of the computer's ships by entering row and column values.")
                                                            print("4. The game will show your hits as ('X') and your misses as ('O'). ")
                                                            print("5. The computer's board will show your progress as you play.")
                                                            print("6. The game ends when you sink all of the computers ships or you quit.")
                                                            print("7. You can quit the game after each round by pressing 'n' .")


                                                            def main():
                                                                """Main function to start the game."""
                                                                
                                                                print("Game Started!")
                                                                
                                                                print_game_instructions() 

                                                                game = BattleshipGame()

                                                                while True:
                                                                    game.player_name = input("Please enter your name:  ")
                                                                game.setup_game()
                                                                game.play()

                                                                if input("Press any key to continue or 'n' to quit: ").lower() == 'n': 
                                                                  print(f"Final Score: {game.player_name}: {game.player_score} | Computer: {game.computer_score}")
                                                                  print("Thanks for playing!")
                                                                else:
                                                                  # Continue with the game logic here
                                                                 pass

                                                                if __name__ == "__main__":
                                                                  main()              
                                                                                    
                                                    
                                                            


                                                



                
        

# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
