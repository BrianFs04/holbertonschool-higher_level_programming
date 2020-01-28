#!/usr/bin/python3
''' Unittests cases
'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    ''' Unittests cases
    '''

    def setUp(self):
        ''' Initializer
        '''
        Base._Base__nb_objects = 0

    def testId(self):
        ''' Positive int as arg
        '''
        b = Base(4)
        self.assertEqual(b.id, 4)

    def testNegativeId(self):
        ''' Negative int as arg
        '''
        b = Base(-4)
        self.assertEqual(b.id, -4)

    def testStringId(self):
        ''' String id as arg
        '''
        b = Base('Holberton')
        self.assertEqual(b.id, 'Holberton')

    def testListId(self):
        ''' List as arg
        '''
        b = Base([1, 2])
        self.assertEqual(b.id, [1, 2])

    def testTupleId(self):
        ''' Tuple as arg
        '''
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))

    def testDictionaryId(self):
        ''' Dictionary as arg
        '''
        b = Base({'1': 2})
        self.assertEqual(b.id, {'1': 2})

    def testFloatId(self):
        ''' Float as arg
        '''
        b = Base(4.5)
        self.assertEqual(b.id, 4.5)

    def testZeroId(self):
        ''' Zero as arg
        '''
        b = Base(0)
        self.assertEqual(b.id, 0)

    def testContinuosId(self):
        ''' Different id assign and iteration
        '''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def testContinuosId2(self):
        ''' Same id assign and iteration
        '''
        b1 = Base()
        b2 = Base(1)
        b3 = Base()
        b4 = Base(2)
        self.assertEqual(b3.id, 2)

    def testFalse(self):
        ''' False as arg
        '''
        b = Base(False)
        self.assertEqual(b.id, False)

    def testTrue(self):
        ''' True as arg
        '''
        b = Base(True)
        self.assertEqual(b.id, True)

    def testEmptyList(self):
        ''' Empty List as arg
        '''
        b = Base([])
        self.assertEqual(b.id, [])

    def testEmptyTuple(self):
        ''' Empty tuple as arg
        '''
        b = Base(())
        self.assertEqual(b.id, ())

    def testNone(self):
        ''' None as arg
        '''
        b = Base(None)
        self.assertEqual(b.id, 1)

    def testJsonToString(self):
        ''' Json to string
        '''
        b = Base()
        dicty = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(type(b.to_json_string(dicty)), str)

    def testJsonToStringNone(self):
        ''' Json None to string
        '''
        b = Base()
        self.assertEqual(b.to_json_string(None), "[]")

    def testNan(self):
        b = Base(float('nan'))
        self.assertNotEqual(b.id, float('nan'))

    def testInf(self):
        b = Base(float('inf'))
        self.assertEqual(b.id, float('inf'))

    def testTwoArgs(self):
        ''' Two args passed
        '''
        with self.assertRaises(TypeError):
            b = Base(4, 4)

    def testPrivateArgs(self):
        ''' Access to a private attribute
        '''
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects

    def testCharacter(self):
        ''' Character as arg
        '''
        with self.assertRaises(NameError):
            b = Base(i)



if __name__ == '__main__':
    ''' Main initializer
    '''
    unittest.main()
