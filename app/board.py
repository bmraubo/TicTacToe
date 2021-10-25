class Board:
    def __init__(self, size):
        self.board = {}
        self.size = size
        self.__generate_board()

    def check_board_value(self, current_board_value):
        # checks value in board data
        return self.board[str(current_board_value)]

    def change_board_value(self, current_board_value, new_board_value):
        # replaces value in board data with new value
        self.board[str(current_board_value)] = str(new_board_value)
        return self.board[str(current_board_value)]

    # creates data structure for board of requested size
    def __generate_board(self):
        highest_value = self.size * self.size
        total_squares = list(range(1, highest_value + 1))
        for num in total_squares:
            self.change_board_value(num, num)
