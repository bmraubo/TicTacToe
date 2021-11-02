import unittest
from app.parser import Parser


class TestParser(unittest.TestCase):
    def test_parser(self):
        args = ["-server"]
        test_server_mode = Parser.run_parser(args)
        self.assertTrue(test_server_mode)
