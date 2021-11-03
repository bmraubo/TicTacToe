import unittest
from app.board import Board
from app.player import HumanPlayer
from app.util import Utilities
from app.server_process import ServerProcess


class TestServerProcess(unittest.TestCase):
    def server_process_test_set_up(test_move):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        request_data = Utilities.generate_payload(test_board, test_player, test_move)
        return request_data

    def test_server_process(self):
        test_move = "1"
        request_data = TestServerProcess.server_process_test_set_up(test_move)
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
        request_data = TestServerProcess.server_process_test_set_up(test_move)
        response_data = ServerProcess.server_process(request_data)
        self.assertFalse(response_data[0]["move_success"])

    def test_server_process_increase_moves_made(self):
        test_move = "1"
        request_data = TestServerProcess.server_process_test_set_up(test_move)
        response_data = ServerProcess.server_process(request_data)
        self.assertEqual(response_data[0]["game_data"]["board"]["moves_made"], 1)

    def test_server_process_declare_endgame(self):
        test_move = "1"
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_board.board_data = {
            "1": "1",
            "2": "X",
            "3": "X",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }
        request_data = Utilities.generate_payload(test_board, test_player, test_move)
        response_data = ServerProcess.server_process(request_data)
        self.assertEqual(response_data[0]["game_data"]["board"]["winner"], "Marx")

    def test_request_data_check(self):
        test_move = "1"
        request_data = TestServerProcess.server_process_test_set_up(test_move)
        data_check_outcome = ServerProcess.request_data_check(request_data)
        self.assertTrue(data_check_outcome[0])

    def test_request_data_check_top_level_key_missing(self):
        test_move = "1"
        request_data = TestServerProcess.server_process_test_set_up(test_move)
        del request_data["board"]
        data_check_outcome = ServerProcess.request_data_check(request_data)
        expected_error_message = "Error: board information missing from request payload"
        self.assertFalse(data_check_outcome[0])
        self.assertEqual(data_check_outcome[1], expected_error_message)

    def test_request_data_check_board_data_key_missing(self):
        test_move = "1"
        request_data = TestServerProcess.server_process_test_set_up(test_move)
        del request_data["board"]["board_data"]
        data_check_outcome = ServerProcess.request_data_check(request_data)
        expected_error_message = (
            "Error: board.board_data information missing from request payload"
        )
        self.assertFalse(data_check_outcome[0])
        self.assertEqual(data_check_outcome[1], expected_error_message)

    def test_request_data_check_player_name_missing(self):
        test_move = "1"
        request_data = TestServerProcess.server_process_test_set_up(test_move)
        del request_data["player"]["name"]
        data_check_outcome = ServerProcess.request_data_check(request_data)
        expected_error_message = (
            "Error: player.name information missing from request payload"
        )
        self.assertFalse(data_check_outcome[0])
        self.assertEqual(data_check_outcome[1], expected_error_message)

    def test_integration_request_data_check(self):
        test_move = "1"
        request_data = TestServerProcess.server_process_test_set_up(test_move)
        del request_data["board"]
        expected_error_message = "Error: board information missing from request payload"
        response_data = ServerProcess.server_process(request_data)
        self.assertFalse(response_data[0]["move_success"])
        self.assertEqual(response_data[0]["error"], expected_error_message)
