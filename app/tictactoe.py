from app.board import Board
from app.player import HumanPlayer, ComputerPlayer
from app.display import Display
from app.ui import UserInterface


class TicTacToe:
    def __init__(self, size, player_list, server=False):
        self.board = Board()
        self.board.create_board(size)
        self.players = []
        self.server = server
        self.__create_players(player_list)

    # Player creation and assignment to X, O values in self.markers
    def __create_players(self, players):
        # loops through player information entered by user in UserInterface.get_player_info
        for player in players:
            if player[1] == "human":
                self.players.append(HumanPlayer(player))
            elif player[1] == "computer":
                self.players.append(ComputerPlayer(player, self.board))

    # Gameplay loops
    def play_game(self):
        # There is a maximum of size*size moves, so the game loops until all moves are made
        Display.draw_board(self.board)
        while self.board.winner == None:
            for player in self.players:
                # Requests input and input is validated until validate_player_move returns True
                valid_move = False
                while valid_move == False:
                    player_move = player.get_player_move()
                    move_outcome = self.board.make_move(
                        player, player_move, server=self.server
                    )
                    valid_move = move_outcome[0]
                    if valid_move:
                        self.board = move_outcome[1]
                        UserInterface.display_move_notification(
                            player_move, player.name
                        )
                        self.update_computer_player_boards()
                    else:
                        UserInterface.display_message(move_outcome[1])
                # Board is re-drawn based on the new move
                Display.draw_board(self.board)
                # Once each move is played, the board is checked to see if the most recent player won, or the game is drawn
                if self.board.winner != None:
                    UserInterface.declare_winner(self.board.winner)
                    break

    def update_computer_player_boards(self):
        for player in self.players:
            if player.type == "computer":
                player.board = self.board
