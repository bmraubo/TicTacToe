class ServerLogic:
    def check_board_value(board, current_board_value):
        # checks value in board data
        return board[str(current_board_value)]

    def change_board_value(board, current_board_value, new_board_value):
        # replaces value in board data with new value
        board[str(current_board_value)] = str(new_board_value)
        return board

    # rejects moves that are outside the range, have been played, or generally unusable - e.g. letters
    def validate_move(board, move):
        highest_value = len(board)
        # Handles ValueError if non-integer is entered
        try:
            move = int(move)
            # If user enters an invalid number, the user is warned and asked for proper input
            # Lowest possible input will always be 1
            if move < 1 or move > highest_value:
                return (False, f"{move} is not between 1 and {highest_value}")
            # If the move has already been played, user is asked to try again
            # this board check could be removed, but that would add too much complexity
            elif str(move) != ServerLogic.check_board_value(board, move):
                return (False, f"{move} has already been played")
            else:
                return (
                    True,
                    f"{move} is valid",
                )  # Validation passes if valid input is given
        except ValueError:
            return (False, f"Value Error: {move} is not between 1-{highest_value}")

    ### Generate Win Arrangements
    def generate_win_arrangements(board, size):
        highest_value = len(board)
        # Creates a master list of all values as strings
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

    ### Win Checks
    def win_check(board, marker, arrangements, size):
        # nested function to check if a win condition is met
        def tally(board, marker, arrangement, size):
            count = 0
            for element in arrangement:
                for num in element:
                    if ServerLogic.check_board_value(board, num) == marker:
                        count += 1
                if count == size:
                    return True
                count = 0

        for key in arrangements:
            if tally(board, marker, arrangements[key], size):
                return True

        return False

    # End Game Check
    def end_game_check(board, moves_made, player_marker, size):
        highest_value = len(board)
        arrangements = ServerLogic.generate_win_arrangements(board, size)
        # Checks if the most recent player's move has won them the game
        if ServerLogic.win_check(board, player_marker, arrangements, size):
            return (True, player_marker)
        # If the most recent move has not won the game, the outcome might be a draw
        elif moves_made == highest_value:
            return (True, "Draw")
        else:
            return (False, "Ongoing")
