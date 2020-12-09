import unittest

from main import LastN
from main import find_contiguous_sum

class TestLastN(unittest.TestCase):
    def test_add(self):
        last_n = LastN(2)
        self.assertEqual(len(last_n), 0)
        
        last_n.add(1)
        last_n.add(1)
        last_n.add(1)
        self.assertEqual(len(last_n), 2)

    def test_count(self):
        last_n = LastN(2)
        self.assertEqual(last_n.count(1), 0)

        last_n.add(1)
        self.assertEqual(last_n.count(1), 1)

        last_n.add(1)
        self.assertEqual(last_n.count(1), 2)

        last_n.add(1)
        self.assertEqual(last_n.count(1), 2)

    def test_in(self):
        last_n = LastN(2)
        self.assertFalse(0 in last_n)

        last_n.add(0)
        self.assertTrue(0 in last_n)

        last_n.add(1)
        self.assertTrue(0 in last_n)

        last_n.add(1)
        self.assertFalse(0 in last_n)

    def test_iteration(self):
        last_n = LastN(3)
        last_n.add(0)
        last_n.add(1)
        for actual, expected in zip(last_n, range(2)):
            self.assertEqual(actual, expected)

class TestFindContiguousSum(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(find_contiguous_sum([], 1), (-1, -1))

    def test_does_not_exist(self):
        self.assertEqual(find_contiguous_sum([2, 3], 1), (-1, -1))

    def test_at_start_of_list(self):
        self.assertEqual(find_contiguous_sum([1, 1, 3], 2), (0, 2))

    def test_in_middle_of_list(self):
        self.assertEqual(find_contiguous_sum([1, 2, 3, 4], 5), (1, 3))

    def test_at_end_of_list(self):
        self.assertEqual(find_contiguous_sum([1, 1, 3], 4), (1, 3))
