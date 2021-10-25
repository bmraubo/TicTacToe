import unittest
from app.gameprocess import GameProcess
from app.board import Board
from app.player import HumanPlayer
from app.gamelogic import GameLogic


class TestGameProcess(unittest.TestCase):
    def test_package_move(self):
        size = 3
        test_board = Board.generate_board(size)
        test_player_info = ["Marx", "human", "X"]
        test_player = HumanPlayer(test_player_info)
        moves_made = 0
        player_move = "1"
        expected_dict = {
            "player": {
                "name": test_player.name,
                "marker": test_player.marker,
            },
            "board": {
                "state": test_board,
                "size": size,
            },
            "move": {"move": player_move, "move_number": moves_made},
        }
        self.assertEqual(
            GameProcess.package_move(
                test_board, size, test_player, player_move, moves_made
            ),
            expected_dict,
        )

    def test_process_move_valid_move(self):
        # Set Up
        size = 3
        test_board = Board.generate_board(size)
        test_player_info = ["Marx", "human", "X"]
        test_player = HumanPlayer(test_player_info)
        moves_made = 0
        player_move = "1"
        move_information = GameProcess.package_move(
            test_board, size, test_player, player_move, moves_made
        )
        move_outcome = GameProcess.process_move(move_information)
        # Expected Results
        updated_board = GameLogic.change_board_value(
            move_information["board"]["state"],
            player_move,
            move_information["player"]["marker"],
        )
        expected_result = {
            "move_success": True,
            "move_info": {
                "game_over": False,
                "game_status": {"game_state": "In Progress", "winner": None},
                "board": updated_board,
                "move_number": 1,
            },
        }
        # Validation
        self.assertEqual(move_outcome, expected_result)

    def test_process_move_invalid_move(self):
        # Set Up
        size = 3
        test_board = Board.generate_board(size)
        test_player_info = ["Marx", "human", "X"]
        test_player = HumanPlayer(test_player_info)
        moves_made = 0
        player_move = "j"
        move_information = GameProcess.package_move(
            test_board, size, test_player, player_move, moves_made
        )
        move_outcome = GameProcess.process_move(move_information)
        # Expected Result
        expected_result = {
            "move_success": False,
            "move_info": {
                "Error": "Invalid Move",
                "Reason": f"Value Error: {player_move} is not between 1-{size*size}",
            },
        }
        # Validation
        self.assertEqual(move_outcome, expected_result)


if __name__ == "__main__":
    unittest.main()
