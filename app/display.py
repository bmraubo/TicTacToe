from app.gamelogic import GameLogic


class Display:

    # draws the current board state
    def draw_board(board, size):
        def print_row(board, start, display_size_modifer, size):
            # Every row starts with a | for decorative reasons
            string = "|"
            # Every value is placed on the board, preceded by a dynamic prefix that evens out the spacing
            for num in range(start, size + start):
                prefix = " " * (
                    display_size_modifer
                    - len(str(GameLogic.check_board_value(board, num)))
                    - 1
                )
                value = GameLogic.check_board_value(board, num)
                string = string + f"{prefix}{value} |"
            # the completed row is returned for printing
            return string

        # calculate display modifer method - this is used to determine display spacing
        highest_value = len(board)

        display_size_modifer = len(str(highest_value)) + 2

        border_element = ("-" * display_size_modifer) + "+"
        start = 1  # determines the start point for each row

        # first, print the top border
        print(f"+{border_element*size}")
        # You want to stop printing the board when you exceed the highest value
        while start < highest_value:
            print(print_row(board, start, display_size_modifer, size))
            start += size
            print(f"+{border_element*size}")
