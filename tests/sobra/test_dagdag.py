import unittest
from sobra.dagdag import Dagdag


class TestDagdag(unittest.TestCase):

    def test_add_two_numbers_int(self):
        d = Dagdag()
        expected = 3
        actual = d.add_two_numbers(1, 2)
        self.assertTrue(expected, actual)

    def test_add_two_numbers_float(self):
        d = Dagdag()
        expected = 6.9
        actual = d.add_two_numbers(2.4, 4.5)
        self.assertTrue(expected, actual)
