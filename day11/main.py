import copy

def main():
    grid = read_grid('input')

    g = GameOfLife(grid, extinction_threshold=4, neighbour_policy='adjacent')
    g.step_until_stable()
    print(f'The number of occupied seats at stable state is {g.count_occupied()} with adjacent neighbour policy')

    g =GameOfLife(grid, extinction_threshold=5, neighbour_policy='line-of-sight')
    g.step_until_stable()
    print(f'The number of occupied seats at stable state is {g.count_occupied()} with line-of-sight neighbour policy')

def read_grid(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

class GameOfLife:
    _INACCESSIBLE = '.'
    _EMPTY = 'L'
    _OCCUPIED = '#'

    def __init__(self, terrain_grid, extinction_threshold, neighbour_policy):
        self._current_grid = terrain_grid
        self._extinction_threshold = extinction_threshold
        self._count_occupied_neighbours = self._get_count_occupied_neighbours(neighbour_policy)
        self._rows = len(terrain_grid)
        self._cols = len(terrain_grid[0])
        self._steps = 0

    def count_occupied(self):
        return sum([row.count(self._OCCUPIED) for row in self._current_grid])

    def step_until_stable(self):
        while True:
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
        current_state = current_grid[row][col]
        if current_state == self._INACCESSIBLE:
            return self._INACCESSIBLE

        occupied_neighbours = self._count_occupied_neighbours(current_grid, row, col)
        if occupied_neighbours == 0:
            return self._OCCUPIED
        if occupied_neighbours >= self._extinction_threshold:
            return self._EMPTY

        return current_state

    def _get_count_occupied_neighbours(self, neighbour_policy):
        if neighbour_policy == 'adjacent':
            return self._count_occupied_immediate_neighbours
        elif neighbour_policy == 'line-of-sight':
            return self._count_occupied_line_of_sight_neighbours
        else:
            raise ValueError(f'Invalid neighbour_policy: {neighbour_policy}')

    def _count_occupied_immediate_neighbours(self, current_grid, row, col):
        row_offsets = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_offsets = [-1, 0, 1, -1, 1, -1, 0, 1]
        neighbours_count = 0
        for ro, co in zip(row_offsets, col_offsets):
            r = row + ro
            c = col + co
            if not self._offset_in_bounds(r, c):
                continue
            if current_grid[r][c] == self._OCCUPIED:
                neighbours_count += 1
        return neighbours_count

    def _count_occupied_line_of_sight_neighbours(self, current_grid, row, col):
        row_offsets = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_offsets = [-1, 0, 1, -1, 1, -1, 0, 1]

        neighbours_count = 0
        for ro, co in zip(row_offsets, col_offsets):
            r = row + ro
            c = col + co
            while self._offset_in_bounds(r, c) and current_grid[r][c] == self._INACCESSIBLE:
                r = r + ro
                c = c + co

            if not self._offset_in_bounds(r, c):
                continue

            if current_grid[r][c] == self._OCCUPIED:
                neighbours_count += 1

        return neighbours_count

    def _offset_in_bounds(self, row, col):
        return row >= 0 and col >= 0 and row < self._rows and col < self._cols

if __name__ == '__main__':
    main()
