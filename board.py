class Board:
    def __init__(self, height, width):
        self.board = {}
        self.generate_board(height, width)

    def generate_board(self, height, width):
        total_squares = list(range(1, height * width + 1))
        for num in total_squares:
            self.access_board(num, new_value=num)

    def draw_board(self):
        # draws the current board state
        divider = "+---+---+---+"
        print(divider)
        print(
            f"| {self.access_board('1')} | {self.access_board('2')} | {self.access_board('3')} |"
        )
        print(divider)
        print(
            f"| {self.access_board('4')} | {self.access_board('5')} | {self.access_board('6')} |"
        )
        print(divider)
        print(
            f"| {self.access_board('7')} | {self.access_board('8')} | {self.access_board('9')} |"
        )
        print(divider)

    def access_board(self, value, new_value=None):
        # checks value in board data, if new_value is present, changes board data to that value
        if new_value == None:
            return self.board[str(value)]
        else:
            self.board[str(value)] = str(new_value)
            return self.board[str(value)]

    def validate_move(self, move):
        # Handles ValueError if non-integer is entered
        try:
            move = int(move)
            # If user enters an invalid number, the user is warned and asked for proper input
            if move < 1 or move > 9:
                print(f"{move} is not between 1 and 9")
                return False
            # If the move has already been played, user is asked to try again
            # this board check could be removed, but that would add too much complexity
            elif str(move) != self.access_board(move):
                print(f"{move} has already been played")
                return False
            else:
                return True  # Validation passes if valid input is given
        except ValueError:
            print(f"Value Error: {move} is not between 1-9")
            return False

    def win_check(self, marker):
        # nested function to check if a win condition is met
        def tally(marker, arrangement):
            for poss in range(len(arrangement)):
                if arrangement[poss].count(marker) == 3:
                    return True

        # Rows described to prevent having to query Board directly
        rows = [
            [self.access_board("1"), self.access_board("2"), self.access_board("3")],
            [self.access_board("4"), self.access_board("5"), self.access_board("6")],
            [self.access_board("7"), self.access_board("8"), self.access_board("9")],
        ]
        # Columns described to be fed as input into tally()
        columns = [
            [self.access_board("1"), self.access_board("4"), self.access_board("7")],
            [self.access_board("2"), self.access_board("5"), self.access_board("8")],
            [self.access_board("3"), self.access_board("6"), self.access_board("9")],
        ]
        # Diagonals described to be fed as input into tally()
        diagonals = [
            [self.access_board("1"), self.access_board("5"), self.access_board("9")],
            [self.access_board("3"), self.access_board("5"), self.access_board("7")],
        ]
        if tally(marker, rows):
            return True
        elif tally(marker, columns):
            return True
        elif tally(marker, diagonals):
            return True
        else:
            return False
