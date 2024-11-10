import unittest
from calc import add

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 3), 6)
        self.assertEqual(add(-1, -3), -4)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 2), 1)

if __name__== '__main__':
    unittest.main()
