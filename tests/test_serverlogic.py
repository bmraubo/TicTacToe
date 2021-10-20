import unittest
from app.board import Board
from app.serverlogic import ServerLogic


class TestLogic(unittest.TestCase):
    def test_check_board_value(self):
        test_board = Board(3).board
        test_request = {
            "player": "X",
            "board": test_board,
            "move": "4",
        }
        self.assertEqual(
            ServerLogic.check_board_value(test_request["board"], test_request["move"]),
            "4",
        )

    def test_change_board_value(self):
        # Set up game
        test_board = Board(3).board
        # Test move
        test_request = {
            "player": "X",
            "board": test_board,
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
        test_board = Board(3).board
        test_request = {
            "player": "X",
            "board": test_board,
            "move": "j",
        }
        self.assertFalse(
            ServerLogic.validate_move(test_request["board"], test_request["move"])
        )

    def test_validate_move_out_of_range(self):
        # Rejects moves that are outside of permitted range
        test_board = Board(3).board
        test_request = {
            "player": "X",
            "board": test_board,
            "move": "10",
        }
        self.assertFalse(
            ServerLogic.validate_move(test_request["board"], test_request["move"])
        )
        test_request = {
            "player": "X",
            "board": test_board,
            "move": "0",
        }
        self.assertFalse(
            ServerLogic.validate_move(test_request["board"], test_request["move"])
        )
        # Tests inputs within range, for completeness => should be allowed
        test_request = {
            "player": "X",
            "board": test_board,
            "move": "9",
        }
        self.assertTrue(
            ServerLogic.validate_move(test_request["board"], test_request["move"])
        )
        test_request = {
            "player": "X",
            "board": test_board,
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

    # Testing Win Arrangement Generation
    def test_win_arrangement_generator_3x3(self):
        size = 3
        test_board = Board(size).board
        expected_rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        expected_columns = [["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"]]
        expected_diagonals = [["1", "5", "9"], ["3", "5", "7"]]
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertEqual(arrangements["rows"], expected_rows)
        self.assertEqual(arrangements["columns"], expected_columns)
        self.assertEqual(arrangements["diagonals"], expected_diagonals)

    def test_win_arrangement_generator_4x4(self):
        size = 4
        test_board = Board(4).board
        expected_rows = [
            ["1", "2", "3", "4"],
            ["5", "6", "7", "8"],
            ["9", "10", "11", "12"],
            ["13", "14", "15", "16"],
        ]
        expected_columns = [
            ["1", "5", "9", "13"],
            ["2", "6", "10", "14"],
            ["3", "7", "11", "15"],
            ["4", "8", "12", "16"],
        ]
        expected_diagonals = [["1", "6", "11", "16"], ["4", "7", "10", "13"]]
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertEqual(arrangements["rows"], expected_rows)
        self.assertEqual(arrangements["columns"], expected_columns)
        self.assertEqual(arrangements["diagonals"], expected_diagonals)

    # Checking for Win conditions
    def test_no_win_3x3(self):
        # test win check where no win or draw state exists
        size = 3
        test_board = Board(size).board
        test_marker = "X"
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertFalse(
            ServerLogic.win_check(test_board, test_marker, arrangements, size)
        )

    def test_no_win_4x4(self):
        # test win check where no win or draw state exists
        size = 4
        test_board = Board(size).board
        test_marker = "X"
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertFalse(
            ServerLogic.win_check(test_board, test_marker, arrangements, size)
        )

    def test_win_column_3x3(self):
        # testing Win state in column
        # Set up a game
        size = 3
        test_board = Board(size).board
        test_marker = "X"
        ServerLogic.change_board_value(test_board, "1", test_marker)
        ServerLogic.change_board_value(test_board, "4", test_marker)
        ServerLogic.change_board_value(test_board, "7", test_marker)
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertTrue(
            ServerLogic.win_check(test_board, test_marker, arrangements, size)
        )

    def test_win_column_4x4(self):
        # testing Win state in column
        size = 4
        # Set up a game
        test_board = Board(size).board
        test_marker = "X"
        ServerLogic.change_board_value(test_board, "1", test_marker)
        ServerLogic.change_board_value(test_board, "5", test_marker)
        ServerLogic.change_board_value(test_board, "9", test_marker)
        ServerLogic.change_board_value(test_board, "13", test_marker)
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertTrue(
            ServerLogic.win_check(test_board, test_marker, arrangements, size)
        )

    def test_win_row_3x3(self):
        size = 3
        # Testing win state in Row
        test_board = Board(size).board
        test_marker = "X"
        ServerLogic.change_board_value(test_board, "1", test_marker)
        ServerLogic.change_board_value(test_board, "2", test_marker)
        ServerLogic.change_board_value(test_board, "3", test_marker)
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertTrue(
            ServerLogic.win_check(test_board, test_marker, arrangements, size)
        )

    def test_win_row_4x4(self):
        size = 4
        # Testing win state in Row
        test_board = Board(size).board
        test_marker = "X"
        ServerLogic.change_board_value(test_board, "1", test_marker)
        ServerLogic.change_board_value(test_board, "2", test_marker)
        ServerLogic.change_board_value(test_board, "3", test_marker)
        ServerLogic.change_board_value(test_board, "4", test_marker)
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertTrue(
            ServerLogic.win_check(test_board, test_marker, arrangements, size)
        )

    def test_row_diagonal_3x3(self):
        size = 3
        # Testing diagonal win states
        test_board = Board(size).board
        test_marker = "X"
        ServerLogic.change_board_value(test_board, "1", test_marker)
        ServerLogic.change_board_value(test_board, "5", test_marker)
        ServerLogic.change_board_value(test_board, "9", test_marker)
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertTrue(
            ServerLogic.win_check(test_board, test_marker, arrangements, size)
        )

    def test_row_diagonal_4x4(self):
        size = 4
        # Testing win state in Row
        test_board = Board(size).board
        test_marker = "X"
        ServerLogic.change_board_value(test_board, "1", test_marker)
        ServerLogic.change_board_value(test_board, "6", test_marker)
        ServerLogic.change_board_value(test_board, "11", test_marker)
        ServerLogic.change_board_value(test_board, "16", test_marker)
        arrangements = ServerLogic.generate_win_arrangements(test_board, size)
        self.assertTrue(
            ServerLogic.win_check(test_board, test_marker, arrangements, size)
        )

    # End Game Checks - Draw
    def test_end_game_draw(self):
        size = 3
        test_board = Board(size).board
        test_marker = "X"
        moves_made = 9
        self.assertEqual(
            ServerLogic.end_game_check(test_board, moves_made, test_marker, size),
            (True, "Draw"),
        )


if __name__ == "__main__":
    unittest.main()
