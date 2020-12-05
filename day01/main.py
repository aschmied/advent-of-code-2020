import itertools

def main():
    numbers_set = read_numbers_from_file('input')
    first_number, second_number = find_two_numbers_that_sum_to(numbers_set, 2020)
    print(f'Found {first_number} and {second_number}.')
    print(f'Their product is {first_number * second_number}')
    first_number, second_number, third_number = find_three_numbers_that_sum_to(numbers_set, 2020)
    print(f'Found {first_number}, {second_number}, and {third_number}.')
    print(f'Their product is {first_number * second_number * third_number}')

def read_numbers_from_file(filename):
    numbers = set()
    with open(filename) as f:
        for line in f:
            number = int(line.strip())
            numbers.add(number)
    return numbers

def find_two_numbers_that_sum_to(numbers_set, target_sum):
    for number in numbers_set:
        target_number = target_sum - number
        if target_number in numbers_set:
            return number, target_number
    raise ValueError(f'No pair of numbers sums to {target_sum}')

def find_three_numbers_that_sum_to(numbers_set, target_sum):
    pairwise_sums = {}
    for first, second in itertools.combinations(numbers_set, 2):
        pairwise_sum = first + second
        pairwise_sums[pairwise_sum] = (first, second)
    for number in numbers_set:
        target_pairwise_sum = target_sum - number
        if target_pairwise_sum in pairwise_sums.keys():
            first, second = pairwise_sums[target_pairwise_sum]
            return first, second, number
    raise ValueError(f'No triple of numbers sums to {target_sum}')

if __name__ == '__main__':
    main()
