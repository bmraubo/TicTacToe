class Board:
    def __init__(self):
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    def draw_board(self):
        # draws the current board state
        divider = "+---+---+---+"
        print(divider)
        print(f"| {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |")
        print(divider)
        print(f"| {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |")
        print(divider)
        print(f"| {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |")
        print(divider)

    def make_move(self, marker, move):
        # Takes user move input and translates it into board location
        row = (move - 1) // 3
        column = (move - 1) % 3
        self.board[row][column] = marker

    def validate_move(self, move):
        # Handles ValueError if non-integer is entered
        try:
            move = int(move)
            # If user enters an invalid number, the user is warned and asked for proper input
            if move < 1 or move > 9:
                print(f"{move} is not between 1 and 9")
                return False
            # If the move has already been played, user is asked to try again
            elif str(move) != (self.board[(move - 1) // 3][(move - 1) % 3]):
                print(f"{move} has already been played")
                return False
            else:
                return True  # Validation passes if valid input is given
        except ValueError:
            print(f"Value Error: {move} is not between 1-9")
            return False
