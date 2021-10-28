from app.util import Utilities


class MoveLogic:

    # rejects moves that are outside the range, have been played, or generally unusable - e.g. letters
    def validate_move(GameBoard, move, size):
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
            elif str(move) != Utilities.check_board_value(GameBoard.board_data, move):
                return (False, f"{move} has already been played")
            else:
                return (True, "OK")  # Validation passes if valid input is given
        except ValueError:
            return (False, f"Value Error: {move} is not between 1-{highest_value}")

    def end_game(GameBoard, player):
        # Checks if the most recent player's move has won them the game
        if MoveLogic.win_check(GameBoard, player.marker):
            winner = player
            return winner
        # If the most recent move has not won the game, the outcome might be a draw
        elif GameBoard.moves_made == GameBoard.highest_value:
            winner = "Draw!"
            return winner
        else:
            return None

        # checks all arrangements to see if player with 'marker' has won the game

    def win_check(GameBoard, marker):
        # nested function to check if a win condition is met
        def tally(GameBoard, marker, arrangement):
            count = 0
            for element in arrangement:
                for num in element:
                    if Utilities.check_board_value(GameBoard.board_data, num) == marker:
                        count += 1
                if count == GameBoard.size:
                    return True
                count = 0

        for key in GameBoard.arrangements:
            if tally(GameBoard, marker, GameBoard.arrangements[key]):
                return True

        return False
