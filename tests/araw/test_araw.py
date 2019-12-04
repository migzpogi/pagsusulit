from araw.araw import Araw
import unittest

class TestAraw(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(1, Araw().foo())

    def test_number_of_days_leap(self):
        self.assertEqual(366, Araw().get_number_of_days(2020))

    def test_number_of_days_not_leap(self):
        self.assertEqual(365, Araw().get_number_of_days(1998))

if __name__ == '__main__':
    unittest.main()