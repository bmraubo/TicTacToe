import unittest
from app.board import Board
from server.processmove import ProcessMove
from server.serverlogic import ServerLogic


class TestServer(unittest.TestCase):
    def test_check_request_true(self):
        test_board = Board(3).board
        test_request = {
            "player": "X",
            "board_size": "3",
            "board": test_board,
            "move": "4",
            "moves_made": 0,
        }
        self.assertEqual(ProcessMove.check_request(test_request), (True, "OK"))

    def test_check_request_false(self):
        test_request = {
            "player": "X",
            "board_size": 3,
            "move": "4",
            "moves_made": "0",
        }
        self.assertEqual(
            ProcessMove.check_request(test_request), (False, "No board information")
        )

    def test_prepare_response_data(self):
        size = 3
        test_board = Board(size).board
        test_request = {
            "player": "X",
            "board_size": size,
            "board": test_board,
            "move": "4",
            "moves_made": 0,
        }
        new_board_state = ServerLogic.change_board_value(
            test_request["board"], test_request["move"], test_request["player"]
        )
        game_status = ServerLogic.end_game_check(
            test_request["board"],
            test_request["moves_made"],
            test_request["player"],
            test_request["board_size"],
        )
        expected_response = {
            "board": new_board_state,
            "game_status": game_status[1],
            "moves_made": 1,
        }
        self.assertEqual(
            ProcessMove.prepare_response_data(
                new_board_state, game_status, test_request["moves_made"]
            ),
            expected_response,
        )


if __name__ == "__main__":
    unittest.main()
