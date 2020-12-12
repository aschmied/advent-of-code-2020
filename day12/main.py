import enum

def main():
    commands = read_movement_commands('input')
    ship = Ship()
    for command in commands:
        command.execute(ship)
    print(f'Manhattan distance from origin is {abs(ship.east()) + abs(ship.north())}')

def read_movement_commands(filename):
    with open(filename) as f:
        return [parse_command(line.strip()) for line in f]

class Ship:
    def __init__(self):
        self._east = 0
        self._north = 0
        self._bearing = Bearing.EAST

    def east(self):
        return self._east

    def north(self):
        return self._north

    def bearing(self):
        return self._bearing

    def forward(self, steps):
        self.move(self._bearing, steps)

    def move(self, bearing, steps):
        step_offset = bearing.offset()
        self._east += steps * step_offset[0]
        self._north += steps * step_offset[1]        

    def turn(self, degrees):
        if degrees % 90 != 0:
            raise ValueError(r'Degrees must be a multiple of 90. Got {degrees}')

        new_degrees = self._bearing.value + degrees
        new_degrees = new_degrees % 360
        if new_degrees < 0:
            new_degrees += 360
        self._bearing = Bearing(new_degrees)

class Bearing(enum.Enum):
    EAST = 0
    NORTH = 90
    WEST = 180
    SOUTH = 270

    def offset(self):
        if self == Bearing.EAST:
            return (1, 0)
        elif self == Bearing.NORTH:
            return (0, 1)
        elif self == Bearing.WEST:
            return (-1, 0)
        elif self == Bearing.SOUTH:
            return (0, -1)

    @classmethod
    def parse(cls, string):
        bearing_string_to_degrees = {
            'E': 0,
            'N': 90,
            'W': 180,
            'S': 270}
        degrees = bearing_string_to_degrees[string]
        return Bearing(degrees)

def parse_command(command):
    action = command[0]
    argument = int(command[1:])

    if action in ['E', 'N', 'W', 'S']:
        return MoveCommand.build(action, argument)
    elif action in ['L', 'R']:
        return TurnCommand.build(action, argument)
    elif action in ['F']:
        return ForwardCommand.build(action, argument)
    raise ValueError(f'Invalid command: {command}')

class MoveCommand:
    def __init__(self, bearing, distance):
        self._bearing = bearing
        self._distance = distance

    def execute(self, ship):
        ship.move(self._bearing, self._distance)

    @classmethod
    def build(cls, action, argument):
        bearing = Bearing.parse(action)
        return cls(bearing, argument)

class TurnCommand:
    def __init__(self, degrees):
        self._degrees = degrees

    def execute(self, ship):
        ship.turn(self._degrees)

    @classmethod
    def build(cls, action, argument):
        if action == 'R':
            argument *= -1
        return TurnCommand(argument)

class ForwardCommand:
    def __init__(self, distance):
        self._distance = distance

    def execute(self, ship):
        ship.forward(self._distance)

    @classmethod
    def build(cls, action, argument):
        return ForwardCommand(argument)

if __name__ == '__main__':
    main()
