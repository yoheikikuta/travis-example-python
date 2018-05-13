# coding:utf-8

import unittest
from src.sayhello import SayHello


class SayHelloTest(unittest.TestCase):

    def setUp(self):
        print('Setting up...')
        self.sayhello = SayHello()

    def test_first(self):
        print('test_first')

    def test_sayhello(self):
        expected = "Hello"
        actual = self.sayhello.sayhello()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
