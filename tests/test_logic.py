import unittest
from app.logic import MoveLogic
from app.board import Board
from app.util import Utilities


class TestMoveLogic(unittest.TestCase):

    # Validate Move
    def test_validate_move_valueerror(self):
        # Test for value error exception handling
        size = 3
        test_board = Board()
        test_board.create_board(3)
        player_move = "j"
        self.assertFalse(MoveLogic.validate_move(test_board, player_move, size)[0])

    def test_validate_move_out_of_range(self):
        # Rejects moves that are outside of permitted range
        size = 3
        test_board = Board()
        test_board.create_board(3)
        player_move = "10"
        self.assertFalse(MoveLogic.validate_move(test_board, player_move, size)[0])
        # Tests inputs within range, for completeness => should be allowed
        player_move = "9"
        self.assertTrue(MoveLogic.validate_move(test_board, player_move, size)[0])

    def test_validate_move_already_played(self):
        # Rejects move if it has already been played
        size = 3
        test_board = Board()
        test_board.create_board(size)
        test_input = "1"
        test_marker = "X"
        Utilities.change_board_value(test_board.board_data, test_input, test_marker)
        # 1 has already been played, so playing it again should return False
        player_move = "1"
        self.assertFalse(MoveLogic.validate_move(test_board, player_move, size)[0])
        # 2 has not been played - it should pass validation and return True
        player_move = "2"
        self.assertTrue(MoveLogic.validate_move(test_board, player_move, size)[0])
