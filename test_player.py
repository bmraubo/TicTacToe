import unittest
from player import HumanPlayer, ComputerPlayer
from board import Board


class TestHumanPlayer(unittest.TestCase):
    def test_get_player_move(self):
        test_player_info = ["Marx", "human", "X"]
        test_player = HumanPlayer(test_player_info)
        player_move = "3"
        self.assertEqual(
            test_player.get_player_move(player_move=player_move), player_move
        )


class TestComputerPlayer(unittest.TestCase):
    def test_get_player_move(self):
        test_player_info = ["Rosa", "computer", "Y"]
        test_player = ComputerPlayer(test_player_info)
        test_board = Board(3)
        expected_move = "1"
        self.assertEqual(test_player.get_player_move(test_board), expected_move)
