from board import Board
from player import Player


class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.markers = {}
        self.players = []

    # Displaying Welcome Message and Game Instructions
    def welcome_message(self):
        print("Welcome to Tic Tac Toe")

    def game_instructions(self):
        instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        print(instructions)

    # Player creation and assignment to X, O values in self.markers
    def set_up_players(self):
        player_list = self.get_player_info()
        self.create_players(player_list)
        self.assign_players()

    def get_player_info(self):
        # Obtains player names from user
        player_list = []
        while len(player_list) != 2:
            player_name = input(f"Enter Player {len(player_list)+1} Name: ")
            player_type = "human"
            player_list.append([player_name, player_type])
        return player_list

    def create_players(self, players):
        # loops through player information entered by user in UserInterface.get_player_info
        for player in players:
            self.players.append(Player(player))

    def assign_players(self):
        # assigns players to X and O
        self.markers[self.players[0]] = "X"
        self.markers[self.players[1]] = "O"

    # Gameplay loops
    def play_game(self):
        # There is a maximum of 9 moves, so the game loops until all moves are made
        self.welcome_message()
        self.game_instructions()
        self.set_up_players()
        self.board.draw_board()
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
        if self.board.win_check(self.markers[player]):
            print(f"{player.name} has won the game\N{Party Popper}")
            print("Game is closing gracefully")
            exit()
        # If the most recent move has not won the game, the outcome might be a draw
        elif moves_made == 9:
            print("It's a draw")
            print("Game is closing gracefully")
            exit()


if __name__ == "__main__":
    game = TicTacToe()

    game.play_game()
