import unittest
from app.board import Board
from app.player import HumanPlayer
from app.util import Utilities


class TestBoard(unittest.TestCase):
    def test_generate_board_3x3(self):
        expected_board = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }
        test_board = Board()
        test_board.create_board(3)
        self.assertEqual(test_board.board_data, expected_board)

    def test_generate_board_4x4(self):
        expected_board = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "10": "10",
            "11": "11",
            "12": "12",
            "13": "13",
            "14": "14",
            "15": "15",
            "16": "16",
        }
        test_board = Board()
        test_board.create_board(4)
        self.assertEqual(test_board.board_data, expected_board)

    # Testing win check
    def test_win_arrangement_generator_3x3(self):
        test_board = Board()
        test_board.create_board(3)
        expected_rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        expected_columns = [["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"]]
        expected_diagonals = [["1", "5", "9"], ["3", "5", "7"]]
        self.assertEqual(test_board.arrangements["rows"], expected_rows)
        self.assertEqual(test_board.arrangements["columns"], expected_columns)
        self.assertEqual(test_board.arrangements["diagonals"], expected_diagonals)

    def test_win_arrangement_generator_4x4(self):
        test_board = Board()
        test_board.create_board(4)
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
        self.assertEqual(test_board.arrangements["rows"], expected_rows)
        self.assertEqual(test_board.arrangements["columns"], expected_columns)
        self.assertEqual(test_board.arrangements["diagonals"], expected_diagonals)

    def test_make_move(self):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        test_board = test_board.make_move(test_player, test_move)[1]
        self.assertEqual(
            Utilities.check_board_value(test_board.board_data, test_move),
            test_player.marker,
        )

    def test_winning_move(self):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        winning_arrangement = ["1", "4", "7"]
        for value in winning_arrangement:
            test_board = test_board.make_move(test_player, value)[1]
        self.assertEqual(test_board.winner, test_player)

    def test_create_server_board_object(self):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        request_data = Utilities.generate_payload(test_board, test_player, test_move)
        new_board = Board.create_server_board_object(request_data)
        self.assertTrue(new_board.size == 3)

    def test_create_new_board_from_server_data(self):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        response_game_data = Utilities.generate_payload(
            test_board, test_player, test_move
        )
        response_data = {"move_success": True, "game_data": response_game_data}
        new_board = Board.create_new_board_from_server_data(response_data["game_data"])
        self.assertTrue(new_board.size == 3)


if __name__ == "__main__":
    unittest.main()
