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
                print(f"{move} is not between 1 and {highest_value}")
                return False
            # If the move has already been played, user is asked to try again
            # this board check could be removed, but that would add too much complexity
            elif str(move) != ServerLogic.check_board_value(board, move):
                print(f"{move} has already been played")
                return False
            else:
                return True  # Validation passes if valid input is given
        except ValueError:
            print(f"Value Error: {move} is not between 1-{highest_value}")
            return False

    ### Generate Win Arrangements

    ### Win Checks
