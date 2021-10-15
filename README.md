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

## w/c 04 October 2021 Redesign

### Redesigning to allow for new data structures

The previous refactor means that only the Board class will have to be changed to facilitate the use of a new data structure.

To further encapsulate the data structure, a check_value() method will be added that will be the sole means of communication between the data structure and the methods that require data. Any references to the 2D matrix will be removed from the Board methods, and replaced by calling check_value for the relevant fields. 

Due to a *small* oversight, make_move() would also have to access the board data. So make_move has been killed and replaced by a conditional statement within check_value... check_value now takes the value to be checked, and an optional new_value (which defaults to None). If there is no new_value, check_value will return the current value of that position on the board. However, if there is a new value, check_value will replace the old value with the new one, and return that. 

Perhaps check_value should be renamed to better reflect its greater role. query_board? **access_board?**

So references to the 2D matrix have been replaced with calls to access_board. This also meant that an additional description of the rows had to be added to win_check, as previously the method would rely on the 'as is' board implementation to check rows.

**This behaviour has now been changed - 2 methods control board access: check_board_value and change_board_value. This has been done in order to enhance clarity of the code - 14 October 2021**

### Changing data structure

With the above changes made, I have changed the initialize_board test to expect a dictionary, and modified access_board to look up keys in a dictionary. All tests pass.

### Adding functionality for 3x3 and 4x4 boards

So we start in a position where 3x3 boards already work. In order to reduce reliance on if/else conditionals, we want the board to be created dynamically based on the size value. 

One of the considerations when moving from a 3x3 board to a 4x4 board is that we will be dealing with double digits, which break the draw_board set up - there will be one more character to account for in some of the squares.

This means that the work that will be done to allow for a 4x4 will also in effect allow a 5x5, 6x6 etc board. But tests will only be run for 3x3 and 4x4. 

Users will be allowed to create a 8x8 board, for example - if they really need to scratch that itch - but will be warned that it is not supported and asked for confirmation if they want to continue.

Dynamic board generation has a number of knock on effects, including making win checks dynamic, which can only really be done algorithmically.

Tests have been added to check 4x4 implementation on various functions of the app.

Some minor points regarding user feedback messages - they are now dynamic.

#### User input of board size

Get_board_size asks the player to enter a value when the app is launched, that choice is validated to ensure that nothing truly stupid is entered. If the value is not 3 or 4, the player is asked whether they want to continue. 

Based on some random manual tests, a value of 1 will break the game, and about 25 you will struggle to display the board (and get bored before you can finish the game).

#### Board generation

Board generation is based on size - generate_board() creates a list of all board numbers and then uses access_board populate the dictionary on the basis of that list. 

#### Drawing the board

Uses size to determine the width of the board, and creates a grid accordingly. The biggest issue was the need for the board spacing to be dynamic due to the presence of double figures. 

This was accomplished by using an abstract display_size_modifier that is set to be `len(str(highest value on the board)) + 2` - so in a 4x4 board, that would be 16: 2+2 = 4.

The nested print_row function goes through the values that need to be displayed on that row, and adds them to the base '|' string, adjusting the space between | and the value by reference to the display_size_modifier. 

This has greatly increased the work done be the draw_board method, so it has been moved out of the Board class into its own Display class. 

#### Win checks 

The challenge here was defining possible win arrangements algorithmically - again avoiding if/else statements that have a static definition based on whether it is a 3x3 or 4x4 board. 

The problem here was that each type of arrangement required a slightly different computation in order to place the right values in the right order, especially if this was always going to be right irrespective of board size. 

The first attempt at doing this used a config modifier dictionary that applies the correct algorithm to the relevant situation. However, this quickly started becoming unwieldy - and the resulting generate_arrangements method started hitting 50 lines of code. 

Attempt number 2 relied on one line for loops for each arrangement: a master list is initially created of all values from 1 to highest value. This master list is then sliced up based on the specific requirements of the arrangement. 

All arrangements are then returned as one dictionary. 

As this solution relies on the numerical board values (and not any markers that may have been placed), the nested tally function within the win_check method needed to be redesigned to make access_board calls to obtain any markers that may be in those positions.

The benefit is that one the arrangements are done, they remain valid for the entirety of the game. For this reason the calculation of the arrangements has been removed from the win_check method and now takes place as part of the initialization of the board.

Some aspects of the old implementation were also cleaned up - win_checks now loops over the arrangements dictionary keys and calls tally, instead of this being written out three times. 

## Refactor 14 October 2021

- Changed some method names to make them more descriptive
- Split access board into check_board_value and change_board_value to ensure each method has a single job. This will increase work to be done if data structure is changed, but minimally so. Greater clarity within the code of what is done each time the board is accessed.
- Computer player is now given the board object from the TicTacToe class on initilisation, which simplifies the player.get_player_move() calls, removing the redundant (but cool) one line conditional statement differentiating between player types in TicTacToe.play_game().

- Board.generate_board and Board.generate_win_arrangements have been made 'private' - or at least as private as Python allows.
