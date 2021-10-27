import unittest
from app.gamelogic import GameLogic
from app.board import Board


class TestGameLogic(unittest.TestCase):

    # Testing Reading and Manipulating Board
    def test_check_board_value(self):
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        value = "4"
        self.assertEqual(GameLogic.check_board_value(test_board.board, value), "4")

    def test_change_board_value(self):
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        test_input = "1"
        marker = "X"
        updated_board = GameLogic.change_board_value(
            test_board.board, test_input, marker
        )
        self.assertEqual(GameLogic.check_board_value(updated_board, test_input), "X")

    # Testing Board Validation
    def test_validate_move_valueerror(self):
        # Test for value error exception handling
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        player_move = "j"
        self.assertFalse(GameLogic.validate_move(test_board, player_move)[0])

    def test_validate_move_out_of_range(self):
        # Rejects moves that are outside of permitted range
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        player_move = "10"
        self.assertFalse(GameLogic.validate_move(test_board, player_move)[0])
        player_move = "0"
        self.assertFalse(GameLogic.validate_move(test_board, player_move)[0])
        # Tests inputs within range, for completeness => should be allowed
        player_move = "9"
        self.assertTrue(GameLogic.validate_move(test_board, player_move)[0])
        player_move = "1"
        self.assertTrue(GameLogic.validate_move(test_board, player_move)[0])

    def test_validate_move_already_played(self):
        # Rejects move if it has already been played
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        test_input = "1"
        marker = "X"
        GameLogic.change_board_value(test_board, test_input, marker)
        player_move = "1"
        self.assertFalse(GameLogic.validate_move(test_board, player_move)[0])
        player_move = "2"
        self.assertTrue(GameLogic.validate_move(test_board, player_move)[0])

    # Testing generation of winning arrangements for win checks
    def test_win_arrangement_generator_3x3(self):
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        expected_rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        expected_columns = [["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"]]
        expected_diagonals = [["1", "5", "9"], ["3", "5", "7"]]
        arrangements = GameLogic.generate_win_arrangements(test_board, size)
        self.assertEqual(arrangements["rows"], expected_rows)
        self.assertEqual(arrangements["columns"], expected_columns)
        self.assertEqual(arrangements["diagonals"], expected_diagonals)

    def test_win_arrangement_generator_4x4(self):
        size = 4
        test_board = Board()
        test_board.generate_board(size)
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
        arrangements = GameLogic.generate_win_arrangements(test_board, size)
        self.assertEqual(arrangements["rows"], expected_rows)
        self.assertEqual(arrangements["columns"], expected_columns)
        self.assertEqual(arrangements["diagonals"], expected_diagonals)

    # Testing Win Checks
    def test_no_win_3x3(self):
        # test win check where no win or draw state exists
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        test_marker = "X"
        self.assertFalse(GameLogic.win_check(test_board, test_marker, size))

    def test_no_win_4x4(self):
        # test win check where no win or draw state exists
        size = 4
        test_board = Board()
        test_board.generate_board(size)
        test_marker = "X"
        self.assertFalse(GameLogic.win_check(test_board, test_marker, size))

    def test_win_column_3x3(self):
        # testing Win state in column
        # Set up a game
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        test_marker = "X"
        test_board = GameLogic.change_board_value(test_board, "1", test_marker)
        test_board = GameLogic.change_board_value(test_board, "4", test_marker)
        test_board = GameLogic.change_board_value(test_board, "7", test_marker)
        self.assertTrue(GameLogic.win_check(test_board, test_marker, size))

    def test_win_column_4x4(self):
        # testing Win state in column
        # Set up a game
        size = 4
        test_board = Board()
        test_board.generate_board(size)
        test_marker = "X"
        test_board = GameLogic.change_board_value(test_board, "1", test_marker)
        test_board = GameLogic.change_board_value(test_board, "5", test_marker)
        test_board = GameLogic.change_board_value(test_board, "9", test_marker)
        test_board = GameLogic.change_board_value(test_board, "13", test_marker)
        self.assertTrue(GameLogic.win_check(test_board, test_marker, size))

    def test_win_row_3x3(self):
        # Testing win state in Row
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        test_marker = "X"
        test_board = GameLogic.change_board_value(test_board, "1", test_marker)
        test_board = GameLogic.change_board_value(test_board, "2", test_marker)
        test_board = GameLogic.change_board_value(test_board, "3", test_marker)
        self.assertTrue(GameLogic.win_check(test_board, test_marker, size))

    def test_win_row_4x4(self):
        # Testing win state in Row
        size = 4
        test_board = Board()
        test_board.generate_board(size)
        test_marker = "X"
        test_board = GameLogic.change_board_value(test_board, "1", test_marker)
        test_board = GameLogic.change_board_value(test_board, "2", test_marker)
        test_board = GameLogic.change_board_value(test_board, "3", test_marker)
        test_board = GameLogic.change_board_value(test_board, "4", test_marker)
        self.assertTrue(GameLogic.win_check(test_board, test_marker, size))

    def test_row_diagonal_3x3(self):
        # Testing diagonal win states
        size = 3
        test_board = Board()
        test_board.generate_board(size)
        test_marker = "X"
        test_board = GameLogic.change_board_value(test_board, "1", test_marker)
        test_board = GameLogic.change_board_value(test_board, "5", test_marker)
        test_board = GameLogic.change_board_value(test_board, "9", test_marker)
        self.assertTrue(GameLogic.win_check(test_board, test_marker, size))

    def test_row_diagonal_4x4(self):
        # Testing diagonal win states
        size = 4
        test_board = Board()
        test_board.generate_board(size)
        test_marker = "X"
        test_board = GameLogic.change_board_value(test_board, "1", test_marker)
        test_board = GameLogic.change_board_value(test_board, "6", test_marker)
        test_board = GameLogic.change_board_value(test_board, "11", test_marker)
        test_board = GameLogic.change_board_value(test_board, "16", test_marker)
        self.assertTrue(GameLogic.win_check(test_board, test_marker, size))


if __name__ == "__main__":
    unittest.main()
