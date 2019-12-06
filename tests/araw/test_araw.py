from araw.araw import Araw
import unittest


class TestAraw(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(1, Araw().foo())

    def test_number_of_days_leap(self):
        self.assertEqual(366, Araw().get_number_of_days(2020))
        self.assertEqual(366, Araw().get_number_of_days(2000))
        self.assertEqual(366, Araw().get_number_of_days(2400))

    def test_number_of_days_not_leap(self):
        self.assertEqual(365, Araw().get_number_of_days(1998))
        self.assertEqual(365, Araw().get_number_of_days(1800))
        self.assertEqual(365, Araw().get_number_of_days(1900))
        self.assertEqual(365, Araw().get_number_of_days(2100))
        self.assertEqual(365, Araw().get_number_of_days(2200))
        self.assertEqual(365, Araw().get_number_of_days(2300))
        self.assertEqual(365, Araw().get_number_of_days(2500))



if __name__ == '__main__':
    unittest.main()