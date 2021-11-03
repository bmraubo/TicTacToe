import unittest
import sys
from io import StringIO
from app.ui import UserInterface
from app.player import HumanPlayer


class TestUserInterface(unittest.TestCase):

    # Testing Game Info messages
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

    def test_declare_error(self):
        invalid_move = (False, "Value Error: g is not between 1-9")
        expected_message = "Value Error: g is not between 1-9"
        self.assertEqual(UserInterface.declare_error(invalid_move[1]), expected_message)

    def test_declare_winner(self):
        winner = HumanPlayer(["Marx", "human", "X"])
        expected_declaration = f"{winner.name} has won the game\N{Party Popper}"
        self.assertEqual(
            UserInterface.declare_winner(winner.name), expected_declaration
        )
        winner = "Draw!"
        expected_declaration = "It's a Draw!"
        self.assertEqual(UserInterface.declare_winner(winner), expected_declaration)

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
