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
        UserInterface.game_instructions(3)
        validate_instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        output = captured_output.getvalue().strip()
        self.assertEqual(output, validate_instructions)

    def test_get_player_name(self):
        player_name = "Marx"
        self.assertEqual(UserInterface.get_player_name(player_name=player_name), "Marx")

    def test_get_player_type(self):
        player_type = "human"
        self.assertEqual(
            UserInterface.get_player_type(player_type=player_type), "human"
        )

    def test_validate_player_type(self):
        player_type = "Human"
        self.assertTrue(UserInterface.validate_player_type(player_type))
        player_type = "Cuman"
        self.assertFalse(UserInterface.validate_player_type(player_type))

    def test_add_custom_marker(self):
        custom_marker = "$"
        self.assertEqual(
            UserInterface.add_custom_marker(custom_marker=custom_marker), custom_marker
        )

    def test_validate_custom_marker_already_used(self):
        custom_marker_list = ["$"]
        custom_marker = "$"
        self.assertFalse(
            UserInterface.validate_custom_marker(custom_marker, custom_marker_list)
        )
        custom_marker = "£"
        self.assertTrue(
            UserInterface.validate_custom_marker(custom_marker, custom_marker_list)
        )

    def test_validate_custom_marker_too_long(self):
        custom_marker_list = []
        custom_marker = "howdy"
        self.assertFalse(
            UserInterface.validate_custom_marker(custom_marker, custom_marker_list)
        )
        custom_marker = "H"
        self.assertTrue(
            UserInterface.validate_custom_marker(custom_marker, custom_marker_list)
        )

    def test_validate_custom_marker_numbers(self):
        # Numbers are not allowed
        custom_marker_list = []
        custom_marker = "1"
        self.assertFalse(
            UserInterface.validate_custom_marker(custom_marker, custom_marker_list)
        )


if __name__ == "__main__":
    unittest.main()
