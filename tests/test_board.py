import unittest
from app.board import Board
from app.gamelogic import GameLogic
from app.player import HumanPlayer


class TestBoard(unittest.TestCase):
    def test_generate_board_3x3(self):
        test_board = Board()
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
        test_board.generate_board(3)
        self.assertEqual(test_board.board, expected_board)

    def test_generate_board_4x4(self):
        test_board = Board()
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
        test_board.generate_board(4)
        self.assertEqual(test_board.board, expected_board)

    def test_make_move(self):
        test_board = Board()
        test_board.generate_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        move = "1"
        test_board.make_move(test_player, move)
        self.assertEqual(GameLogic.check_board_value(test_board.board, "1"), "X")


if __name__ == "__main__":
    unittest.main()
