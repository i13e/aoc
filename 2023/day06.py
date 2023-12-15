from __future__ import annotations

from functools import reduce

import pytest
from aocd import data

import support

INPUT_S = """\
Time:      7  15   30
Distance:  9  40  200
"""
EXPECTED_1 = 288
EXPECTED_2 = 71503


def count_wins(time: int, distance: int) -> int:
    return sum(t * (time - t) > distance for t in range(1, time))


def part_1(s: str) -> int:
    lines = s.splitlines()
    races = zip(*(map(int, line.split()[1:]) for line in lines))

    return reduce(lambda res, race: res * count_wins(*race), races, 1)


def part_2(s: str) -> int:
    lines = s.splitlines()
    time, distance = [int("".join(line.split()[1:])) for line in lines]
    return count_wins(time, distance)


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, EXPECTED_1, EXPECTED_2),
        (str(data), 3316275, 27102791),
    ),
)
def test(input_s: str, expected_1: int, expected_2: int) -> None:
    if result_1 := part_1(input_s):
        assert result_1 == expected_1

    if result_2 := part_2(input_s):
        assert result_2 == expected_2


def main() -> int:
    with support.timing():
        print(part_1(str(data)))

    with support.timing():
        print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
