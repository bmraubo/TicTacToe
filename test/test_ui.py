import unittest
import sys
from io import StringIO
from ui import UserInterface


class TestUserInterface(unittest.TestCase):

    # Testing welcome message and game instructions
    def test_display_welcome_message(self):
        # Tests display of welcome message
        captured_output = StringIO()
        sys.stdout = captured_output
        UserInterface.display_welcome_message()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Welcome to Tic Tac Toe")

    def test_display_game_instructions(self):
        # Tests Display of Game Instructions
        captured_output = StringIO()
        sys.stdout = captured_output
        UserInterface.display_game_instructions(3)
        validate_instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        output = captured_output.getvalue().strip()
        self.assertEqual(output, validate_instructions)

    # Testing User Input of Player Information\
    # Testing obtaining player name
    def test_input_player_name(self):
        player_name = "Marx"
        self.assertEqual(
            UserInterface.input_player_name(player_name=player_name), "Marx"
        )

    # Testing obtaining and validating player type
    def test_input_player_type(self):
        player_type = "human"
        self.assertEqual(
            UserInterface.input_player_type(player_type=player_type), "human"
        )

    def test_validate_player_type(self):
        player_type = "Human"
        self.assertTrue(UserInterface.validate_player_type(player_type))
        player_type = "Cuman"
        self.assertFalse(UserInterface.validate_player_type(player_type))

    # Testing obtaining and validating custom marker
    def test_input_custom_marker(self):
        custom_marker = "$"
        self.assertEqual(
            UserInterface.input_custom_marker(custom_marker=custom_marker),
            custom_marker,
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
        custom_marker = "8"
        self.assertFalse(
            UserInterface.validate_custom_marker(custom_marker, custom_marker_list)
        )


if __name__ == "__main__":
    unittest.main()