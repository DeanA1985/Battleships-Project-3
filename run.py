import os
import random

# Constants for Battleships Board Representation
EMPTY_CELL, SHIP_CELL, HIT_CELL, MISS_CELL = "~", "S", "X", "O"

"""This class is designed to initialize various attributes related to the game,
including player information, board sizes, and tracking hits and misses as well
as an integer to keep track of the players score"""


class BattleshipGame:
    def __init__(self):
        self.player_name = ""
        self.grid_size = 0
        self.num_ships = 0
        self.player_board = []
        self.computer_board = []
        self.hits, self.misses = set(), set()
        self.player_score = 0

    """Creates an empty grid. The method relies on two attributes:
    self.grid_size, which creates the dimensions of the grid, and
    EMPTY_CELL, which gives the value of each cell on same grid"""

    def initialize_board(self):
        return [
            [EMPTY_CELL for _ in range(self.grid_size)] for _ in range
            (self.grid_size)
        ]

    """Prints the game board"""

    def print_board(self, board, hide_ships=False):
        for row in board:
            print(
                " ".join(
                    [
                        EMPTY_CELL if cell == SHIP_CELL and hide_ships
                        else cell
                        for cell in row
                    ]
                )
            )
        print()

    """Randomly places ships on the computers board, using a while loop
    to randomly generates coordinates until the required number of ships set
    by self.num_ships is met it places them within the bounds of the board"""

    def place_computer_ships(self):
        ships_placed = 0
        while ships_placed < self.num_ships:
            """This generates random coordinates for ship placement"""
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)

            """Ensure the spot is empty before placing a ship"""
            if self.computer_board[x][y] == EMPTY_CELL:
                self.computer_board[x][y] = SHIP_CELL
                ships_placed += 1

    """Gets row and column guess from the player using input
    validation methods"""

    def get_user_input(self):
        while True:
            try:
                x = int(input(f"Row (0-{self.grid_size - 1}): "))
                y = int(input(f"Column (0-{self.grid_size - 1}): "))
                if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                    return x, y
                print("Coordinates are off the grid. Try Again.")
            except ValueError:
                print("Invalid input. Please enter integers.")

    """Player makes a guess, the result is updated on the board,
    but stops repeat guesses"""

    def make_guess(self, x, y):
        if (x, y) in self.hits or (x, y) in self.misses:
            print("You have already guessed this spot!")
            return False

        if self.computer_board[x][y] == SHIP_CELL:
            print("Hit!")
            self.player_board[x][y] = HIT_CELL
            self.hits.add((x, y))
        else:
            print("Miss!")
            self.player_board[x][y] = MISS_CELL
            self.misses.add((x, y))

        return True

    """Play one round of the game. The method includes: Printing the player's
    board.Printing the computer's board with the ships hidden. Getting user
    input for the coordinates of the guess. Making a guess based on the
    provided coordinates x & y row and column."""

    def play_round(self):
        print(f"\n{self.player_name}'s board:")
        self.print_board(self.player_board)
        print("\nComputer's board (your progress):")
        self.print_board(self.computer_board, hide_ships=True)
        x, y = self.get_user_input()
        self.make_guess(x, y)

    """Setup_game prompts the user to input the grid size and the number
    of ships, initializes two game boards (one for the player and one for
    the computer), and places ships on the computer's board"""

    def setup_game(self):
        self.grid_size = int(input("Enter the grid size (5-10): "))
        self.num_ships = int(input(f"Enter number of ships (1- {self.grid_size}): "))
        """Initialize boards"""
        self.player_board = self.initialize_board()
        self.computer_board = self.initialize_board()
        self.place_computer_ships()

    """Main game loops until all the ships are sunk"""

    def play(self):
        while len(self.hits) < self.num_ships:
            self.play_round()
        print(f"Well Done {self.player_name}, you sunk all the ships!")


"""Prints the games instructions"""


def print_game_instructions():
    print("Welcome to Battleships!\n")
    print("Instructions:")
    print("1. Play on a custom grid")
    print(
        "2. Guess the location of the "
        "computer's ships by entering row/column values."
    )
    print("3. Hits ('X'), Misses ('O'). Sink all ships to win.\n")


"""Main function to start the game"""


def main():
    print_game_instructions()
    game = BattleshipGame()
    game.player_name = input("Please enter your name: ")
    game.setup_game()
    game.play()


if __name__ == "__main__":
    main()
