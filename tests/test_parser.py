import unittest
from app.parser import Parser
from app.tictactoe import TicTacToe


class TestParser(unittest.TestCase):
    def test_parser(self):
        parser = Parser.create_parser()
        args = parser.parse_args(["-server"])
        self.assertEqual(args.server, True)

    def test_start_game_in_server_mode(self):
        parser = Parser.create_parser()
        args = parser.parse_args(["-server"])
        test_players = [["Marx", "human", "X"], ["Engels", "human", "$"]]
        size = 3
        test_game = TicTacToe(size, test_players, server=args.server)
        self.assertEqual(test_game.server, True)
