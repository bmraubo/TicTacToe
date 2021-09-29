# TicTacToe
TicTacToe in Python as part of 8thLight Apprenticeship programme

### Set Up Instructions

Application requires Python 3.9.6

```
# Clone the repository
$ git clone https://github.com/bmraubo/TicTacToe.git

# Go into repository
$ cd TicTacToe

# Install dependencies
$ python3 -m pip install --upgrade pip
$ pip3 install -r requirements.txt

# Run the application
$ python3 tictactoe.py

# Run tests
$ python3 -m unittest test_app.py
```

## How it works

### TicTacToe class

The TicTacToe class initializes with:
- a 3x3 matrix of strings containing values from 1-9
- a dictionary of markers X and O
- an empty list of players

Players are added using the create_players method which is run per player and appends a new Player object to the player list. The function has to be run once per player. 

The assign_players method sets the values of X and O to `TicTacToe.players[0]` and `TicTacToe.players[1]` respectively. This assignment is static - `TicTacToe.player[0]` will always be X. However, there is room to change this behaviour either to make the assignment random or to allow the player to select the marker they want.

The board is displayed using the draw_board() method, which uses `TicTacToe.board` as the authoritative source of the current board state. Initially, the available spaces will be filled with the values 1-9 - the use of the index makes no sense given the board set up as a 3x3 matrix (which makes checking win state easier down the line), and is more natural for a non-technically minded player to understand. 

