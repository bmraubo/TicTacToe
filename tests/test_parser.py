import unittest
from app.parser import Parser


class TestParser(unittest.TestCase):
    def test_parser(self):
        test_server_mode = Parser.run_parser()
        self.assertTrue(test_server_mode)
