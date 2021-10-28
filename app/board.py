class Board:
    def __init__(
        self,
        board={},
        size=None,
        highest_value=None,
        arrangements=None,
        winner=None,
        moves_made=0,
    ):
        self.board = board
        self.size = size
        self.highest_value = highest_value
        self.arrangements = arrangements
        self.winner = winner
        self.moves_made = moves_made

    def create_board(self, size):
        self.size = size
        self.highest_value = size * size
        self.board = self.__generate_board()
        self.arrangements = self.__generate_win_arrangements()

    def check_board_value(board, current_board_value):
        # checks value in board data
        return board[str(current_board_value)]

    def change_board_value(board, current_board_value, new_board_value):
        # replaces value in board data with new value
        board[str(current_board_value)] = str(new_board_value)
        return board

    # creates data structure for board of requested size
    def __generate_board(self):
        board_data = {}
        total_squares = list(range(1, self.highest_value + 1))
        for num in total_squares:
            Board.change_board_value(board_data, num, num)
        return board_data

    # rejects moves that are outside the range, have been played, or generally unusable - e.g. letters
    def validate_move(board, move, size):
        # Handles ValueError if non-integer is entered
        highest_value = size * size
        try:
            move = int(move)
            # If user enters an invalid number, the user is warned and asked for proper input
            # Lowest possible input will always be 1
            if move < 1 or move > highest_value:
                return (False, f"{move} is not between 1 and {highest_value}")
            # If the move has already been played, user is asked to try again
            # this board check could be removed, but that would add too much complexity
            elif str(move) != Board.check_board_value(board, move):
                return (False, f"{move} has already been played")
            else:
                return (True, "OK")  # Validation passes if valid input is given
        except ValueError:
            return (False, f"Value Error: {move} is not between 1-{highest_value}")

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
                    if Board.check_board_value(self.board, num) == marker:
                        count += 1
                if count == self.size:
                    return True
                count = 0

        for key in self.arrangements:
            if tally(self, marker, self.arrangements[key]):
                return True

        return False

    def make_move(self, Player, move, server=False):
        if server == False:
            move_validation_result = Board.validate_move(self.board, move, self.size)
            if move_validation_result[0]:
                new_board = Board.__local_move_logic(self, Player, move)
                return (True, new_board)
            else:
                return move_validation_result
        if server == True:
            server_response = Board.__make_server_request(self, Player, move)
            new_board = Board.__server_move_logic(server_response)
            return new_board

    def __local_move_logic(GameBoard, Player, move):
        new_board_data = Board.change_board_value(GameBoard.board, move, Player.marker)
        new_board = Board(
            board=new_board_data,
            size=GameBoard.size,
            highest_value=GameBoard.highest_value,
            arrangements=GameBoard.arrangements,
            moves_made=GameBoard.moves_made + 1,
        )
        new_board.winner = Board.end_game(new_board, Player)
        print(Board.declare_winner(new_board.winner))
        return new_board

    def __make_server_request(GameBoard, Player, move):
        pass

    def __read_server_response(server_response):
        pass

    def end_game(GameBoard, player):
        # Checks if the most recent player's move has won them the game
        if GameBoard.win_check(player.marker):
            winner = player
            return winner
        # If the most recent move has not won the game, the outcome might be a draw
        elif GameBoard.moves_made == GameBoard.highest_value:
            winner = "Draw!"
            return winner
        else:
            return None

    def declare_winner(winner):
        if winner == "Draw!":
            return f"It's a {winner}"
        elif winner == None:
            return None
        else:
            return f"{winner.name} has won the game\N{Party Popper}"
