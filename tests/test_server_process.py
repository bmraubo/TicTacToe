import unittest
from app.board import Board
from app.player import HumanPlayer
from app.util import Utilities
from app.server_process import ServerProcess


class TestLogic(unittest.TestCase):
    def server_process_test_set_up(test_move):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        request_data = Utilities.generate_payload(test_board, test_player, test_move)
        return request_data

    def test_server_process(self):
        test_move = "1"
        request_data = TestLogic.server_process_test_set_up(test_move)
        response_data = ServerProcess.server_process(request_data)
        self.assertTrue(response_data[0]["move_success"])
        self.assertEqual(
            Utilities.check_board_value(
                response_data[0]["game_data"]["board"]["board_data"], "1"
            ),
            "X",
        )

    def test_server_process_bad_move(self):
        test_move = "g"
        request_data = TestLogic.server_process_test_set_up(test_move)
        response_data = ServerProcess.server_process(request_data)
        self.assertFalse(response_data[0]["move_success"])

    def test_server_process_increase_moves_made(self):
        test_move = "1"
        request_data = TestLogic.server_process_test_set_up(test_move)
        response_data = ServerProcess.server_process(request_data)
        self.assertEqual(response_data[0]["game_data"]["board"]["moves_made"], 1)

    def test_request_data_check(self):
        test_move = "1"
        request_data = TestLogic.server_process_test_set_up(test_move)
        self.assertTrue(ServerProcess.request_data_check(request_data))

    def test_request_data_check_top_level_key_missing(self):
        test_move = "1"
        request_data = TestLogic.server_process_test_set_up(test_move)
        del request_data["board"]
        self.assertFalse(ServerProcess.request_data_check(request_data))

    def test_request_data_check_board_data_key_missing(self):
        test_move = "1"
        request_data = TestLogic.server_process_test_set_up(test_move)
        del request_data["board"]["board_data"]
        self.assertFalse(ServerProcess.request_data_check(request_data))

    def test_request_data_check_player_name_missing(self):
        test_move = "1"
        request_data = TestLogic.server_process_test_set_up(test_move)
        del request_data["player"]["name"]
        self.assertFalse(ServerProcess.request_data_check(request_data))
