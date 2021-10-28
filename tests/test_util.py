import unittest
from app.util import Utilities
from app.board import Board


class TestUtilities(unittest.TestCase):
    def test_check_board_value(self):
        test_board = Board()
        test_board.create_board(3)
        value = "4"
        self.assertEqual(Utilities.check_board_value(test_board.board_data, value), "4")

    def test_change_board_value(self):
        # Set up game
        test_board = Board()
        test_board.create_board(3)
        # Test move
        test_input = "1"
        marker = "X"
        Utilities.change_board_value(test_board.board_data, test_input, marker)
        self.assertEqual(
            Utilities.check_board_value(test_board.board_data, test_input), "X"
        )
