import unittest
from app.player import HumanPlayer, ComputerPlayer
from app.board import Board


class TestHumanPlayer(unittest.TestCase):
    def test_get_human_player_move(self):
        test_player_info = ["Marx", "human", "X"]
        test_player = HumanPlayer(test_player_info)
        player_move = "3"
        self.assertEqual(
            test_player.get_player_move(player_move=player_move), player_move
        )


class TestComputerPlayer(unittest.TestCase):
    def test_get_computer_player_move_first_available(self):
        test_board = Board(3)
        test_player_info = ["Rosa", "computer", "Y"]
        test_player = ComputerPlayer(test_player_info, test_board)
        expected_move = "1"
        self.assertEqual(test_player.get_player_move(), expected_move)

    def test_computer_player_move_find_win(self):
        test_board = Board(3)
        test_player_info = ["Rosa", "computer", "Y"]
        test_player = ComputerPlayer(test_player_info, test_board)
        # Create a board state where win is possible
        test_board.change_board_value("4", "Y")
        test_board.change_board_value("6", "Y")
        expected_move = "5"
        self.assertEqual(test_player.get_player_move(), expected_move)
