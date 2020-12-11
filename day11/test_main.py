import unittest

from main import GameOfLife

class TestGameOfLife(unittest.TestCase):
    def test_all_empty(self):
        grid = [
            '.L.',
            'LLL',
            '.L.']
        next_grid = [
            '.#.',
            '###',
            '.#.']
        g = GameOfLife(grid, extinction_threshold=4)
        self.assertListEqual(g.step(), next_grid)

    def test_some_die(self):
        grid = [
            '.#.',
            '###',
            '.#.']
        next_grid = [
            '.#.',
            '#L#',
            '.#.']
        g = GameOfLife(grid, extinction_threshold=4)
        self.assertListEqual(g.step(), next_grid)

    def test_count_occupied__empty(self):
        g = GameOfLife(['.L.'], extinction_threshold=1)
        self.assertEqual(g.count_occupied(), 0)

    def test_count_occupied__non_empty(self):
        g = GameOfLife(['.#.'], extinction_threshold=1)
        self.assertEqual(g.count_occupied(), 1)
