import unittest
from dummy_package import foo

class TestFoo(unittest.TestCase):

    def test_foo(self):
        self.assertTrue(foo.bar())

if __name__ == '__main__':
    unittest.main()