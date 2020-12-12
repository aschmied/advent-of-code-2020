## Advent of Code 2020

This repo contains my solutions to the [Advent of Code 2020](http://adventofcode.com/2020) puzzles.

## Prerequisites

Solutions are tested with Python 3.9.0 on Windows 10. There are no other dependencies.

## Running

The solutions are in "day" directories and the main programs are called "main.py." So, to run the solution for day 1, do:

```
> cd day01
> python main.py
```

## Tests

Some solutions have tests. To run the tests do e.g.:

```
> cd day04
> python -m unittest discover
```

## My Favourite Solutions

### [Day 4](https://adventofcode.com/2020/day/4)

Coming up with the representation of the passport validation rules in the `is_passport_strictly_valid` method was enjoyable.

### [Day 5](https://adventofcode.com/2020/day/5)

Binary search in disguise.

### [Day 9](https://adventofcode.com/2020/day/9)

In one possible solution, two data structures working together solve the problem.

### [Day 10](https://adventofcode.com/2020/day/10)

My path to a solution highlighted the power of dynamic programming. I tried a brute force recursive approach first. It didn't finish after a few minutes, so I added memoization. It finished faster than I could blink.

## License

[2-clause BSD](https://opensource.org/licenses/BSD-2-Clause)
