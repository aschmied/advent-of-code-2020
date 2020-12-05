import math

def main():
    grid = read_grid('input')
    hash_count = count_hashes_on_path(grid, 1, 3)
    print(f'There were {hash_count} hashes on the 1, 3 path.')

    paths_to_try = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    hash_counts = map(lambda path: count_hashes_on_path(grid, path[0], path[1]), paths_to_try)
    hash_count_product  = math.prod(hash_counts)
    print(f'The product of the hash counts on various paths is {hash_count_product}.')


def count_hashes_on_path(grid, row_step, col_step):
    height = len(grid)
    width = len(grid[0])
    row = 0
    col = 0
    hash_count = 0
    while row < height:
        char = grid[row][col]
        if char == '#':
            hash_count += 1
        row += row_step
        col = (col + col_step) % width
    return hash_count

def read_grid(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

if __name__ == '__main__':
    main()
