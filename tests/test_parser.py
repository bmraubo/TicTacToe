import unittest
from app.parser import Parser


class TestParser(unittest.TestCase):
    def test_parser(self):
        parser = Parser.create_parser()
        test_server_mode = parser.parse_args(["-server"])
        self.assertTrue(test_server_mode)
