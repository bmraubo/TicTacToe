from app.gameprocess import GameProcess


class Logic:

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
                return (False, f"{move} is not between 1 and {highest_value}")
            # If the move has already been played, user is asked to try again
            # this board check could be removed, but that would add too much complexity
            elif str(move) != GameProcess.check_board_value(board, move):
                return (False, f"{move} has already been played")
            else:
                return (True, "OK")  # Validation passes if valid input is given
        except ValueError:
            return (False, f"Value Error: {move} is not between 1-{highest_value}")

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
                    if GameProcess.check_board_value(board, num) == marker:
                        count += 1
                if count == size:
                    return True
                count = 0

        arrangements = Logic.generate_win_arrangements(board, size)

        for key in arrangements:
            if tally(board, marker, arrangements[key], size):
                return True
        return False

    def end_game(updated_board, move_information):
        # Checks if the most recent player's move has won them the game
        if Logic.win_check(
            updated_board,
            move_information["player"]["marker"],
            move_information["board"]["size"],
        ):
            winner = move_information["player"]["name"]
            return (True, {"game_state": "won", "winner": winner})
        # If the most recent move has not won the game, the outcome might be a draw
        elif move_information["move"]["move_number"] == len(updated_board):
            return (
                True,
                {"game_state": "Draw", "winner": None},
            )
        else:
            return (False, {"game_state": "In Progress", "winner": None})
