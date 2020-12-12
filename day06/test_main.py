import unittest

from main import intersection_of_chars

class TestIntersectionOfChars(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(intersection_of_chars([]), set())

    def test_one_string(self):
        self.assertEqual(intersection_of_chars(['abc']), set(list('abc')))

    def test_many_strings(self):
        self.assertEqual(intersection_of_chars(['abc', 'ab', 'c']), set())
        self.assertEqual(intersection_of_chars(['abc', 'ab', 'ac']), set('a'))
