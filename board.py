class Board:
    def __init__(self, size):
        self.board = {}
        self.size = size
        self.highest_value = size * size
        self.generate_board(size)

    def generate_board(self, size):
        total_squares = list(range(1, size * size + 1))
        for num in total_squares:
            self.access_board(num, new_value=num)

    def draw_board(self):
        # draws the current board state
        def print_row(self, start, size, display_size_modifer):
            # Every row starts with a | for decorative reasons
            string = "|"
            # Every value is placed on the board, preceded by a dynamic prefix that evens out the spacing
            for num in range(start, size + start):
                prefix = " " * (
                    display_size_modifer - len(str(self.access_board(num))) - 1
                )
                value = self.access_board(num)
                string = string + f"{prefix}{value} |"
            # the completed row is returned for printing
            return string

        # calculate display modifer method - this is used to determine display spacing
        display_size_modifer = len(str(self.highest_value)) + 2

        border_element = ("-" * display_size_modifer) + "+"
        start = 1  # determines the start point for each row

        print(f"+{border_element*self.size}")
        # You want to stop printing the board when you exceed the highest value
        while start < self.highest_value:
            print(print_row(self, start, self.size, display_size_modifer))
            start += self.size
            print(f"+{border_element*self.size}")

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
            # Lowest possible input will always be 1
            if move < 1 or move > self.highest_value:
                print(f"{move} is not between 1 and {self.highest_value}")
                return False
            # If the move has already been played, user is asked to try again
            # this board check could be removed, but that would add too much complexity
            elif str(move) != self.access_board(move):
                print(f"{move} has already been played")
                return False
            else:
                return True  # Validation passes if valid input is given
        except ValueError:
            print(f"Value Error: {move} is not between 1-{self.highest_value}")
            return False

    def generate_arrangements(self):

        # Creates a master list of all values as strings
        master_list = []
        for x in list(range(1, self.highest_value + 1)):
            master_list.append(str(x))

        arrangements = {"rows": [], "columns": [], "diagonals": []}

        # creates a matrices of values, arranged in order for checking
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

    def win_check(self, marker):
        # nested function to check if a win condition is met
        def tally(self, marker, arrangement):
            count = 0
            for element in arrangement:
                for num in element:
                    if self.access_board(num) == marker:
                        count += 1
                if count == self.size:
                    return True

        arrangements = self.generate_arrangements()

        for key in arrangements:
            if tally(self, marker, arrangements[key]):
                return True

        return False
