from app.gamelogic import GameLogic


class Board:

    # creates data structure for board of requested size
    def generate_board(size):
        board = {}
        highest_value = size * size
        total_squares = list(range(1, highest_value + 1))
        for num in total_squares:
            GameLogic.change_board_value(board, num, num)
        return board
