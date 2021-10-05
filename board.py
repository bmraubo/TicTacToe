class Board:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

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
        row = (int(value) - 1) // 3
        column = (int(value) - 1) % 3
        if new_value == None:
            return self.board[row][column]
        else:
            self.board[row][column] = new_value
            return self.board[row][column]

    def validate_move(self, move):
        # Handles ValueError if non-integer is entered
        try:
            move = int(move)
            # If user enters an invalid number, the user is warned and asked for proper input
            if move < 1 or move > 9:
                print(f"{move} is not between 1 and 9")
                return False
            # If the move has already been played, user is asked to try again
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

        # Columns described to be fed as input into tally()
        columns = [
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
        ]
        # Diagonals described to be fed as input into tally()
        diagonals = [
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]],
        ]
        if tally(marker, self.board):
            return True
        elif tally(marker, columns):
            return True
        elif tally(marker, diagonals):
            return True
        else:
            return False
