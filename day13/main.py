def main():
    lines = read_notes('input')
    arrival_time, bus_ids = parse_notes(lines)
    bus_id, wait_time = find_earliest_bus(arrival_time, bus_ids)
    print(f'The earliest bus I can take has ID {bus_id} and I will have to wait {wait_time} minutes for it.')
    print(f'The product of those numbers is {bus_id * wait_time}.')

def read_notes(filename):
    with open(filename) as f:
        return f.readlines()

def parse_notes(lines):
    arrival_time = int(lines[0].strip())
    bus_id_strings = filter(lambda string: string != 'x', lines[1].strip().split(','))
    bus_ids = map(int, bus_id_strings)
    return arrival_time, bus_ids

def find_earliest_bus(arrival_time, bus_ids):
    shortest_wait_time = arrival_time
    bus_id_with_shortest_wait_time = None
    for bus_id in bus_ids:
        candidate_wait_time = -1 * (arrival_time % bus_id) + bus_id
        if candidate_wait_time < shortest_wait_time:
            shortest_wait_time = candidate_wait_time
            bus_id_with_shortest_wait_time = bus_id
    return bus_id_with_shortest_wait_time, shortest_wait_time

if __name__ == '__main__':
    main()
