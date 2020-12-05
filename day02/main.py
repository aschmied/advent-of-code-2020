def main():
    valid_passwords_by_range_policy = 0
    valid_passwords_by_position_policy = 0
    with open('input') as f:
        for line in f:
            policy_string, password = parse_line(line.strip())
            policy = Policy.parse(policy_string)
            if policy.is_valid_by_range_policy(password):
                valid_passwords_by_range_policy += 1
            if policy.is_valid_by_position_policy(password):
                valid_passwords_by_position_policy += 1
    print(f'There are {valid_passwords_by_range_policy} valid passwords by "range" policy.')
    print(f'There are {valid_passwords_by_position_policy} valid passwords by "position" policy.')

def parse_line(line):
    tokens = line.split(':', 1)
    policy_string = tokens[0]
    password = tokens[1].strip()
    return policy_string, password

class Policy:
    def __init__(self, first_number, second_number, letter):
        self._first_number = first_number
        self._second_number = second_number
        self._letter = letter

    def is_valid_by_range_policy(self, password):
        count = password.count(self._letter)
        return count >= self._first_number and count <= self._second_number

    def is_valid_by_position_policy(self, password):
        index1 = self._first_number - 1
        index2 = self._second_number - 1
        return (password[index1] == self._letter) != (password[index2] == self._letter)

    @classmethod
    def parse (cls, string):
        tokens = string.split(' ')
        first_number_string, second_number_string = tokens[0].split('-')
        letter = tokens[1]
        return cls(int(first_number_string), int(second_number_string), letter)

if __name__ == '__main__':
    main()
