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

    # Testing Info functions
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

    # Test Players

    # Test assign player to marker

    # Testing Game Board

    # Draw Board
    def test_initialize_board(self):
        expected_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        test_board = Board()
        self.assertEqual(test_board.board, expected_board)
        self.assertEqual(test_board.markers["X"], None)
        self.assertEqual(test_board.markers["O"], None)

    # Create Players
    def test_create_player(self):
        test_board = Board()
        test_board.create_player("Marx")
        self.assertEqual(test_board.players[0].name, "Marx")

    # Assign Players
    def test_player_assignment(self):
        test_board = Board()
        test_player1 = Player("Marx")
        test_player2 = Player("Engels")
        test_board.assign_players(test_player1, test_player2)
        self.assertEqual(test_board.markers["X"], test_player1)
        self.assertEqual(test_board.markers["O"], test_player2)


if __name__ == "__main__":
    unittest.main()
