import re

REQUIRED_KEYS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid']

def main():
    with open('input') as f:
        valid_passport_count = 0
        strictly_valid_passport_count = 0
        for chunk in iterate_in_chunks(f):
            combined = ' '.join([line.strip() for line in chunk])
            passport = parse_passport(combined)
            if is_passport_valid(passport):
                valid_passport_count += 1
            if is_passport_strictly_valid(passport):
                strictly_valid_passport_count += 1
    print(f'There were {valid_passport_count} valid passports.')
    print(f'There were {strictly_valid_passport_count} strictly valid passports.')


def iterate_in_chunks(iterable, delimiter='\n'):
    elements_in_chunk = []
    for element in iterable:
        if element == delimiter:
            yield elements_in_chunk
            elements_in_chunk = []
        else:
            elements_in_chunk.append(element)
    yield elements_in_chunk

def parse_passport(string):
    key_value_strings = string.split(' ')
    key_value_tuples = [s.split(':', 1) for s in key_value_strings]
    return {t[0]: t[1] for t in key_value_tuples}

def is_passport_valid(passport):
    return all([k in passport.keys() for k in REQUIRED_KEYS])

def is_passport_strictly_valid(passport):
    if not is_passport_valid(passport):
        return False

    validation_table = {
        'byr': lambda x: number_in_range(1920, 2002, x),
        'iyr': lambda x: number_in_range(2010, 2020, x),
        'eyr': lambda x: number_in_range(2020, 2030, x),
        'pid': lambda x: re.match(r'^[0-9]{9}$', x),
        'hgt': validate_height,
        'hcl': lambda x: re.match(r'^#[0-9a-f]{6}$', x),
        'ecl': lambda x: re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', x)
    }

    for key, value in passport.items():
        validation_function = validation_table.get(key)
        if validation_function and not validation_function(value):
            return False
    return True

def number_in_range(min, max, number_string):
    try:
        number = int(number_string)
        return number >= min and number <= max
    except ValueError:
        return False

def validate_height(height_string):
    magnitude_string = height_string[0:-2]
    units = height_string[-2:]
    if units == 'cm':
        return number_in_range(150, 193, magnitude_string)
    elif units == 'in':
        return number_in_range(59, 76, magnitude_string)
    else:
        return False

if __name__ == '__main__':
    main()
