import unittest
from app.tictactoe import TicTacToe


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)


class TestTicTacToe(unittest.TestCase):

    # Initialise and Assign Players
    def test_create_player(self):
        test_players = [["Marx", "human", "X"], ["Engels", "human", "$"]]
        test_board = TicTacToe(3, test_players)
        self.assertEqual(test_board.players[0].name, "Marx")
        self.assertEqual(test_board.players[0].type, "human")
        self.assertEqual(test_board.players[0].marker, "X")

    def test_end_to_end_computer_players(self):
        test_players = [["Marx", "computer", "X"], ["Engels", "computer", "$"]]
        test_board = TicTacToe(3, test_players)
        test_board.play_game()
        self.assertEqual(test_board.board.winner, test_board.players[0])

    def test_initiate_local_game(self):
        size = 3
        test_players = [["Marx", "computer", "X"], ["Engels", "computer", "$"]]
        test_game = TicTacToe(size, test_players)
        self.assertFalse(test_game.server)


if __name__ == "__main__":
    unittest.main()
