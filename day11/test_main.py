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
        game_of_life = GameOfLife(grid, extinction_threshold=4)
        self.assertListEqual(game_of_life.step(), next_grid)

    def test_some_die(self):
        grid = [
            '.#.',
            '###',
            '.#.']
        next_grid = [
            '.#.',
            '#L#',
            '.#.']
        game_of_life = GameOfLife(grid, extinction_threshold=4)
        self.assertListEqual(game_of_life.step(), next_grid)
