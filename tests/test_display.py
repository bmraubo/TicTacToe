import unittest
import sys
from io import StringIO
from app.board import Board
from app.display import Display


class TestDisplay(unittest.TestCase):
    def test_draw_board_3x3(self):
        test_board = Board()
        test_board.generate_board(3)
        initial_board = "+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+"
        captured_output = StringIO()
        sys.stdout = captured_output
        Display.draw_board(test_board, 3)
        output = captured_output.getvalue().strip()
        self.assertEqual(output, initial_board)

    def test_draw_board_4x4(self):
        test_board = Board()
        test_board.generate_board(4)
        initial_board = "+----+----+----+----+\n|  1 |  2 |  3 |  4 |\n+----+----+----+----+\n|  5 |  6 |  7 |  8 |\n+----+----+----+----+\n|  9 | 10 | 11 | 12 |\n+----+----+----+----+\n| 13 | 14 | 15 | 16 |\n+----+----+----+----+"
        captured_output = StringIO()
        sys.stdout = captured_output
        Display.draw_board(test_board, 4)
        output = captured_output.getvalue().strip()
        self.assertEqual(output, initial_board)


if __name__ == "__main__":
    unittest.main()
