
# Battleship Game
This is a terminal based version of the classic Battleship game where you play against the computer. You will set up a custom grid and choose the number of ships to place on the grid. The objective all the game is to sink all of the computer's ships by guessing their locations in the grid.


## Description
Your goal is to sink all of the computer's ships by guessing their positions. The game is fully customizable, allowing you to set up the grid size and the number of ships that you want to place on the board. The game incorporates error handling for invalid inputs like placing text where there should be numbers. 

## Games Rules
 - The game is played on a square grid where you choose the size (try to keep grids in mutliples of ten for effective game play although there is no max limit only to the size of the terminal width)
 - You and the computer each have a number if ships randomly placed on the grid.
- On each turn you are asked to guess a location row and column to strike.
- The game will tell you if you hit or miss a ship
- The goal is to sink all of the computer's ships by hitting all of their positions 
- After sinking all of the ships the game is complete.

## Features
- Customisable Grid : You can choose the size of the game board there are no limits to my game, although for better functionality and gameplay it is advised to keep the grid as small as possible .
- Number of Ships : You can decide how many ships you wish to place on the board but the only parameters are the board size for example if your choose a 5 x 5 grid you cannot exceed 25 ships so a safe number in that case would be having 10 ships so that you can have space for empty cells which would enable misses.
- PEP8 Compliant: The game has been put through linter however there are 5 lines of code that exceed the 79 character limit. I have tried to shorten them and ident them however doing do causes functionality issues in the working code so I have mentioned them here: 

## System Requirements 
- To run the game you need to have Python3 installed on your system

## How to Play the Game
- When the game starts , you will be greeted with a message and some game instructions.
- You must enter your name, you will be prompted to enter your name, which will be used throughout the game.
- Once you have entered your name you will be prompted to setup a grid where you can determine the size of your playable area. If you choose a 5 x 5 grid then you can have a maximum then there will be 25 cells, it may be a good idea to keep the number of ships down to a minumum to make the game challenging and to give opportunity to create a balanced amount of misses to hits.

- You will then be asked to add a number of ships to your grid, choose a number and it will disperse the ships 

- Make guesses, by entering the row an column values. The game will tell you if you hit a ship or miss a ship
You will be able to view the amount of ships you have on your side however the computers ships will be hidden from you. The game through inout validation will not allow you to enter the same guess twice. If your coordinates are off the grid the game will tell you to try again.
- The game ends when all ships are sunk you will receive a message that either the computer has sunken all of your ships or you have won by sinking all of the comouter's ships.


1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
