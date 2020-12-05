def main():
    with open('input') as f:
        process_lines(f)

def process_lines(iterable):
    occupied_seat_ids = []
    available_seat_ids = set(range(0, 128 * 8))
    for line in iterable:
        seat_sequence = line.strip()
        row, col = decode_seat_sequence(seat_sequence)
        seat_id = calculate_sead_id(row, col)
        occupied_seat_ids.append(seat_id)
        available_seat_ids.remove(seat_id)
    largest_occupied_seat_id = max(sorted(occupied_seat_ids))
    print(f'Largest occupied seat ID is {largest_occupied_seat_id}')

    available_seats_not_at_front_or_back = exclude_front_and_back(available_seat_ids)
    available_seats_adjacent_to_occupied = [s for s in available_seats_not_at_front_or_back if s - 1 in occupied_seat_ids and s + 1 in occupied_seat_ids]
    print(f'Your seat is {available_seats_adjacent_to_occupied[0]}')

def decode_seat_sequence(seat_sequence):
    split_index = max([seat_sequence.rindex('B'), seat_sequence.rindex('F')]) + 1
    front_back_sequence = seat_sequence[0:split_index].replace('F', 'l').replace('B', 'u')
    left_right_sequence = seat_sequence[split_index:].replace('L', 'l').replace('R', 'u')
    row = decode_binary_sequence(0, 128, front_back_sequence)
    col = decode_binary_sequence(0, 8, left_right_sequence)
    return row, col

def decode_binary_sequence(lo, hi, sequence):
    # Target is always in [min, max)
    for char in sequence:
        mid = (lo + hi) // 2
        if char == 'l':
            hi = mid
        elif char == 'u':
            lo = mid
    return lo

def calculate_sead_id(row, col):
    return 8 * row + col

def exclude_front_and_back(seat_ids):
    return [seat_id for seat_id in seat_ids if not at_front_or_back(seat_id)]

def at_front_or_back(seat_id):
    row = seat_id // 8
    return row == 0 or row == 127

if __name__ == '__main__':
    main()
