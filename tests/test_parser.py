import unittest
from app.parser import Parser
from app.tictactoe import TicTacToe


class TestParser(unittest.TestCase):
    def test_parser(self):
        parser = Parser.create_parser()
        test_server_mode = parser.parse_args(["-server"])
        self.assertTrue(test_server_mode)

    def test_start_game_in_server_mode(self):
        parser = Parser.create_parser()
        test_server_mode = parser.parse_args(["-server"])
        test_players = [["Marx", "human", "X"], ["Engels", "human", "$"]]
        size = 3
        test_game = TicTacToe(size, test_players, server=test_server_mode)
        self.assertTrue(test_game.server)
