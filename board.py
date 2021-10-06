class Board:
    def __init__(self, height, width):
        self.board = {}
        self.height = height
        self.width = width
        self.highest_value = height * width
        self.generate_board(height, width)

    def generate_board(self, height, width):
        total_squares = list(range(1, height * width + 1))
        for num in total_squares:
            self.access_board(num, new_value=num)

    def draw_board(self):
        # draws the current board state
        def print_row(self, start, width, display_size_modifer):
            # Every row starts with a | for decorative reasons
            string = "|"
            # Every value is placed on the board, preceded by a dynamic prefix that evens out the spacing
            for num in range(start, width + start):
                prefix = " " * (
                    display_size_modifer - len(str(self.access_board(num))) - 1
                )
                value = self.access_board(num)
                string = string + f"{prefix}{value} |"
            # the completed row is returned for printing
            return string

        # calculate display modifer method
        # for future ref: create display class

        display_size_modifer = (
            len(str(self.highest_value)) + 2
        )  # used to calculate spacing
        border_element = ("-" * display_size_modifer) + "+"
        start = 1  # determines the start point for each row

        print(f"+{border_element*self.width}")
        # You want to stop printing the board when you exceed the highest value
        while start < self.highest_value:
            print(print_row(self, start, self.width, display_size_modifer))
            start += self.width
            print(f"+{border_element*self.width}")

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
            if move < 1 or move > self.highest_value:
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
