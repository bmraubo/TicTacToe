class UserInterface:
    def welcome_message():
        print("Welcome to Tic Tac Toe")

    def game_instructions():
        instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        print(instructions)

    def get_player_info():
        # Obtains player names from user
        player_list = []
        while len(player_list) != 2:
            player_name = input(f"Enter Player {len(player_list)+1} Name: ")
            player_type = "human"
            player_list.append([player_name, player_type])
        return player_list


class TicTacToe:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.markers = {}
        self.players = []

    # Player creation and assignment to X, O values in self.markers
    def create_players(self, players):
        # loops through player information entered by user in UserInterface.get_player_info
        for player in players:
            self.players.append(Player(player))

    def assign_players(self):
        # assigns players to X and O
        self.markers[self.players[0]] = "X"
        self.markers[self.players[1]] = "O"

    def draw_board(self):
        # draws the current board state
        divider = "+---+---+---+"
        print(divider)
        print(f"| {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |")
        print(divider)
        print(f"| {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |")
        print(divider)
        print(f"| {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |")
        print(divider)

    def make_move(self, player, move):
        # Takes user move input and translates it into board location
        row = (move - 1) // 3
        column = (move - 1) % 3
        marker = self.markers[player]
        self.board[row][column] = marker

    def validate_player_move(self, player_move):
        # Handles ValueError if non-integer is entered
        try:
            player_move = int(player_move)
            # If user enters an invalid number, the user is warned and asked for proper input
            if player_move < 1 or player_move > 9:
                print(f"{player_move} is not between 1 and 9")
                return False
            # If the move has already been played, user is asked to try again
            elif str(player_move) != (
                self.board[(player_move - 1) // 3][(player_move - 1) % 3]
            ):
                print(f"{player_move} has already been played")
                return False
            else:
                return True  # Validation passes if valid input is given
        except ValueError:
            print(f"Value Error: {player_move} is not between 1-9")
            return False

    def play_game(self):
        # There is a maximum of 9 moves, so the game loops until all moves are made
        moves_made = 0
        while moves_made < 9:
            for player in self.players:
                # Requests input and input is validated until validate_player_move returns True
                valid_move = False
                while valid_move == False:
                    player_move = input(f"{player.name}, please enter move: ")
                    valid_move = self.validate_player_move(player_move)
                # Valid moves are made
                self.make_move(player, int(player_move))
                # Board is re-drawn based on the new move
                self.draw_board()
                moves_made += 1
                # Once each move is played, the board is checked to see if the most recent player won, or the game is drawn
                self.end_game(moves_made, player)

    def end_game(self, moves_made, player):
        # Checks if the most recent player's move has won them the game
        if self.win_check(player):
            print(f"{player.name} has won the game\N{Party Popper}")
            print("Game is closing gracefully")
            exit()
        # If the most recent move has not won the game, the outcome might be a draw
        elif moves_made == 9:
            print("It's a draw")
            print("Game is closing gracefully")
            exit()

    def win_check(self, player):
        # nested function to check if a win condition is met
        def tally(player, arrangement):
            for poss in range(len(arrangement)):
                if arrangement[poss].count(self.markers[player]) == 3:
                    return True

        # Columns described to be fed as input into tally()
        columns = [
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
        ]
        # Diagonals described to be fed as input into tally()
        diagonals = [
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]],
        ]
        if tally(player, self.board):
            return True
        elif tally(player, columns):
            return True
        elif tally(player, diagonals):
            return True
        else:
            return False


class Player:
    def __init__(self, player_info):
        self.name = player_info[0]
        self.type = player_info[1]


if __name__ == "__main__":
    UserInterface.welcome_message()
    UserInterface.game_instructions()
    game = TicTacToe()
    player_list = UserInterface.get_player_info()
    game.create_players(player_list)
    game.assign_players()
    game.draw_board()
    game.play_game()
