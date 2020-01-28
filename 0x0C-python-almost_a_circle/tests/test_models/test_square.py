#!/usr/bin/python3
''' Unittests cases
'''
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    ''' Unittests cases
    '''
    def setUp(self):
        Base._Base__nb_objects = 0

    def testStrMethod(self):
        ''' Print str method
        '''
        s = Square(5)
        self.assertEqual(str(s), '[Square] (1) 0/0 - 5')

    def testArea(self):
        ''' Area of square
        '''
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def testSize(self):
        ''' Size of square
        '''
        s = Square(8)
        self.assertEqual(s.size, 8)

    def testWidth(self):
        ''' Width of square
        '''
        s = Square(4)
        self.assertEqual(s.width, 4)

    def testHeight(self):
        ''' Height of square
        '''
        s = Square(4)
        self.assertEqual(s.height, 4)

    def testZeroSize(self):
        ''' Size as zero
        '''
        with self.assertRaises(ValueError):
            s = Square(0)

    def testEmptyFunc(self):
        ''' Empty function
        '''
        with self.assertRaises(TypeError):
            s = Square()

    def testXTwoAttrs(self):
        ''' Test X with two attributes
        '''
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def testXThreeAttrs(self):
        ''' Test X with three attributes
        '''
        s = Square(7, 9, 9)
        self.assertEqual(s.x, 9)

    def testXFourAttrs(self):
        ''' Test X with four attributes
        '''
        s = Square(3, 5, 3, 5)
        self.assertEqual(s.x, 5)

    def testYTwoAttrs(self):
        ''' Test Y with two attributes
        '''
        s = Square(7, 9)
        self.assertEqual(s.y, 0)

    def testYThreeAttrs(self):
        ''' Test Y with three attributes
        '''
        s = Square(7, 9, 3)
        self.assertEqual(s.y, 3)

    def testYFourAttrs(self):
        ''' Test Y with four attributes
        '''
        s = Square(3, 5, 3, 5)
        self.assertEqual(s.y, 3)

    def testId(self):
        ''' Test id
        '''
        s = Square(1, 2)
        s1 = Square(3, 4)
        s2 = Square(5, 6)
        s3 = Square(100, 100, 100, 100)
        self.assertEqual(s.id, 1)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s2.id, 3)
        self.assertEqual(s3.id, 100)

    def testArgs(self):
        ''' All arguments passed
        '''
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def testAllZero(self):
        ''' All argument in zero
        '''
        with self.assertRaises(ValueError):
            s = Square(0, 0, 0, 0)

    def testUpdate(self):
        ''' Updating values
        '''
        s = Square(1, 2, 3, 4)
        s.update(5, 6, 7, 8)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)

    def testString(self):
        ''' String passed
        '''
        with self.assertRaises(TypeError):
            s = Square('Holberton')

    def testList(self):
        ''' List passed
        '''
        with self.assertRaises(TypeError):
            s = Square([7, 7, 7])

    def testDict(self):
        ''' Dictionary passed
        '''
        with self.assertRaises(TypeError):
            s = Square({'a': 1, 'b': 2})

    def testTuple(self):
        ''' Tuple passed
        '''
        with self.assertRaises(TypeError):
            s = Square((1, ))
