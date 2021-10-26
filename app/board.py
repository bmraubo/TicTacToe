from app.gameprocess import GameProcess


class Board:
    def __init__(self, size):
        self.board = {}
        self.size = size
        self.highest_value = size * size
        self.moves_made = 0
        self.__generate_board()

    # creates data structure for board of requested size
    def __generate_board(self):
        total_squares = list(range(1, self.highest_value + 1))
        for num in total_squares:
            self.board = GameProcess.change_board_value(self.board, num, num)
