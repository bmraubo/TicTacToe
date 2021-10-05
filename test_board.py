import unittest
import sys
from io import StringIO
from board import Board


class TestBoard(unittest.TestCase):
    def test_initialize_board(self):
        expected_board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        test_board = Board()
        self.assertEqual(test_board.board, expected_board)

    def test_check_value(self):
        test_board = Board()
        value = "4"
        self.assertEqual(test_board.check_value(value), "4")

    def test_print_board(self):
        test_board = Board()
        initial_board = "+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+"
        captured_output = StringIO()
        sys.stdout = captured_output
        test_board.draw_board()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, initial_board)

    def test_make_move(self):
        # Set up game
        test_board = Board()
        # Test move
        test_input = "1"
        marker = "X"
        test_board.make_move(marker, int(test_input))
        self.assertEqual(test_board.board[0][0], "X")

    def test_validate_move_valueerror(self):
        # Test for value error exception handling
        test_board = Board()
        player_move = "j"
        self.assertFalse(test_board.validate_move(player_move))

    def test_validate_move_out_of_range(self):
        # Rejects moves that are outside of permitted range
        test_board = Board()
        player_move = "10"
        self.assertFalse(test_board.validate_move(player_move))
        player_move = "0"
        self.assertFalse(test_board.validate_move(player_move))
        # Tests inputs within range, for completeness => should be allowed
        player_move = "9"
        self.assertTrue(test_board.validate_move(player_move))
        player_move = "1"
        self.assertTrue(test_board.validate_move(player_move))

    def test_validate_move_already_played(self):
        # Rejects move if it has already been played
        test_board = Board()
        test_input = "1"
        test_board.make_move("X", int(test_input))
        player_move = "1"
        self.assertFalse(test_board.validate_move(player_move))
        player_move = "2"
        self.assertTrue(test_board.validate_move(player_move))

    # Testing win check
    def test_no_win(self):
        # test win check where no win or draw state exists
        test_board = Board()
        test_marker = "X"
        self.assertFalse(test_board.win_check(test_marker))

    def test_win_column(self):
        # testing Win state in column
        # Set up a game
        test_board = Board()
        test_marker = "X"
        test_board.board[0][1] = "X"
        test_board.board[1][1] = "X"
        test_board.board[2][1] = "X"
        self.assertTrue(test_board.win_check(test_marker))

    def test_win_row(self):
        # Testing win state in Row
        test_board = Board()
        test_marker = "X"
        test_board.board[0][0] = "X"
        test_board.board[0][1] = "X"
        test_board.board[0][2] = "X"
        self.assertTrue(test_board.win_check(test_marker))

    def test_row_diagonal(self):
        # Testing diagonal win states
        test_board = Board()
        test_marker = "X"
        test_board.board[0][0] = "X"
        test_board.board[1][1] = "X"
        test_board.board[2][2] = "X"
        self.assertTrue(test_board.win_check(test_marker))


if __name__ == "__main__":
    unittest.main()
