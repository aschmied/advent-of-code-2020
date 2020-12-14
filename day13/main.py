import itertools
import math

def main():
    lines = read_notes('input')
    arrival_time, bus_ids = parse_notes(lines)
    bus_id, wait_time = find_earliest_bus(arrival_time, bus_ids)
    print(f'The earliest bus I can take has ID {bus_id} and I will have to wait {wait_time} minutes for it.')
    print(f'The product of those numbers is {int(bus_id) * wait_time}.')
    print('')

    earliest_magic_time = find_earliest_magic_time(bus_ids)

def read_notes(filename):
    with open(filename) as f:
        return f.readlines()

def parse_notes(lines):
    arrival_time = int(lines[0].strip())
    bus_ids = lines[1].strip().split(',')
    return arrival_time, bus_ids

def find_earliest_bus(arrival_time, bus_ids):
    shortest_wait_time = arrival_time
    bus_id_with_shortest_wait_time = None
    for bus_id in bus_ids:
        if bus_id == 'x':
            continue
        bus_id_int = int(bus_id)
        candidate_wait_time = -1 * (arrival_time % bus_id_int) + bus_id_int
        if candidate_wait_time < shortest_wait_time:
            shortest_wait_time = candidate_wait_time
            bus_id_with_shortest_wait_time = bus_id
    return bus_id_with_shortest_wait_time, shortest_wait_time

def find_earliest_magic_time(bus_ids):
    '''We are given a sequence where each element is a bus ID or an `x`.
    All buses depart at time 0. The ID of a bus indicates how many minutes
    past 0 that bus departs again. For example, bus 3 departs at 0 minutes,
    3 minutes, 6 minutes, etc. We ignore the `x` elements in the sequence.

    We are asked to find the earliest time `t` such that the bus at index
    `a` in the sequence departs `a` minutes past `t`. So we want:

      t == bus_id - a (mod bus_id), if bus_id > a
      t == bus_id - (index % bus_id) (mod bus_id), if bus_id < a

    One way to solve `t` is by using Chinese Remainder Theorem
    (https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html).

    However, in the puzzle each `bus_id` is prime. CRT would only require
    that the `bus_id`s be pairwise coprime, so there is probably a simpler\
    way to solve this.
    '''
    indexes = []
    bus_id_ints = []
    for index, bus_id in enumerate(bus_ids):
        if bus_id == 'x':
            continue
        indexes.append(index)
        bus_id_ints.append(int(bus_id))
    
    remainders = []
    for index, bus_id_int in zip(indexes, bus_id_ints):
        if bus_id_int > index:
            r = bus_id_int - index
        else:
            r = bus_id_int - (index % bus_id_int)
        remainders.append(r)
    print('Enter the following system in a Chinese Remainder Theorem calculator:')
    for remainder, bus_id_int in zip(remainders, bus_id_ints):
        print(f't == {remainder} (mod {bus_id_int})')

    print('I used the one at https://www.dcode.fr/chinese-remainder.')
    print('It gave me the answer of 725169163285238.')

if __name__ == '__main__':
    main()
