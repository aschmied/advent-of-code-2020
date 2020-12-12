import enum
import math

def main():
    commands = read_movement_commands('input')
    absolute_ship = AbsoluteShip()
    waypoint_ship = WaypointShip()
    for command in commands:
        command.execute(absolute_ship)
        command.execute(waypoint_ship)
    print(f'Manhattan distance from origin is {abs(absolute_ship.east()) + abs(absolute_ship.north())} for absolute ship')
    print(f'Manhattan distance from origin is {abs(waypoint_ship.east()) + abs(waypoint_ship.north())} for waypoint ship')

def read_movement_commands(filename):
    with open(filename) as f:
        return [parse_command(line.strip()) for line in f]

class AbsoluteShip:
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
            raise ValueError(f'Degrees must be a multiple of 90. Got {degrees}')

        new_degrees = self._bearing.value + degrees
        self._bearing = Bearing(_normalize_degrees(new_degrees))

class WaypointShip:
    def __init__(self):
        self._east = 0
        self._north = 0
        self._direction_east = 10
        self._direction_north = 1

    def east(self):
        return self._east

    def north(self):
        return self._north

    def direction_east(self):
        return self._direction_east

    def direction_north(self):
        return self._direction_north

    def move(self, bearing, steps):
        step_offset = bearing.offset()
        self._direction_east += steps * step_offset[0]
        self._direction_north += steps * step_offset[1]

    def forward(self, steps):
        self._east += steps * self._direction_east
        self._north += steps * self._direction_north

    def turn(self, degrees):
        if degrees % 90 != 0:
            raise ValueError(f'Degrees must be a multiple of 90. Got {degrees}')

        rotation_matrix = self._get_rotation_matrix(_normalize_degrees(degrees))
        rotated_direction = (
            rotation_matrix[0][0] * self._direction_east + rotation_matrix[0][1] * self._direction_north,
            rotation_matrix[1][0] * self._direction_east + rotation_matrix[1][1] * self._direction_north)
        self._direction_east = rotated_direction[0]
        self._direction_north = rotated_direction[1]

    def _get_rotation_matrix(self, degrees):
        radians = math.radians(degrees)
        return (
            (round(math.cos(radians)), round(-math.sin(radians))),
            (round(math.sin(radians)), round(math.cos(radians))))

def _normalize_degrees(degrees):
    normalized_degrees = degrees % 360
    if normalized_degrees < 0:
        return normalized_degrees + 360
    return normalized_degrees

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
