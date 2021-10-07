from ui import UserInterface
from board import Board
from player import HumanPlayer, ComputerPlayer
from display import Display


class TicTacToe:
    def __init__(self, size):
        self.board = Board(size)
        self.markers = {}
        self.players = []

    # Player creation and assignment to X, O values in self.markers
    def set_up_players(self):
        player_list = UserInterface.get_player_info()
        self.create_players(player_list)
        self.assign_players()

    def create_players(self, players):
        # loops through player information entered by user in UserInterface.get_player_info
        for player in players:
            if player[1] == "human":
                self.players.append(HumanPlayer(player))
            elif player[1] == "computer":
                self.players.append(ComputerPlayer(player))

    def assign_players(self):
        # assigns players to X and O
        self.markers[self.players[0]] = "X"
        self.markers[self.players[1]] = "O"

    # Gameplay loops
    def play_game(self):
        # There is a maximum of 9 moves, so the game loops until all moves are made
        UserInterface.game_instructions(self.board.size)
        self.set_up_players()
        Display.draw_board(self.board)
        moves_made = 0
        while moves_made < self.board.highest_value:
            for player in self.players:
                # Requests input and input is validated until validate_player_move returns True
                valid_move = False
                while valid_move == False:
                    player_move = (
                        player.get_player_move()
                        if player.type == "human"
                        else player.get_player_move(self.board)
                    )
                    valid_move = self.board.validate_move(player_move)
                # Valid moves are made
                self.board.access_board(
                    int(player_move), new_value=self.markers[player]
                )
                # Board is re-drawn based on the new move
                Display.draw_board(self.board)
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
        elif moves_made == self.board.highest_value:
            print("It's a draw")
            print("Game is closing gracefully")
            exit()


if __name__ == "__main__":
    UserInterface.welcome_message()
    size = UserInterface.get_board_size()
    game = TicTacToe(size)
    game.play_game()
