import unittest
from app.board import Board
from app.player import HumanPlayer


class TestBoard(unittest.TestCase):
    def test_generate_board_3x3(self):
        expected_board = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }
        test_board = Board()
        test_board.create_board(3)
        self.assertEqual(test_board.board, expected_board)

    def test_generate_board_4x4(self):
        expected_board = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "10": "10",
            "11": "11",
            "12": "12",
            "13": "13",
            "14": "14",
            "15": "15",
            "16": "16",
        }
        test_board = Board()
        test_board.create_board(4)
        self.assertEqual(test_board.board, expected_board)

    def test_check_board_value(self):
        test_board = Board()
        test_board.create_board(3)
        value = "4"
        self.assertEqual(Board.check_board_value(test_board.board, value), "4")

    def test_change_board_value(self):
        # Set up game
        test_board = Board()
        test_board.create_board(3)
        # Test move
        test_input = "1"
        marker = "X"
        Board.change_board_value(test_board.board, test_input, marker)
        self.assertEqual(Board.check_board_value(test_board.board, test_input), "X")

    def test_validate_move_valueerror(self):
        # Test for value error exception handling
        test_board = Board()
        test_board.create_board(3)
        player_move = "j"
        self.assertFalse(test_board.validate_move(player_move))

    def test_validate_move_out_of_range(self):
        # Rejects moves that are outside of permitted range
        test_board = Board()
        test_board.create_board(3)
        player_move = "10"
        self.assertFalse(test_board.validate_move(player_move))
        # Tests inputs within range, for completeness => should be allowed
        player_move = "9"
        self.assertTrue(test_board.validate_move(player_move))

    def test_validate_move_already_played(self):
        # Rejects move if it has already been played
        test_board = Board()
        test_board.create_board(3)
        test_input = "1"
        test_marker = "X"
        Board.change_board_value(test_board.board, test_input, test_marker)
        # 1 has already been played, so playing it again should return False
        player_move = "1"
        self.assertFalse(test_board.validate_move(player_move))
        # 2 has not been played - it should pass validation and return True
        player_move = "2"
        self.assertTrue(test_board.validate_move(player_move))

    # Testing win check
    def test_win_arrangement_generator_3x3(self):
        test_board = Board()
        test_board.create_board(3)
        expected_rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        expected_columns = [["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"]]
        expected_diagonals = [["1", "5", "9"], ["3", "5", "7"]]
        self.assertEqual(test_board.arrangements["rows"], expected_rows)
        self.assertEqual(test_board.arrangements["columns"], expected_columns)
        self.assertEqual(test_board.arrangements["diagonals"], expected_diagonals)

    def test_win_arrangement_generator_4x4(self):
        test_board = Board()
        test_board.create_board(4)
        expected_rows = [
            ["1", "2", "3", "4"],
            ["5", "6", "7", "8"],
            ["9", "10", "11", "12"],
            ["13", "14", "15", "16"],
        ]
        expected_columns = [
            ["1", "5", "9", "13"],
            ["2", "6", "10", "14"],
            ["3", "7", "11", "15"],
            ["4", "8", "12", "16"],
        ]
        expected_diagonals = [["1", "6", "11", "16"], ["4", "7", "10", "13"]]
        self.assertEqual(test_board.arrangements["rows"], expected_rows)
        self.assertEqual(test_board.arrangements["columns"], expected_columns)
        self.assertEqual(test_board.arrangements["diagonals"], expected_diagonals)

    def test_no_win_3x3(self):
        # test win check where no win or draw state exists
        test_board = Board()
        test_board.create_board(3)
        test_marker = "X"
        self.assertFalse(test_board.win_check(test_marker))

    def test_no_win_4x4(self):
        # test win check where no win or draw state exists
        test_board = Board()
        test_board.create_board(4)
        test_marker = "X"
        self.assertFalse(test_board.win_check(test_marker))

    def test_wins_3x3(self):
        # testing Win state in column
        # Set up a game
        winning_arrangements = [["1", "4", "7"], ["1", "2", "3"], ["1", "5", "9"]]
        for arrangement in winning_arrangements:
            test_board = Board()
            test_board.create_board(3)
            test_marker = "X"
            for value in arrangement:
                Board.change_board_value(test_board.board, value, test_marker)
            self.assertTrue(test_board.win_check(test_marker))

    def test_wins_4x4(self):
        # testing Win state in column
        # Set up a game
        winning_arrangements = [
            ["1", "5", "9", "13"],
            ["1", "2", "3", "4"],
            ["1", "6", "11", "16"],
        ]
        for arrangement in winning_arrangements:
            test_board = Board()
            test_board.create_board(4)
            test_marker = "X"
            for value in arrangement:
                Board.change_board_value(test_board.board, value, test_marker)
            self.assertTrue(test_board.win_check(test_marker))

    def test_make_move(self):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        test_move = "1"
        test_board = test_board.make_move(test_player, test_move)
        self.assertEqual(
            Board.check_board_value(test_board.board, test_move), test_player.marker
        )

    def test_winning_move(self):
        test_board = Board()
        test_board.create_board(3)
        test_player = HumanPlayer(["Marx", "human", "X"])
        winning_arrangement = ["1", "4", "7"]
        for value in winning_arrangement:
            test_board = test_board.make_move(test_player, value)
        self.assertEqual(test_board.winner, test_player)

    def test_declare_winner(self):
        winner = HumanPlayer(["Marx", "human", "X"])
        expected_declaration = f"{winner.name} has won the game\N{Party Popper}"
        self.assertEqual(Board.declare_winner(winner), expected_declaration)


if __name__ == "__main__":
    unittest.main()
