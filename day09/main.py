import collections

def main():
    numbers = read_numbers('input')
    first_invalid_number = find_first_invalid_number(numbers, 25)
    print(f'The first invalid number is {first_invalid_number}')

    start, end = find_contiguous_sum(numbers, first_invalid_number)
    min_in_range = min(numbers[start:end])
    max_in_range = max(numbers[start:end])
    print(f'The sum of the smallest and largest numbers in the range is {min_in_range + max_in_range}')

def read_numbers(filename):
    with open(filename) as f:
        return [int(line.strip()) for line in f]

def find_first_invalid_number(numbers, preamble_length):
    last_n = LastN(preamble_length)
    for number in numbers[0:preamble_length]:
        last_n.add(number)

    for number in numbers[preamble_length:]:
        number1, number2 = find_two_numbers_that_sum_to(last_n, number)
        if number1 is None:
            return number
        last_n.add(number)

    raise RuntimeError('No invalid number found')

def find_contiguous_sum(numbers, target_sum):
    if len(numbers) == 0:
        return -1, -1

    start = 0
    end = 0
    current_sum = 0
    while start < len(numbers) and end < len(numbers):
        while current_sum < target_sum:
            current_sum += numbers[end]
            end += 1
        if current_sum == target_sum:
            return start, end

        while current_sum > target_sum:
            current_sum -= numbers[start]
            start += 1
        if current_sum == target_sum:
            return start, end

    return -1, -1

def find_two_numbers_that_sum_to(last_n, target_sum):
    for number in last_n:
        target_number = target_sum - number
        if target_number not in last_n:
            continue
        if target_number != number:
            return number, target_number
        if last_n.count(target_number) > 1:
            return target_number, target_number
    return None, None

class LastN:
    def __init__(self, max_size):
        self._max_size = max_size
        self._queue = collections.deque()
        self._counts = collections.defaultdict(lambda: 0)

    def add(self, obj):
        self._append_to_queue(obj)
        self._add_to_counts(obj)
        if len(self._queue) > self._max_size:
            removed = self._pop_from_queue(obj)
            self._subtract_from_counts(removed)

    def _append_to_queue(self, obj):
        self._queue.append(obj)

    def _add_to_counts(self, obj):
        self._counts[obj] += 1

    def _pop_from_queue(self, obj):
        return self._queue.popleft()

    def _subtract_from_counts(self, obj):
        self._counts[obj] -= 1
        if self._counts[obj] == 0:
            del(self._counts[obj])

    def count(self, obj):
        return self._counts[obj]

    def __len__(self):
        return len(self._queue)

    def __contains__(self, obj):
        return obj in self._counts.keys()

    def __iter__(self):
        return self._queue.__iter__()

if __name__ == '__main__':
    main()
