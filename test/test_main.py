import unittest


class TestGeneral(unittest.TestCase):
    def test_example_function(self):
        two = 2
        one = 1
        two_plus_one = two + one
        self.assertEqual(two_plus_one, 3, f'{two_plus_one} was not equal to 3.')