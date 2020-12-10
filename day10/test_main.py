import unittest

from main import count_valid_arrangements

class TestCountValidArrangements(unittest.TestCase):
    def test_base_case(self):
        self.assertValidArrangements([1, 2], 1)
        self.assertValidArrangements([1, 4], 1)
        self.assertValidArrangements([1, 5], 0)

    def test_three_numbers__exclusion_valid(self):
        self.assertValidArrangements([1, 2, 3], 2)

    def test_three_numbers__exclusion_invalid(self):
        self.assertValidArrangements([1, 3, 5], 1)

    def test_many_numbers(self):
        # This example comes from the problem statement:
        #   https://adventofcode.com/2020/day/10
        
        # The socket jolts.
        numbers = [0]
        numbers.extend(sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]))
        
        # My device's jolts.
        numbers.append(numbers[-1] + 3)
        self.assertValidArrangements(numbers, 8)

    def test_many_many_numbers(self):
        # This example comes from the problem statement:
        #   https://adventofcode.com/2020/day/10

        # The socket jolts.
        numbers = [0]
        numbers.extend(sorted([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]))
        
        # My device's jolts.
        numbers.append(numbers[-1] + 3)
        self.assertValidArrangements(numbers, 19208)

    def assertValidArrangements(self, numbers, expected):
        self.assertEqual(count_valid_arrangements(numbers), expected)
