import unittest

from main import AbsoluteShip
from main import Bearing
from main import WaypointShip

class TestAbsoluteShip(unittest.TestCase):
    def setUp(self):
        self._ship = AbsoluteShip()

    def test_forward(self):
        self._ship.forward(1)
        self.assertEqual(self._ship.east(), 1)
        self.assertEqual(self._ship.north(), 0)

        self._ship.forward(-2)
        self.assertEqual(self._ship.east(), -1)
        self.assertEqual(self._ship.north(), 0)

    def test_move__east(self):
        self._ship.move(Bearing.EAST, 1)
        self.assertEqual(self._ship.east(), 1)
        self.assertEqual(self._ship.north(), 0)

    def test_move__north(self):
        self._ship.move(Bearing.NORTH, 1)
        self.assertEqual(self._ship.east(), 0)
        self.assertEqual(self._ship.north(), 1)

    def test_move__west(self):
        self._ship.move(Bearing.WEST, 1)
        self.assertEqual(self._ship.east(), -1)
        self.assertEqual(self._ship.north(), 0)

    def test_move__south(self):
        self._ship.move(Bearing.SOUTH, 1)
        self.assertEqual(self._ship.east(), 0)
        self.assertEqual(self._ship.north(), -1)

    def test_turn__invalid(self):
        with self.assertRaises(ValueError):
            self._ship.turn(1)

    def test_turn__left(self):
        self._ship.turn(90)
        self.assertEqual(self._ship.bearing(), Bearing.NORTH)

    def test_turn__right(self):
        self._ship.turn(-90)
        self.assertEqual(self._ship.bearing(), Bearing.SOUTH)

    def test_turn__past_zero_positive(self):
        self._ship.turn(360 + 90)
        self.assertEqual(self._ship.bearing(), Bearing.NORTH)

    def test_turn__past_zero_negative(self):
        self._ship.turn(-360 - 90)
        self.assertEqual(self._ship.bearing(), Bearing.SOUTH)

class TestWaypointShip(unittest.TestCase):
    def setUp(self):
        self._ship = WaypointShip()

    def test_forward(self):
        self._ship.forward(2)
        self.assertEqual(self._ship.east(), 20)
        self.assertEqual(self._ship.north(), 2)

    def test_move(self):
        self._ship.move(Bearing.WEST, 2)
        self.assertEqual(self._ship.direction_east(), 8)
        self.assertEqual(self._ship.direction_north(), 1)

    def test_turn(self):
        self._ship.turn(90)
        self.assertEqual(self._ship.direction_east(), -1)
        self.assertEqual(self._ship.direction_north(), 10)
