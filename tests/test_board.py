import unittest
from app.board import Board
from app.player import HumanPlayer
from app.util import Utilities
from app.server_process import ServerProcess


class TestBoard(unittest.TestCase):
    expected_board_information = {
        "size3": {
            "board": {
                "1": "1",
                "2": "2",
                "3": "3",
                "4": "4",
                "5": "5",
                "6": "6",
                "7": "7",
                "8": "8",
                "9": "9",
            },
            "rows": [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]],
            "columns": [["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"]],
            "diagonals": [["1", "5", "9"], ["3", "5", "7"]],
        },
        "size4": {
            "board": {
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
            },
            "rows": [
                ["1", "2", "3", "4"],
                ["5", "6", "7", "8"],
                ["9", "10", "11", "12"],
                ["13", "14", "15", "16"],
            ],
            "columns": [
                ["1", "5", "9", "13"],
                ["2", "6", "10", "14"],
                ["3", "7", "11", "15"],
                ["4", "8", "12", "16"],
            ],
            "diagonals": [["1", "6", "11", "16"], ["4", "7", "10", "13"]],
        },
    }

    def create_test_board(size):
        test_board = Board()
        test_board.create_board(size)
        return test_board

    # Testing Board generation

    def test_generate_board_3x3(self):
        expected_board = TestBoard.expected_board_information["size3"]["board"]
        test_board = TestBoard.create_test_board(3)
        self.assertEqual(test_board.board_data, expected_board)

    def test_generate_board_4x4(self):
        expected_board = TestBoard.expected_board_information["size4"]["board"]
        test_board = TestBoard.create_test_board(4)
        self.assertEqual(test_board.board_data, expected_board)

    # Testing Win Arrangement Generator

    def test_win_arrangement_generator_3x3(self):
        test_board = TestBoard.create_test_board(3)
        expected_rows = TestBoard.expected_board_information["size3"]["rows"]
        expected_columns = TestBoard.expected_board_information["size3"]["columns"]
        expected_diagonals = TestBoard.expected_board_information["size3"]["diagonals"]
        self.assertEqual(test_board.arrangements["rows"], expected_rows)
        self.assertEqual(test_board.arrangements["columns"], expected_columns)
        self.assertEqual(test_board.arrangements["diagonals"], expected_diagonals)

    def test_win_arrangement_generator_4x4(self):
        test_board = TestBoard.create_test_board(4)
        expected_rows = TestBoard.expected_board_information["size4"]["rows"]
        expected_columns = TestBoard.expected_board_information["size4"]["columns"]
        expected_diagonals = TestBoard.expected_board_information["size4"]["diagonals"]
        self.assertEqual(test_board.arrangements["rows"], expected_rows)
        self.assertEqual(test_board.arrangements["columns"], expected_columns)
        self.assertEqual(test_board.arrangements["diagonals"], expected_diagonals)

    # Testing local make_move method

    def test_make_move(self):
        test_board = TestBoard.create_test_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        test_board = test_board.make_move(test_player, test_move)[1]
        self.assertEqual(
            Utilities.check_board_value(test_board.board_data, test_move),
            test_player.marker,
        )

    def test_winning_move(self):
        test_board = TestBoard.create_test_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        winning_arrangement = TestBoard.expected_board_information["size3"]["rows"][1]
        for value in winning_arrangement:
            test_board = test_board.make_move(test_player, value)[1]
        self.assertEqual(test_board.winner, test_player.name)

    # Testing server make_move method

    # Mocking server make_move -- this does not use a json, so implementation must take this into account
    def mock_server_make_move(GameBoard, Player, move, server=True):
        def __mock_make_server_request(GameBoard, Player, move):
            request_data = Utilities.generate_payload(GameBoard, Player, move)
            server_response = ServerProcess.server_process(request_data)
            return server_response  # As server_process does not return a json, production code should return server_response.json()

        server_response = __mock_make_server_request(GameBoard, Player, move)[
            0
        ]  # the index is only here because we are not dealing with a json
        if server_response["move_success"]:
            new_board = Board.create_new_board_object(
                server_response["game_data"]["board"]
            )
            return (True, new_board)
        else:
            return (False, server_response["error"])

    def test_make_move_using_server(self):
        test_board = TestBoard.create_test_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        test_board = TestBoard.mock_server_make_move(
            test_board, test_player, test_move, server=True
        )[1]
        self.assertEqual(
            Utilities.check_board_value(test_board.board_data, test_move),
            test_player.marker,
        )

    def test_make_move_using_server_invalid_move(self):
        test_board = TestBoard.create_test_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "g"
        move_outcome = TestBoard.mock_server_make_move(
            test_board, test_player, test_move, server=True
        )
        self.assertFalse(move_outcome[0])

    def test_make_winning_move_on_server(self):
        test_board = TestBoard.create_test_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        test_board.board_data = Utilities.change_board_value(
            test_board.board_data, test_move, test_player.marker
        )
        test_move = "2"
        test_board.board_data = Utilities.change_board_value(
            test_board.board_data, test_move, test_player.marker
        )
        test_winning_move = "3"
        move_outcome = TestBoard.mock_server_make_move(
            test_board, test_player, test_winning_move, server=True
        )
        self.assertEqual(move_outcome[1].winner, "Marx")

    def test_create_board_object_to_send_to_server(self):
        test_board = TestBoard.create_test_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        request_data = Utilities.generate_payload(test_board, test_player, test_move)
        new_board = Board.create_new_board_object(request_data["board"])
        self.assertTrue(new_board.size == 3)

    def test_create_new_board_from_server_data(self):
        test_board = TestBoard.create_test_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        response_game_data = Utilities.generate_payload(
            test_board, test_player, test_move
        )
        response_data = {"move_success": True, "game_data": response_game_data}
        new_board = Board.create_new_board_object(response_data["game_data"]["board"])
        self.assertTrue(new_board.size == 3)

    def test_increasing_moves_made_total(self):
        test_board = TestBoard.create_test_board(3)
        test_board.increase_moves_made_total()
        self.assertEqual(test_board.moves_made, 1)


if __name__ == "__main__":
    unittest.main()
