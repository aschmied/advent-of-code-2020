import copy

def main():
    pass

class GameOfLife:
    _INACCESSIBLE = '.'
    _EMPTY = 'L'
    _OCCUPIED = '#'

    def __init__(self, terrain_grid, extinction_threshold):
        self._current_grid = terrain_grid
        self._extinction_threshold = extinction_threshold
        self._rows = len(terrain_grid)
        self._cols = len(terrain_grid[0])
        self._steps = 0

    def count_occupied(self):
        return sum([row.count(self._OCCUPIED) for row in self._current_grid])

    def step_until_stable(self):
        stable = False
        while not stable:
            next_grid = self.step()
            if next_grid == self._current_grid:
                return
            self._current_grid = next_grid
            self._steps += 1
            if self._steps > 1e6:
                raise RuntimeError(f'Reached {self._steps} steps')

    def step(self):
        current_grid = self._current_grid
        rows = self._rows
        cols = self._cols
        next_grid = [[None] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                next_grid[row][col] = self._next_state_for_cell(row, col)
        return [''.join(row) for row in next_grid]

    def _next_state_for_cell(self, row, col):
        current_grid = self._current_grid
        if current_grid[row][col] == self._INACCESSIBLE:
            return self._INACCESSIBLE
        occupied_neighbours = self._count_occupied_neighbours(current_grid, row, col)
        if occupied_neighbours >= self._extinction_threshold:
            return self._EMPTY
        return self._OCCUPIED

    def _count_occupied_neighbours(self, current_grid, row, col):
        row_offsets = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_offsets = [-1, 0, 1, -1, 1, -1, 0, 1]
        neighbours_count = 0
        for ro, co in zip(row_offsets, col_offsets):
            r = row + ro
            c = col + co
            if r < 0 or c < 0 or r >= self._rows or c >= self._cols:
                continue
            if current_grid[r][c] == self._OCCUPIED:
                neighbours_count += 1
        return neighbours_count

if __name__ == '__main__':
    main()
