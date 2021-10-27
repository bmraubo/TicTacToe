from app.gamelogic import GameLogic
from app.gameprocess import GameProcess


class Board:
    def __init__(self, board={}, size=0, moves_made=0):
        self.board = board
        self.size = size
        self.moves_made = moves_made

    # creates data structure for board of requested size
    def generate_board(self, size):
        self.size = size
        highest_value = size * size
        total_squares = list(range(1, highest_value + 1))
        for num in total_squares:
            GameLogic.change_board_value(self.board, num, num)
        return self.board

    def __update_board_after_move(self, move_outcome):
        self.board = move_outcome["move_info"]["board"]
        self.moves_made = move_outcome["move_info"]["move_number"]

    def make_move(self, Player, move):
        move_information = GameProcess.package_move(self, Player, move)
        move_outcome = GameProcess.process_move(move_information)
        if move_outcome["move_success"] == True:
            self.__update_board_after_move(move_outcome)
            return move_outcome
        else:
            return move_outcome
