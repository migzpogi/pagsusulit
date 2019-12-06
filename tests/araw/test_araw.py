from araw.araw import Araw
import unittest


class TestAraw(unittest.TestCase):

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

    def test_days_to_year_ratio(self):
        self.assertEqual(0.27, Araw().days_to_year_ratio(1, 2019))
        self.assertEqual(0.27, Araw().days_to_year_ratio(1, 2020))

    def test_accuracy(self):
        self.assertEqual(99.73, Araw().accuracy(1, 2019))
        self.assertEqual(99.73, Araw().accuracy(1, 2020))

    def test_once(self):
        self.assertEqual(99.73, Araw().accuracy(1, 2019))
        self.assertEqual(99.73, Araw().accuracy(1, 2020))


if __name__ == '__main__':
    unittest.main()