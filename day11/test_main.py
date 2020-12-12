import unittest

from main import GameOfLife

class TestGameOfLife(unittest.TestCase):
    def test_count_occupied__empty(self):
        g = GameOfLife(['.L.'], extinction_threshold=1, neighbour_policy='adjacent')
        self.assertEqual(g.count_occupied(), 0)

    def test_count_occupied__non_empty(self):
        g = GameOfLife(['.#.'], extinction_threshold=1, neighbour_policy='adjacent')
        self.assertEqual(g.count_occupied(), 1)

    def test_step__all_empty(self):
        grid = [
            '.L.',
            'LLL',
            '.L.']
        next_grid = [
            '.#.',
            '###',
            '.#.']
        g = GameOfLife(grid, extinction_threshold=4, neighbour_policy='adjacent')
        self.assertListEqual(g.step(), next_grid)

    def test_step__some_die(self):
        grid = [
            '.#.',
            '###',
            '.#.']
        next_grid = [
            '.#.',
            '#L#',
            '.#.']
        g = GameOfLife(grid, extinction_threshold=4, neighbour_policy='adjacent')
        self.assertListEqual(g.step(), next_grid)

    def test_step__new_life(self):
        grid = [
            'L.#',
            'L.#',
            '#..']
        next_grid = [
            '#.#',
            'L.#',
            '#..']
        g = GameOfLife(grid, extinction_threshold=4, neighbour_policy='adjacent')
        self.assertEqual(g.step(), next_grid)

    def test_step__line_of_sight_policy(self):
        grid = ['L.L.#']
        next_grid = ['#.L.#']
        g = GameOfLife(grid, extinction_threshold=4, neighbour_policy='line-of-sight')
        self.assertEqual(g.step(), next_grid)
