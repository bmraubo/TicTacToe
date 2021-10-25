class GameLogic:

    # Board reading and manipulation
    def check_board_value(board, current_board_value):
        # checks value in board data
        return board[str(current_board_value)]

    def change_board_value(board, current_board_value, new_board_value):
        # replaces value in board data with new value
        board[str(current_board_value)] = str(new_board_value)
        return board

    # Move Validation
    # rejects moves that are outside the range, have been played, or generally unusable - e.g. letters
    def validate_move(board, move):
        highest_value = len(board)
        # Handles ValueError if non-integer is entered
        try:
            move = int(move)
            # If user enters an invalid number, the user is warned and asked for proper input
            # Lowest possible input will always be 1
            if move < 1 or move > highest_value:
                print(f"{move} is not between 1 and {highest_value}")
                return False
            # If the move has already been played, user is asked to try again
            # this board check could be removed, but that would add too much complexity
            elif str(move) != GameLogic.check_board_value(board, move):
                print(f"{move} has already been played")
                return False
            else:
                return True  # Validation passes if valid input is given
        except ValueError:
            print(f"Value Error: {move} is not between 1-{highest_value}")
            return False

    # End Game Checks
    # Generate Winning Arrangements to check the board against
    def generate_win_arrangements(board, size):
        # Creates a master list of all values as strings
        highest_value = len(board)
        master_list = []
        for x in list(range(1, highest_value + 1)):
            master_list.append(str(x))

        arrangements = {"rows": [], "columns": [], "diagonals": []}

        # creates a matrices of board locations, arranged in order for checking
        arrangements["rows"] = [
            master_list[x : x + size] for x in range(0, len(master_list), size)
        ]
        arrangements["columns"] = [master_list[x::size] for x in range(0, size)]
        arrangements["diagonals"] = [
            master_list[0 :: size + 1],
            master_list[size - 1 : highest_value - 2 : size - 1],
        ]

        return arrangements

    # checks all arrangements to see if player with 'marker' has won the game
    def win_check(board, marker, size):
        # nested function to check if a win condition is met
        def tally(board, marker, arrangement, size):
            count = 0
            for element in arrangement:
                for num in element:
                    if GameLogic.check_board_value(board, num) == marker:
                        count += 1
                if count == size:
                    return True
                count = 0

        arrangements = GameLogic.generate_win_arrangements(board, size)

        for key in arrangements:
            if tally(board, marker, arrangements[key], size):
                return True

        return False
