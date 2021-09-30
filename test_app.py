import unittest
import sys
from io import StringIO
from unittest.mock import patch
from tictactoe import *


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)

    def test_ci_workflow(self):
        self.assertEqual(True, True)


class TestIntroMessages(unittest.TestCase):

    # Testing UserInterface functions
    def test_welcome_message(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        UserInterface.welcome_message()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Welcome to Tic Tac Toe")

    def test_game_instructions(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        UserInterface.game_instructions()
        validate_instructions = "Each square on the board have a value from 1-9. Select which square you would like to play by inputting the correct value when promoted."
        output = captured_output.getvalue().strip()
        self.assertEqual(output, validate_instructions)


class TestGameplay(unittest.TestCase):
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

    # Test Move Making
    def test_make_move(self):
        # Set up game
        test_board = TicTacToe()
        test_players = [["Marx", "human"], ["Engels", "human"]]
        test_board.create_players(test_players)
        test_board.assign_players()
        # Test move
        test_input = "1"
        test_board.make_move(test_board.players[0], int(test_input))
        self.assertEqual(test_board.board[0][0], "X")

    def test_validate_player_move(self):
        # If player inputs value that has been used or is outside of range, returns False
        # Set up game
        test_board = TicTacToe()
        test_players = [["Marx", "human"], ["Engels", "human"]]
        test_board.create_players(test_players)
        test_board.assign_players()
        # Test input out of range
        player_move = "10"
        self.assertFalse(test_board.validate_player_move(player_move))
        player_move = "0"
        self.assertFalse(test_board.validate_player_move(player_move))
        player_move = "9"
        self.assertTrue(test_board.validate_player_move(player_move))
        player_move = "1"
        self.assertTrue(test_board.validate_player_move(player_move))
        # Test move already played
        test_input = "1"
        test_board.make_move(test_board.players[0], int(test_input))
        player_move = "1"
        self.assertFalse(test_board.validate_player_move(player_move))
        player_move = "2"
        self.assertTrue(test_board.validate_player_move(player_move))
        # Test for value error exception handling
        player_move = "j"
        self.assertFalse(test_board.validate_player_move(player_move))


class TestWinCheck(unittest.TestCase):
    def test_no_win(self):
        # test win check where no win or draw state exists
        test_board = TicTacToe()
        test_players = [["Marx", "human"], ["Engels", "human"]]
        test_board.create_players(test_players)
        test_board.assign_players()
        self.assertFalse(test_board.win_check(test_board.players[0]))

    def test_win_column(self):
        # testing Win state in column
        # Set up a game
        test_board = TicTacToe()
        test_players = [["Marx", "human"], ["Engels", "human"]]
        test_board.create_players(test_players)
        test_board.assign_players()
        test_board.board[0][1] = "X"
        test_board.board[1][1] = "X"
        test_board.board[2][1] = "X"
        self.assertTrue(test_board.win_check(test_board.players[0]))

    def test_win_row(self):
        # Testing win state in Row
        test_board = TicTacToe()
        test_players = [["Marx", "human"], ["Engels", "human"]]
        test_board.create_players(test_players)
        test_board.assign_players()
        test_board.board[0][0] = "X"
        test_board.board[0][1] = "X"
        test_board.board[0][2] = "X"
        self.assertTrue(test_board.win_check(test_board.players[0]))

    def test_row_diagonal(self):
        # Testing diagonal win states
        test_board = TicTacToe()
        test_players = [["Marx", "human"], ["Engels", "human"]]
        test_board.create_players(test_players)
        test_board.assign_players()
        test_board.board[0][0] = "X"
        test_board.board[1][1] = "X"
        test_board.board[2][2] = "X"
        self.assertTrue(test_board.win_check(test_board.players[0]))


if __name__ == "__main__":
    unittest.main()
