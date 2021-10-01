import unittest
import sys
from io import StringIO
from tictactoe import TicTacToe


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)

    def test_ci_workflow(self):
        self.assertEqual(True, True)


class TestTicTacToe(unittest.TestCase):
    # Testing welcome message and game instructions
    def test_welcome_message(self):
        test_game = TicTacToe()
        # Tests display of welcome message
        captured_output = StringIO()
        sys.stdout = captured_output
        test_game.welcome_message()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Welcome to Tic Tac Toe")

    def test_game_instructions(self):
        test_game = TicTacToe()
        # Tests Display of Game Instructions
        captured_output = StringIO()
        sys.stdout = captured_output
        test_game.game_instructions()
        validate_instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        output = captured_output.getvalue().strip()
        self.assertEqual(output, validate_instructions)

    # Initialise and Assign Players
    def test_create_player(self):
        test_board = TicTacToe()
        test_players = [["Marx", "human"], ["Engels", "human"]]
        test_board.create_players(test_players)
        self.assertEqual(test_board.players[0].name, "Marx")
        self.assertEqual(test_board.players[0].type, "human")

    def test_player_assignment(self):
        test_board = TicTacToe()
        test_players = [["Marx", "human"], ["Engels", "human"]]
        test_board.create_players(test_players)
        test_board.assign_players()
        self.assertEqual(test_board.markers[test_board.players[0]], "X")
        self.assertEqual(test_board.markers[test_board.players[1]], "O")


if __name__ == "__main__":
    unittest.main()
