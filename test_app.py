import unittest
import sys
from io import StringIO
from tictactoe import *

class TestDummy(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual(True,True)

    def test_ci_workflow(self):
        self.assertEqual(True, True)

class TestApplication(unittest.TestCase):

    def test_welcome_message(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        Info.welcome_message()
        output = captured_output.getvalue().strip()
        self.assertEqual(output, 'Welcome to Tic Tac Toe')

if __name__ == '__main__':
    unittest.main()