import unittest
import sys
from io import StringIO
from tictactoe import TicTacToe, UserInterface


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)

    def test_ci_workflow(self):
        self.assertEqual(True, True)


class TestUserInterface(unittest.TestCase):
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


class TestTicTacToe(unittest.TestCase):
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
