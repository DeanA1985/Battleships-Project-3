!
# Battleship Game
This is a terminal based version of the classic Battleship game where you play against the computer. You will set up a custom grid and choose the number of ships to place on the grid. The objective all the game is to sink all of the computer's ships by guessing their locations in the grid.


## Description
Your goal is to sink all of the computer's ships by guessing their positions. The game is fully customizable, allowing you to set up the grid size and the number if ships that you want to place on the board. The game incorporates error handling for invalid inputs like placing text where there should be numbers. 

## Games Rules
 - The game is played on a square grid where you choose the size (from 5x5 to 10x10).
- On each turn you are asked to guess a location row and column to strike.
- The game will tell you if you hit or miss a ship
- The goal is to sink all of the computer's ships by hitting all of their positions 
- After sinking all of the ships the game is complete.

## Features
- Customisable Grid : Choose the size of the game board (5x5 to 10x10).
- Number of Ships : You can decide how many ships you wish to place on the board but the only parameters are the board size.
- PEP8 Compliant: The game is 



1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
