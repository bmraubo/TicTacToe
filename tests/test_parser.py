import unittest
from app.tictactoe import TicTacToe


class TestParser(unittest.TestCase):
    def test_parser(self):
        test_parser = Parser.create_parser()
        test_server_mode = test_parser.parse_args("-server")
        self.assertTrue(test_server_mode)
