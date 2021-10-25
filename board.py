class Board:
    def __init__(self, size):
        self.board = {}
        self.size = size
        self.highest_value = size * size
        self.__generate_board()
        self.arrangements = self.__generate_win_arrangements()

    def check_board_value(self, current_board_value):
        # checks value in board data
        return self.board[str(current_board_value)]

    def change_board_value(self, current_board_value, new_board_value):
        # replaces value in board data with new value
        self.board[str(current_board_value)] = str(new_board_value)
        return self.board[str(current_board_value)]

    # creates data structure for board of requested size
    def __generate_board(self):
        total_squares = list(range(1, self.highest_value + 1))
        for num in total_squares:
            self.change_board_value(num, num)

    # rejects moves that are outside the range, have been played, or generally unusable - e.g. letters
    def validate_move(self, move):
        # Handles ValueError if non-integer is entered
        try:
            move = int(move)
            # If user enters an invalid number, the user is warned and asked for proper input
            # Lowest possible input will always be 1
            if move < 1 or move > self.highest_value:
                print(f"{move} is not between 1 and {self.highest_value}")
                return False
            # If the move has already been played, user is asked to try again
            # this board check could be removed, but that would add too much complexity
            elif str(move) != self.check_board_value(move):
                print(f"{move} has already been played")
                return False
            else:
                return True  # Validation passes if valid input is given
        except ValueError:
            print(f"Value Error: {move} is not between 1-{self.highest_value}")
            return False

    # generates possible win arrangements to be checked by win_check()
    def __generate_win_arrangements(self):
        # Creates a master list of all values as strings
        master_list = []
        for x in list(range(1, self.highest_value + 1)):
            master_list.append(str(x))

        arrangements = {"rows": [], "columns": [], "diagonals": []}

        # creates a matrices of board locations, arranged in order for checking
        arrangements["rows"] = [
            master_list[x : x + self.size]
            for x in range(0, len(master_list), self.size)
        ]
        arrangements["columns"] = [
            master_list[x :: self.size] for x in range(0, self.size)
        ]
        arrangements["diagonals"] = [
            master_list[0 :: self.size + 1],
            master_list[self.size - 1 : self.highest_value - 2 : self.size - 1],
        ]

        return arrangements

    # checks all arrangements to see if player with 'marker' has won the game
    def win_check(self, marker):
        # nested function to check if a win condition is met
        def tally(self, marker, arrangement):
            count = 0
            for element in arrangement:
                for num in element:
                    if self.check_board_value(num) == marker:
                        count += 1
                if count == self.size:
                    return True
                count = 0

        for key in self.arrangements:
            if tally(self, marker, self.arrangements[key]):
                return True

        return False
