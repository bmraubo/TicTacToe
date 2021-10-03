import unittest
import sys
from io import StringIO
from ui import UserInterface


class TestUserInterface(unittest.TestCase):

    # Testing welcome message and game instructions
    def test_welcome_message(self):
        # Tests display of welcome message
        captured_output = StringIO()
        sys.stdout = captured_output
        UserInterface.welcome_message()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Welcome to Tic Tac Toe")

    def test_game_instructions(self):
        # Tests Display of Game Instructions
        captured_output = StringIO()
        sys.stdout = captured_output
        UserInterface.game_instructions()
        validate_instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        output = captured_output.getvalue().strip()
        self.assertEqual(output, validate_instructions)


if __name__ == "__main__":
    unittest.main()
