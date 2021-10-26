import unittest
from app.board import Board
from app.gameprocess import GameProcess
from app.player import HumanPlayer


class TestGameProcess(unittest.TestCase):

    # Check Board Value
    def test_check_board_value(self):
        test_board = Board(3)
        value = "4"
        self.assertEqual(GameProcess.check_board_value(test_board.board, value), "4")

    # Change Board Value
    def test_change_board_value(self):
        test_board = Board(3)
        # Test move information
        test_input = "1"
        marker = "X"
        # Make Move
        test_board.board = GameProcess.change_board_value(
            test_board.board, test_input, marker
        )
        self.assertEqual(
            GameProcess.check_board_value(test_board.board, test_input), "X"
        )

    # Package Move Information
    def test_package_move_information(self):
        test_board = Board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        moves_made = 0
        player_move = "1"
        expected_dict = {
            "player": {
                "name": test_player.name,
                "marker": test_player.marker,
            },
            "board": {
                "state": test_board.board,
                "size": 3,
            },
            "move": {"move": player_move, "move_number": moves_made},
        }
        self.assertEqual(
            GameProcess.package_move_information(
                test_board, test_player, player_move, moves_made
            ),
            expected_dict,
        )

    # Read Move Response


if __name__ == "__main__":
    unittest.main()
