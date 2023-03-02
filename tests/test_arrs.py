import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        """тест функции get"""
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], 5, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -2, "test"), "test")

    def test_slice(self):
        """тест функции slice"""
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -6), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3, -2), [2])
