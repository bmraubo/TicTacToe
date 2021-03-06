import unittest
from app.logic import Logic
from app.board import Board
from app.util import Utilities
from app.player import HumanPlayer


class TestLogic(unittest.TestCase):
    def create_test_board(size):
        test_board = Board()
        test_board.create_board(size)
        return test_board

    # Test move validation

    def test_validate_good_move(self):
        size = 3
        test_board = TestLogic.create_test_board(size)
        test_move = "1"
        self.assertTrue(Logic.validate_move(test_board, test_move))

    def test_validate_move_valueerror(self):
        # Test for value error exception handling
        size = 3
        test_board = TestLogic.create_test_board(size)
        player_move = "j"
        self.assertFalse(Logic.validate_move(test_board, player_move)[0])

    def test_validate_move_out_of_range(self):
        # Rejects moves that are outside of permitted range
        size = 3
        test_board = TestLogic.create_test_board(size)
        player_move = "10"
        self.assertFalse(Logic.validate_move(test_board, player_move)[0])
        # Tests inputs within range, for completeness => should be allowed
        player_move = "9"
        self.assertTrue(Logic.validate_move(test_board, player_move)[0])

    def test_validate_move_already_played(self):
        # Rejects move if it has already been played
        size = 3
        test_board = TestLogic.create_test_board(size)
        test_input = "1"
        test_marker = "X"
        Utilities.change_board_value(test_board.board_data, test_input, test_marker)
        # 1 has already been played, so playing it again should return False
        player_move = "1"
        self.assertFalse(Logic.validate_move(test_board, player_move)[0])
        # 2 has not been played - it should pass validation and return True
        player_move = "2"
        self.assertTrue(Logic.validate_move(test_board, player_move)[0])

    # Win Checks

    # Sets a new board to a winning arrangement for testing
    def set_board_to_win_arrangement(test_board, arrangement, test_marker):
        for value in arrangement:
            Utilities.change_board_value(test_board.board_data, value, test_marker)

    def test_no_win_3x3(self):
        # test win check where no win or draw state exists
        size = 3
        test_board = TestLogic.create_test_board(size)
        test_marker = "X"
        self.assertFalse(Logic.win_check(test_board, test_marker))

    def test_no_win_4x4(self):
        # test win check where no win or draw state exists
        size = 4
        test_board = TestLogic.create_test_board(size)
        test_marker = "X"
        self.assertFalse(Logic.win_check(test_board, test_marker))

    def test_wins_3x3(self):
        winning_arrangements = [["1", "4", "7"], ["1", "2", "3"], ["1", "5", "9"]]
        for arrangement in winning_arrangements:
            size = 3
            test_board = TestLogic.create_test_board(size)
            test_marker = "X"
            TestLogic.set_board_to_win_arrangement(test_board, arrangement, test_marker)
            self.assertTrue(Logic.win_check(test_board, test_marker))

    def test_wins_4x4(self):
        winning_arrangements = [
            ["1", "5", "9", "13"],
            ["1", "2", "3", "4"],
            ["1", "6", "11", "16"],
        ]
        for arrangement in winning_arrangements:
            size = 4
            test_board = TestLogic.create_test_board(size)
            test_marker = "X"
            TestLogic.set_board_to_win_arrangement(test_board, arrangement, test_marker)
            self.assertTrue(Logic.win_check(test_board, test_marker))
