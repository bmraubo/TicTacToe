import unittest

class TestDummy(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual(True,True)

    def test_ci_workflow(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()