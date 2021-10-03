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
$ python3 -m unittest -v 
```

## How it works

### TicTacToe class

The TicTacToe class initializes with:
- a 3x3 matrix of strings containing values from 1-9
- an empty dictionary for markers
- an empty list of players

*LEGACY - Players are added using the create_players method which is run per player and appends a new Player object to the player list. The function has to be run once per player.*

A get_player_info() function runs in UserInterface class (formerly Info class) and obtains the name and type of two players from the user. This limits errors by ensuring there will always be two users. This returns an array with two objects in the format `[name, type]`. The create_players() method loops over the two players and creates Player objects for each.

*LEGACY - The assign_players method sets the values of X and O to `TicTacToe.players[0]` and `TicTacToe.players[1]` respectively. This assignment is static - `TicTacToe.player[0]` will always be X. However, there is room to change this behaviour either to make the assignment random or to allow the player to select the marker they want.* 

In order to make making a move easier, I have used the Player object as the key in the markers dictionary, and assigned the markers as values to those keys. I have a feeling that markers and players could be combined, but I am saving that for refactoring.

The board is displayed using the draw_board() method, which uses `TicTacToe.board` as the authoritative source of the current board state. Initially, the available spaces will be filled with the values 1-9 - the use of the index makes no sense given the board set up as a 3x3 matrix (which makes checking win state easier down the line), and is more natural for a non-technically minded player to understand.

### User input and validation

The game takes user input as a string and validates it using the validate_player_move method which checks for Out of Range, Value errors and if the move has already been played. Feedback is given to the user to inform them of what went wrong. The user can try again to input a valid move. 

The move is then played using the make_move method, which uses floor division and modulo to determine which square is to be replaced with the player marker (X or O). Quite proud of this one:

```
def make_move(self, player, move):
        self.board[(move - 1) // 3][(move - 1) % 3] = self.markers[player]
```

So clean.

### Gameplay loop

Starting with X, each player has a chance to input a move, which is then validated. Valid moves are played. Moves are rejected if that move has already been played, if the value entered is outside the permitted range, and potential ValueErrors are handled.

Moves are played until a winning condition is met, or until 9 moves have been played. 

### Win state check and game exit

After every move is played, the game checks whether the player making the move has won the game. The end_game functions checks whether the game should end by running win_check and declaring a winner if win_check returns True, or declaring a draw if 9 moves have been played. 

The order of logic means win_check will be conducted before a draw is declared, in case someone wins on the last move. 

The win_state check includes a nested tally() function that takes in an arrangement of board values. When checking rows, it checks each object in the board list - nothing needs to be changed. Checking columns and diagonals requires a specific arrangement of board values, which are defined as the columns and diagonals variables within the win_state function.

If the game has reached the end by win or draw, it exits gracefully, and tells the user that it is doing so.

### Some Refactoring...

The TicTacToe class was getting too big; it handles the player creation, the board, the win validation, and the game logic. Players may be a separate class, but it does very little but allow for identifiable objects that store the name and player type of the player and can be assigned with markers.

As a first step the refactor:

- Separates work done by TicTacToe class to the Board and TicTacToe class. TicTacToe class deals with setting up and executing the gameplay loop. It still deals with player creation, but that will likely need to be revisited.
- The has been restored and tasked with creating and drawing the board, making modifications to the board (through making and validating the player moves), and conducting checks on the board to see if there is a winner. 
- Classes are now contained within separate files, with corresponding testing documents. ReadMe instructions updated to reflect this, as has the GitHub actions workflow.

Next refactoring steps:
- Decide whether User Interface should take over responsibility for requesting and validating player moves.
- Get rid of markers from TicTacToe and give Player the marker attribute.
- Revisit the player class. If we could change the way that players are added then modularity could be increased. Since the potential for different board sizes could be in the game, why not the potential for different number of players
- Give markers colour assignments. If we add more players we will need more markers.

Further functionality:
- Allow creating board of N*N size, as well as unlimited? number of players, each with their own marker. Distinguish markers by colour. 



