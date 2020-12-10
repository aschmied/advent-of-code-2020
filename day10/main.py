import collections

def main():
    # The adapter has an effective rating of 0 jolts.
    numbers = [0]
    numbers.extend(sorted([int(line) for line in read_input('input')]))
    # My device input is 3 jolts greater than the rating of
    # the largest adapter.
    numbers.append(numbers[-1] + 3)

    distribution = difference_distribution(sorted(numbers))
    product = distribution[1] * distribution[3]
    print(f'The product of counts of differences of 1 and 3 is {product}')

    valid_arrangements = count_valid_arrangements(numbers)
    print(f'The number of valid arrangements is {valid_arrangements}')

def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def difference_distribution(numbers):
    differences = collections.defaultdict(lambda: 0)
    for first, second in zip(numbers, numbers[1:]):
        difference = second - first
        differences[difference] += 1
    return differences

def count_valid_arrangements(numbers):
    '''Counts valid arrangements of the monotonic sequence
    `numbers`. A valid arrangement is a subsequence of `numbers`
    where no pair of contiguous elements has a difference
    greater than 3. Left and right endpoints of `number` must be
    included in the subsequence.
    '''
    if len(numbers) < 2:
        raise RuntimeError(f'Need at least 2 numbers but got {len(numbers)}')
    return _count_valid_arrangements(numbers, numbers[0], 1, {})

def _count_valid_arrangements(numbers, previous_number, from_index, memo):
    next_number = numbers[from_index]
    if next_number - previous_number > 3:
        return 0

    if from_index == len(numbers) - 1:
        return 1

    memo_key = (previous_number, from_index)
    if memo_key in memo:
        return memo[memo_key]

    count = (_count_valid_arrangements(numbers, previous_number, from_index + 1, memo) +
        _count_valid_arrangements(numbers, numbers[from_index], from_index + 1, memo))
    memo[memo_key] = count

    return count

if __name__ == '__main__':
    main()
