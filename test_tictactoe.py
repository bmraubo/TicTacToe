import unittest
from tictactoe import TicTacToe


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)

    def test_ci_workflow(self):
        self.assertEqual(True, True)


class TestTicTacToe(unittest.TestCase):

    # Initialise and Assign Players
    def test_create_player(self):
        test_board = TicTacToe(3)
        test_players = [["Marx", "human", "X"], ["Engels", "human", "$"]]
        test_board.create_players(test_players)
        self.assertEqual(test_board.players[0].name, "Marx")
        self.assertEqual(test_board.players[0].type, "human")
        self.assertEqual(test_board.players[0].marker, "X")

    def test_player_assignment(self):
        test_board = TicTacToe(3)
        test_players = [["Marx", "human", "X"], ["Engels", "human", "$"]]
        test_board.create_players(test_players)
        test_board.assign_players()
        self.assertEqual(test_board.markers[test_board.players[0]], "X")
        self.assertEqual(test_board.markers[test_board.players[1]], "O")


if __name__ == "__main__":
    unittest.main()
