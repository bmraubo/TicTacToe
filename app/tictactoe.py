from app.board import Board
from app.gameprocess import GameProcess
from app.player import HumanPlayer, ComputerPlayer
from app.display import Display


class TicTacToe:
    def __init__(self, size, player_list):
        self.board = Board(size)
        self.markers = {}
        self.players = []
        self.winner = None
        self.set_up_players(player_list)

    # Player creation and assignment to X, O values in self.markers
    def set_up_players(self, player_list):
        self.__create_players(player_list)
        self.__assign_players()

    def __create_players(self, players):
        # loops through player information entered by user in UserInterface.get_player_info
        for player in players:
            if player[1] == "human":
                self.players.append(HumanPlayer(player))
            elif player[1] == "computer":
                self.players.append(ComputerPlayer(player, self.board))

    def __assign_players(self):
        # assigns players to X and O
        self.markers[self.players[0]] = self.players[0].marker
        self.markers[self.players[1]] = self.players[1].marker

    # Gameplay loops
    def play_game(self):
        # There is a maximum of 9 moves, so the game loops until all moves are made

        Display.draw_board(self.board)
        moves_made = 0
        while (moves_made < self.board.highest_value) and self.winner == None:
            for player in self.players:
                # Requests input and input is validated until validate_player_move returns True
                valid_move = False
                while valid_move == False:
                    player_move = player.get_player_move()
                    move_information = GameProcess.package_move_information(
                        self.board, player, player_move
                    )
                    move_outcome = GameProcess.process_move(move_information)
                    valid_move = move_outcome["move_success"]
                # Valid moves are made
                GameProcess.process_response(move_outcome)
                # Board is re-drawn based on the new move
                Display.draw_board(self.board)
                moves_made += 1
                # Once each move is played, the board is checked to see if the most recent player won, or the game is drawn
                if self.end_game(moves_made, player):
                    break

    def end_game(self, moves_made, player):
        # Checks if the most recent player's move has won them the game
        if self.board.win_check(self.markers[player]):
            print(f"{player.name} has won the game\N{Party Popper}")
            self.winner = player
            return True
        # If the most recent move has not won the game, the outcome might be a draw
        elif moves_made == self.board.highest_value:
            print("It's a draw")
            self.winner = "Draw"
            return True
        else:
            return False
