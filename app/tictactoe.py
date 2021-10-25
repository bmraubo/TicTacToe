from app.board import Board
from app.player import HumanPlayer, ComputerPlayer
from app.display import Display
from app.gameprocess import GameProcess


class TicTacToe:
    def __init__(self, size, player_list):
        self.board = Board.generate_board(size)
        self.board_size = size
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

        Display.draw_board(self.board, self.board_size)
        moves_made = 0
        while (moves_made < len(self.board)) and self.winner == None:
            for player in self.players:
                # Requests input and input is validated until validate_player_move returns True
                valid_move_made = False
                while valid_move_made == False:
                    player_move = player.get_player_move()
                    move_information = GameProcess.package_move(
                        self.board, self.board_size, player, player_move, moves_made
                    )
                    move_outcome = GameProcess.process_move(move_information)
                    valid_move_made = move_outcome["move_success"]
                self.board = move_outcome["move_info"]["board"]
                moves_made = move_outcome["move_info"]["move_number"]
                # Board is re-drawn based on the new move
                Display.draw_board(self.board, self.board_size)
                # Once each move is played, the board is checked to see if the most recent player won, or the game is drawn
                if move_outcome["move_info"]["game_over"]:
                    # declare winner
                    self.declare_end_game(move_outcome)
                    break

    def declare_end_game(self, move_outcome):
        if move_outcome["move_info"]["game_status"]["winner"] != None:
            self.winner = move_outcome["move_info"]["game_status"]["winner"]
            print(f"{self.winner} has won the game\N{Party Popper}")
        elif move_outcome["move_info"]["game_status"]["game_state"] == "Draw":
            print("It's a draw")
