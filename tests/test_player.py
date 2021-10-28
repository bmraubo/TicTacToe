import unittest
from app.player import Player, HumanPlayer, ComputerPlayer
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
    def test_get_computer_player_move(self):
        test_board = Board()
        test_board.create_board(3)
        test_player_info = ["Rosa", "computer", "Y"]
        test_player = ComputerPlayer(test_player_info, test_board)
        expected_move = "1"
        self.assertEqual(test_player.get_player_move(), expected_move)


class TestServerPlayer(unittest.TestCase):
    def test_create_server_player_object(self):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        request_data = Board.package_request(test_board, test_player, test_move)
        new_player = Player.create_server_player_object(request_data)
        self.assertTrue(new_player.name == "Marx")
