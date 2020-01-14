#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def testPass(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-1, 3, -4, -2]), 3)
        self.assertEqual(max_integer([-1.7, 3.9, -4.9, -2.3]), 3.9)
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer([(1, 4), (7, 8), (-15, 30)]), (7, 8))
        self.assertEqual(max_integer("Hola, mundo"), 'u')

    def testFail(self):
        with self.assertRaises(TypeError):
            max_integer(14)
        with self.assertRaises(TypeError):
            max_integer([1, (2, 3)])
        with self.assertRaises(KeyError):
            max_integer({'first_key': 1, 'second_key': 2})

if __name__ == '__main__':
    unittest.main()
