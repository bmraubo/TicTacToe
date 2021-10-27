import unittest
from app.tictactoe import TicTacToe


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)

    def test_ci_workflow(self):
        self.assertEqual(True, True)


class TestTicTacToe(unittest.TestCase):

    # Initialise and Assign Players
    def test_create_player(self):
        test_players = [["Marx", "human", "X"], ["Engels", "human", "$"]]
        test_board = TicTacToe(3, test_players)
        test_board.set_up_players(test_players)
        self.assertEqual(test_board.players[0].name, "Marx")
        self.assertEqual(test_board.players[0].type, "human")
        self.assertEqual(test_board.players[0].marker, "X")

    def test_player_assignment(self):
        test_players = [["Marx", "human", "X"], ["Engels", "human", "$"]]
        test_board = TicTacToe(3, test_players)
        self.assertEqual(test_board.markers[test_board.players[0]], "X")
        self.assertEqual(test_board.markers[test_board.players[1]], "$")

    def test_end_to_end_computer_players(self):
        test_players = [["Marx", "computer", "X"], ["Engels", "computer", "$"]]
        test_board = TicTacToe(3, test_players)
        test_board.play_game()
        self.assertEqual(test_board.board.winner, test_board.players[0])

    def test_declare_invalid_move_reason(self):
        invalid_move = (False, "Value Error: g is not between 1-9")
        expected_message = "Value Error: g is not between 1-9"
        self.assertEqual(
            TicTacToe.declare_invalid_move_reason(invalid_move), expected_message
        )


if __name__ == "__main__":
    unittest.main()
