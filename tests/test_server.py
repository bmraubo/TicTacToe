import unittest
from app.board import Board
from server.server import ProcessMove


class TestServer(unittest.TestCase):
    def test_check_request_true(self):
        test_board = Board(3).board
        test_request = {
            "player": "X",
            "board_size": "3",
            "board": test_board,
            "move": "4",
        }
        self.assertEqual(ProcessMove.check_request(test_request), (True, "OK"))

    def test_check_request_false(self):
        test_request = {
            "player": "X",
            "board_size": "3",
            "move": "4",
        }
        self.assertEqual(
            ProcessMove.check_request(test_request), (False, "No board information")
        )


if __name__ == "__main__":
    unittest.main()
