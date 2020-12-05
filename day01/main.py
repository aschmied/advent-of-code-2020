def main():
    numbers_set = read_numbers_from_file('input')
    first_number, second_number = find_two_numbers_that_sum_to(numbers_set, 2020)
    print(f'Found {first_number} and {second_number}.')
    print(f'Their product is {first_number * second_number}')

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
    raise ValueError(f'No pair of numbers sum to {target_sum}')

if __name__ == '__main__':
    main()
