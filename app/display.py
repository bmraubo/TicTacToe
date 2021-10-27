from app.board import Board


class Display:

    # draws the current board state
    def draw_board(board):
        def print_row(board, start, display_size_modifer):
            # Every row starts with a | for decorative reasons
            string = "|"
            # Every value is placed on the board, preceded by a dynamic prefix that evens out the spacing
            for num in range(start, board.size + start):
                prefix = " " * (
                    display_size_modifer
                    - len(str(Board.check_board_value(board.board, num)))
                    - 1
                )
                value = Board.check_board_value(board.board, num)
                string = string + f"{prefix}{value} |"
            # the completed row is returned for printing
            return string

        # calculate display modifer method - this is used to determine display spacing

        display_size_modifer = len(str(board.highest_value)) + 2

        border_element = ("-" * display_size_modifer) + "+"
        start = 1  # determines the start point for each row

        # first, print the top border
        print(f"+{border_element*board.size}")
        # You want to stop printing the board when you exceed the highest value
        while start < board.highest_value:
            print(print_row(board, start, display_size_modifer))
            start += board.size
            print(f"+{border_element*board.size}")
