import enum

def main():
    pass

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

if __name__ == '__main__':
    main()
