import unittest
import sys
from io import StringIO
from tictactoe import *


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)

    def test_ci_workflow(self):
        self.assertEqual(True, True)


class TestApplication(unittest.TestCase):
    def test_welcome_message(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        Info.welcome_message()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Welcome to Tic Tac Toe")

    def test_game_instructions(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        Info.game_instructions()
        validate_instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        output = captured_output.getvalue().strip()
        self.assertEqual(output, validate_instructions)


if __name__ == "__main__":
    unittest.main()
