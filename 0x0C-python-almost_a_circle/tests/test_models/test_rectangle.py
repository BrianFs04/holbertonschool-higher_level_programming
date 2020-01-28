#!/usr/bin/python3
''' Unittests cases
'''
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    ''' Unittests cases
    '''
    def setUp(self):
        Base._Base__nb_objects = 0

    def testWidthAndHeight(self):
        ''' Width and Height attrs
        '''
        r = Rectangle(5, 6)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)

    def testXAndY(self):
        ''' X and Y attrs
        '''
        r = Rectangle(5, 6, 7, 8)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)

    def testId(self):
        ''' Id attr
        '''
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def testZeroId(self):
        ''' Id attr is 0
        '''
        r = Rectangle(5, 6, id=0)
        self.assertEqual(r.id, 0)

    def testWidthTypeStr(self):
        ''' Type error for width
        '''
        with self.assertRaises(TypeError):
            r = Rectangle('10', 9)

    def testHeightTypeStr(self):
        ''' Type error for height
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(9, '10')

    def testWidthValue(self):
        ''' Value error for width
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 9)

    def testHeightValue(self):
        ''' Value error for height
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(9, -2)

    def testXValue(self):
        ''' Value error for x
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(7, 6, -9, 9)

    def testYValue(self):
        ''' Value error for y
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(7, 6, 9, -9)

    def testWidthList(self):
        ''' Type list in width attr
        '''
        with self.assertRaises(TypeError):
            r = Rectangle([9], 2)

    def testHeightList(self):
        ''' Type list in height attr
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(2, [9])

    def testWidthZero(self):
        ''' Zero in width
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def testHeightZero(self):
        ''' Zero in height
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(2, 0)

    def testWidthFloat(self):
        ''' Float in width
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(0.5, 9)

    def testHeightFloat(self):
        ''' Float in height
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(9, 0.5)

    def testXTypeStr(self):
        ''' Type error for x
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(9, 8, '7', 6)

    def testYTypeStr(self):
        ''' Type error for y
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(9, 8, 7, '6')

    def testXList(self):
        ''' List in x
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(9, 8, [7], 6)

    def testYList(self):
        ''' List in y
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(9, 8, 7, [6])

    def testXNegative(self):
        ''' Negative value in x
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(9, 8, -7, 6)

    def testYNegative(self):
        ''' Negative value in y
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(9, 8, 7, -6)

    def testXNothing(self):
        ''' Nothing in x
        '''
        r = Rectangle(9, 2)
        self.assertEqual(r.x, 0)

    def testYNothing(self):
        ''' Nothing in y
        '''
        r = Rectangle(9, 2)
        self.assertEqual(r.y, 0)

    def testInherit(self):
        ''' Inheritance
        '''
        self.assertEqual(issubclass(Rectangle, Base), True)

    def testArea(self):
        ''' Area of rectangle
        '''
        r = Rectangle(7, 6)
        self.assertEqual(r.area(), 42)

    def testStrMethod(self):
        ''' Prints __str__
        '''
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')

    def testStrMethodFewArgs(self):
        ''' __str__ few arguments
        '''
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), '[Rectangle] (1) 1/0 - 5/5')

    def testUpdateArgs(self):
        ''' Update all arguments
        '''
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def testUpdateKwargs(self):
        ''' Update all arguments
        '''
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)

    def testUpdateKwargs(self):
        ''' Update only id
        '''
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def testTypeDict(self):
        ''' Type Dict
        '''
        r = Rectangle(5, 10)
        self.assertEqual(type(r.to_dictionary()), dict)

    def testDict(self):
        ''' To dictionary
        '''
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.to_dictionary(), {'width': 10, 'height': 10,
                                             'x': 10, 'y': 10, 'id': 10})

if __name__ == '__main__':
    unittest.main()
