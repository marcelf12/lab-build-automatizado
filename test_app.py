# test_app.py

import unittest
from app import soma, subtrai


class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(2.5, 3.5), 6.0)

    def test_subtrai(self):
        self.assertEqual(subtrai(5, 2), 3)
        self.assertEqual(subtrai(1, 1), 0)
        self.assertEqual(subtrai(0, 0), 0)
        self.assertEqual(subtrai(5.0, 2.5), 2.5)


if __name__ == '__main__':
    unittest.main()
