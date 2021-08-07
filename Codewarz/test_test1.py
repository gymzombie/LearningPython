
import unittest

from test1 import fun


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

    def makesureequals(self):
        self.assertEqual(fun_one(4), 5)


if __name__ == '__main__':
    unittest.main()
