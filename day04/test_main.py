import unittest

from main import is_passport_strictly_valid
from main import iterate_in_chunks

class TestIsPassportStrictlyValid(unittest.TestCase):
    def test_valid(self):
        passport = {
            'pid': '087499704',
            'hgt': '74in',
            'ecl': 'grn',
            'iyr': '2012',
            'eyr': '2030',
            'byr': '1980',
            'hcl': '#623a2f'}
        self.assertTrue(is_passport_strictly_valid(passport))

    def test_valid_2(self):
        passport = {
            'eyr': '2029',
            'ecl': 'blu',
            'cid': '129',
            'byr': '1989',
            'iyr': '2014',
            'pid': '896056539',
            'hcl': '#a97842',
            'hgt': '165cm'}
        self.assertTrue(is_passport_strictly_valid(passport))

    def test_valid_3(self):
        passport = {
            'hcl': '#888785',
            'hgt': '164cm',
            'byr': '2001',
            'iyr': '2015',
            'cid': '88',
            'pid': '545766238',
            'ecl': 'hzl',
            'eyr': '2022'}
        self.assertTrue(is_passport_strictly_valid(passport))

    def test_valid_4(self):
        passport = {
            'iyr': '2010',
            'hgt': '158cm',
            'hcl': '#b6652a',
            'ecl': 'blu',
            'byr': '1944',
            'eyr': '2021',
            'pid': '093154719'}
        self.assertTrue(is_passport_strictly_valid(passport))



class TestIterateInChunks(unittest.TestCase):
    def test_empty(self):
        output = list(iterate_in_chunks([]))
        self.assertEqual(output, [[]])

    def test_single_value(self):
        output = list(iterate_in_chunks(['blah']))
        self.assertEqual(output, [['blah']])

    def test_single_delimiter(self):
        output = list(iterate_in_chunks(['\n']))
        self.assertEqual(output, [[], []])

    def test_multiple_values(self):
        output = list(iterate_in_chunks(['blah', 'blerg', '\n', 'foo']))
        self.assertEqual(output, [['blah', 'blerg'], ['foo']])