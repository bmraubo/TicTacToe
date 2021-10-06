import unittest
import sys
from io import StringIO
from board import Board


class TestBoard(unittest.TestCase):
    def test_generate_board_3x3(self):
        expected_board = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }
        test_board = Board(3, 3)
        self.assertEqual(test_board.board, expected_board)

    def test_generate_board_4x4(self):
        expected_board = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "10": "10",
            "11": "11",
            "12": "12",
            "13": "13",
            "14": "14",
            "15": "15",
            "16": "16",
        }
        test_board = Board(4, 4)
        self.assertEqual(test_board.board, expected_board)

    def test_access_board(self):
        test_board = Board(3, 3)
        value = "4"
        self.assertEqual(test_board.access_board(value), "4")

    def test_access_board_new_value(self):
        # Set up game
        test_board = Board(3, 3)
        # Test move
        test_input = "1"
        marker = "X"
        self.assertEqual(test_board.access_board(test_input, new_value=marker), "X")

    def test_print_board_3x3(self):
        test_board = Board(3, 3)
        initial_board = "+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+"
        captured_output = StringIO()
        sys.stdout = captured_output
        test_board.draw_board()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, initial_board)

    def test_print_board_4x4(self):
        test_board = Board(4, 4)
        initial_board = "+----+----+----+----+\n|  1 |  2 |  3 |  4 |\n+----+----+----+----+\n|  5 |  6 |  7 |  8 |\n+----+----+----+----+\n|  9 | 10 | 11 | 12 |\n+----+----+----+----+\n| 13 | 14 | 15 | 16 |\n+----+----+----+----+"
        captured_output = StringIO()
        sys.stdout = captured_output
        test_board.draw_board()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, initial_board)

    def test_validate_move_valueerror(self):
        # Test for value error exception handling
        test_board = Board(3, 3)
        player_move = "j"
        self.assertFalse(test_board.validate_move(player_move))

    def test_validate_move_out_of_range(self):
        # Rejects moves that are outside of permitted range
        test_board = Board(3, 3)
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
        test_board = Board(3, 3)
        test_input = "1"
        marker = "X"
        test_board.access_board(test_input, new_value=marker)
        player_move = "1"
        self.assertFalse(test_board.validate_move(player_move))
        player_move = "2"
        self.assertTrue(test_board.validate_move(player_move))

    # Testing win check
    def test_arrangement_generator_3x3(self):
        test_board = Board(3, 3)
        expected_rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        expected_columns = [["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"]]
        expected_diagonals = [["1", "5", "9"], ["3", "5", "7"]]
        arrangements = test_board.generate_arrangements()
        self.assertEqual(arrangements["rows"], expected_rows)
        self.assertEqual(arrangements["columns"], expected_columns)
        self.assertEqual(arrangements["diagonals"], expected_diagonals)

    def test_arrangement_generator_4x4(self):
        test_board = Board(4, 4)
        expected_rows = [
            ["1", "2", "3", "4"],
            ["5", "6", "7", "8"],
            ["9", "10", "11", "12"],
            ["13", "14", "15", "16"],
        ]
        expected_columns = [
            ["1", "5", "9", "13"],
            ["2", "6", "10", "14"],
            ["3", "7", "11", "15"],
            ["4", "8", "12", "16"],
        ]
        expected_diagonals = [["1", "6", "11", "16"], ["4", "7", "10", "13"]]
        arrangements = test_board.generate_arrangements()
        self.assertEqual(arrangements["rows"], expected_rows)
        self.assertEqual(arrangements["columns"], expected_columns)
        self.assertEqual(arrangements["diagonals"], expected_diagonals)

    def test_no_win_3x3(self):
        # test win check where no win or draw state exists
        test_board = Board(3, 3)
        test_marker = "X"
        self.assertFalse(test_board.win_check(test_marker))

    def test_no_win_4x4(self):
        # test win check where no win or draw state exists
        test_board = Board(4, 4)
        test_marker = "X"
        self.assertFalse(test_board.win_check(test_marker))

    def test_win_column_3x3(self):
        # testing Win state in column
        # Set up a game
        test_board = Board(3, 3)
        test_marker = "X"
        test_board.access_board("1", new_value=test_marker)
        test_board.access_board("4", new_value=test_marker)
        test_board.access_board("7", new_value=test_marker)
        self.assertTrue(test_board.win_check(test_marker))

    def test_win_column_4x4(self):
        # testing Win state in column
        # Set up a game
        test_board = Board(4, 4)
        test_marker = "X"
        test_board.access_board("1", new_value=test_marker)
        test_board.access_board("5", new_value=test_marker)
        test_board.access_board("9", new_value=test_marker)
        test_board.access_board("13", new_value=test_marker)
        self.assertTrue(test_board.win_check(test_marker))

    def test_win_row_3x3(self):
        # Testing win state in Row
        test_board = Board(3, 3)
        test_marker = "X"
        test_board.access_board("1", new_value=test_marker)
        test_board.access_board("2", new_value=test_marker)
        test_board.access_board("3", new_value=test_marker)
        self.assertTrue(test_board.win_check(test_marker))

    def test_win_row_4x4(self):
        # Testing win state in Row
        test_board = Board(4, 4)
        test_marker = "X"
        test_board.access_board("1", new_value=test_marker)
        test_board.access_board("2", new_value=test_marker)
        test_board.access_board("3", new_value=test_marker)
        test_board.access_board("4", new_value=test_marker)
        self.assertTrue(test_board.win_check(test_marker))

    def test_row_diagonal_3x3(self):
        # Testing diagonal win states
        test_board = Board(3, 3)
        test_marker = "X"
        test_board.access_board("1", new_value=test_marker)
        test_board.access_board("5", new_value=test_marker)
        test_board.access_board("9", new_value=test_marker)
        self.assertTrue(test_board.win_check(test_marker))

    def test_row_diagonal_4x4(self):
        # Testing diagonal win states
        test_board = Board(4, 4)
        test_marker = "X"
        test_board.access_board("1", new_value=test_marker)
        test_board.access_board("6", new_value=test_marker)
        test_board.access_board("11", new_value=test_marker)
        test_board.access_board("16", new_value=test_marker)
        self.assertTrue(test_board.win_check(test_marker))


if __name__ == "__main__":
    unittest.main()
