import unittest
from app.board import Board
from app.player import HumanPlayer
from app.util import Utilities
from app.server_process import ServerProcess


class TestLogic(unittest.TestCase):
    def test_server_process(self):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        request_data = Utilities.generate_payload(test_board, test_player, test_move)
        response_data = ServerProcess.server_process(request_data)
        self.assertTrue(response_data["move_success"])
        self.assertEqual(
            Utilities.check_board_value(
                response_data["game_data"]["board"]["board_state"], "1"
            ),
            "X",
        )
