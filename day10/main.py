import collections

def main():
    # The adapter has an effective rating of 0 jolts.
    numbers = [0]
    numbers.extend([int(line) for line in read_input('input')])
    distribution = difference_distribution(sorted(numbers))

    # My device input is 3 jolts greater than the rating of
    # the largest adapter.
    distribution[3] += 1

    product = distribution[1] * distribution[3]
    print(f'The product of counts of differences of 1 and 3 is {product}')

def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def difference_distribution(numbers):
    differences = collections.defaultdict(lambda: 0)
    for first, second in zip(numbers, numbers[1:]):
        difference = second - first
        differences[difference] += 1
    return differences

if __name__ == '__main__':
    main()
