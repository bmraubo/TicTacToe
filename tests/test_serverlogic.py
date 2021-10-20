import unittest
from app.board import Board
from app.serverlogic import ServerLogic


class TestLogic(unittest.TestCase):
    def test_check_board_value(self):
        test_board = Board(3)
        test_request = {
            "player": "X",
            "board": test_board.board,
            "move": "4",
        }
        self.assertEqual(
            ServerLogic.check_board_value(test_request["board"], test_request["move"]),
            "4",
        )

    def test_change_board_value(self):
        # Set up game
        test_board = Board(3)
        # Test move
        test_request = {
            "player": "X",
            "board": test_board.board,
            "move": "4",
        }
        test_board = ServerLogic.change_board_value(
            test_request["board"], test_request["move"], test_request["player"]
        )
        self.assertEqual(
            ServerLogic.check_board_value(test_request["board"], test_request["move"]),
            test_request["player"],
        )

    def test_validate_move_valueerror(self):
        # Test for value error exception handling
        test_board = Board(3)
        test_request = {
            "player": "X",
            "board": test_board.board,
            "move": "j",
        }
        self.assertFalse(
            ServerLogic.validate_move(test_request["board"], test_request["move"])
        )

    def test_validate_move_out_of_range(self):
        # Rejects moves that are outside of permitted range
        test_board = Board(3)
        test_request = {
            "player": "X",
            "board": test_board.board,
            "move": "10",
        }
        self.assertFalse(
            ServerLogic.validate_move(test_request["board"], test_request["move"])
        )
        test_request = {
            "player": "X",
            "board": test_board.board,
            "move": "0",
        }
        self.assertFalse(
            ServerLogic.validate_move(test_request["board"], test_request["move"])
        )
        # Tests inputs within range, for completeness => should be allowed
        test_request = {
            "player": "X",
            "board": test_board.board,
            "move": "9",
        }
        self.assertTrue(
            ServerLogic.validate_move(test_request["board"], test_request["move"])
        )
        test_request = {
            "player": "X",
            "board": test_board.board,
            "move": "1",
        }
        self.assertTrue(
            ServerLogic.validate_move(test_request["board"], test_request["move"])
        )

    def test_validate_move_already_played(self):
        # Rejects move if it has already been played
        test_board = Board(3).board
        test_board["1"] = "X"
        test_request = {
            "player": "X",
            "board": test_board,
            "move": "1",
        }
        # Running validation on square 1 should fail
        self.assertFalse(ServerLogic.validate_move(test_board, test_request["move"]))
        # However a request to change square 2 should pass
        test_request = {
            "player": "X",
            "board": test_board,
            "move": "2",
        }
        self.assertTrue(ServerLogic.validate_move(test_board, test_request["move"]))


if __name__ == "__main__":
    unittest.main()
