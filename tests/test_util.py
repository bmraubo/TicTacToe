import unittest
from app.util import Utilities
from app.board import Board
from app.player import HumanPlayer


class TestUtilities(unittest.TestCase):

    # Testing reading and writing board values
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

    # Testing game info payload generation
    def test_generate_payload(self):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        request_data = Utilities.generate_payload(test_board, test_player, test_move)
        expected_package = {
            "board": {
                "board_data": test_board.board_data,
                "size": test_board.size,
                "highest_value": test_board.highest_value,
                "arrangements": test_board.arrangements,
                "winner": test_board.winner,
                "moves_made": test_board.moves_made,
            },
            "player": {
                "name": test_player.name,
                "type": test_player.type,
                "marker": test_player.marker,
            },
            "move": test_move,
        }
        self.assertEqual(request_data, expected_package)

    def test_generate_payload_empty_board(self):
        test_board = Board()
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        request_data = Utilities.generate_payload(test_board, test_player, test_move)
        expected_package = {
            "board": {
                "board_data": {},
                "size": None,
                "highest_value": None,
                "arrangements": None,
                "winner": None,
                "moves_made": 0,
            },
            "player": {
                "name": test_player.name,
                "type": test_player.type,
                "marker": test_player.marker,
            },
            "move": test_move,
        }
        self.assertEqual(request_data, expected_package)
