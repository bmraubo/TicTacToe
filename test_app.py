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

    # Game Board

    # Draw Board
    def test_initialize_board(self):
        expected_board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        test_board = TicTacToe()
        self.assertEqual(test_board.board, expected_board)
        self.assertEqual(test_board.markers, {})
        self.assertEqual(test_board.players, [])

    def test_print_board(self):
        test_board = TicTacToe()
        initial_board = "+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+"
        captured_output = StringIO()
        sys.stdout = captured_output
        test_board.draw_board()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, initial_board)

    # Players
    def test_create_player(self):
        test_board = TicTacToe()
        test_board.create_player("Marx", "human")
        self.assertEqual(test_board.players[0].name, "Marx")
        self.assertEqual(test_board.players[0].type, "human")

    def test_player_assignment(self):
        test_board = TicTacToe()
        test_board.create_player("Marx", "human")
        test_board.create_player("Engels", "human")
        test_board.assign_players()
        self.assertEqual(test_board.markers[test_board.players[0]], "X")
        self.assertEqual(test_board.markers[test_board.players[1]], "O")

    def test_make_move(self):
        test_board = TicTacToe()
        test_board.create_player("Marx", "human")
        test_board.create_player("Engels", "human")
        test_board.assign_players()
        test_input = 1
        test_board.make_move(test_board.players[0], test_input)
        self.assertEqual(test_board.board[0][0], "X")


if __name__ == "__main__":
    unittest.main()
