def main():
    with open('input') as f:
        process_input(f)

def process_input(iterable):
    total_yes_answers = 0
    total_yes_for_all_in_group = 0
    for chunk in iterate_chunks(iterable):
        yes_answers_by_traveller = [line.strip() for line in chunk]
        total_yes_answers += len(union_of_chars(yes_answers_by_traveller))
        total_yes_for_all_in_group += len(intersection_of_chars(yes_answers_by_traveller))

    print(f'Sum of total yes answer counts is {total_yes_answers}')
    print(f'Sum of questions answered yes by everyone counts is {total_yes_for_all_in_group}')

def union_of_chars(strings):
    chars = []
    for string in strings:
        chars.extend(list(string))
    return set(chars)

def intersection_of_chars(strings):
    if len(strings) == 0:
        return set()

    intersection_of_chars = set(list(strings[0]))
    return intersection_of_chars.intersection(*[set(list(s)) for s in strings])

def iterate_chunks(iterable, delimiter='\n'):
    elements_in_chunk = []
    for element in iterable:
        if element == delimiter:
            yield elements_in_chunk
            elements_in_chunk = []
        else:
            elements_in_chunk.append(element)
    yield elements_in_chunk

if __name__ == '__main__':
    main()
