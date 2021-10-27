from app.board import Board
from app.player import HumanPlayer, ComputerPlayer
from app.display import Display


class TicTacToe:
    def __init__(self, size, player_list):
        self.board = Board()
        self.board.create_board(size)
        self.markers = {}
        self.players = []
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
        while self.board.winner == None:
            for player in self.players:
                # Requests input and input is validated until validate_player_move returns True
                valid_move = False
                while valid_move == False:
                    player_move = player.get_player_move()
                    valid_move = self.board.make_move(player, player_move)
                    if valid_move[0]:
                        self.board = valid_move[1]
                    else:
                        TicTacToe.declare_reason_for_move_rejection(valid_move)
                # Board is re-drawn based on the new move
                Display.draw_board(self.board)
                moves_made += 1
                # Once each move is played, the board is checked to see if the most recent player won, or the game is drawn
                if self.board.winner != None:
                    break

    def declare_invalid_move_reason(valid_move):
        return valid_move[1]
