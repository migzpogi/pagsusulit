import unittest
from sobra.dagdag import Dagdag


class TestDagdag(unittest.TestCase):

    def test_add_two_integers(self):
        d = Dagdag()
        expected = 3
        actual = d.add_two_integers(1, 2)
        self.assertTrue(expected, actual)
