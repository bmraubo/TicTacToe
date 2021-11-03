import unittest
from app.tictactoe import TicTacToe
from app.board import Board
from app.util import Utilities


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)


class TestTicTacToe(unittest.TestCase):

    # Test Local and Server game creation
    def test_initiate_local_game(self):
        size = 3
        test_players = [["Marx", "computer", "X"], ["Engels", "computer", "$"]]
        test_game = TicTacToe(size, test_players)
        self.assertFalse(test_game.server)

    def test_initiate_server_game(self):
        size = 3
        test_players = [["Marx", "computer", "X"], ["Engels", "computer", "$"]]
        test_game = TicTacToe(size, test_players, server=True)
        self.assertTrue(test_game.server)

    # Initialise and Assign Players
    def test_create_player(self):
        test_players = [["Marx", "human", "X"], ["Engels", "human", "$"]]
        test_board = TicTacToe(3, test_players)
        self.assertEqual(test_board.players[0].name, "Marx")
        self.assertEqual(test_board.players[0].type, "human")
        self.assertEqual(test_board.players[0].marker, "X")

    def test_update_computer_player_board_state(self):
        size = 3
        test_players = [["Marx", "computer", "X"], ["Engels", "computer", "$"]]
        test_game = TicTacToe(size, test_players)
        new_board = Board()
        new_board.create_board(size)
        new_board.board_data = Utilities.change_board_value(
            new_board.board_data, "1", "X"
        )
        test_game.board = new_board
        test_game.update_computer_player_boards()
        computer_player_board_data = test_game.players[0].board.board_data
        self.assertEqual(computer_player_board_data, new_board.board_data)

    def test_end_to_end_computer_players(self):
        test_players = [["Marx", "computer", "X"], ["Engels", "computer", "$"]]
        test_board = TicTacToe(3, test_players)
        test_board.play_game()
        self.assertEqual(test_board.board.winner, test_board.players[0].name)


if __name__ == "__main__":
    unittest.main()
