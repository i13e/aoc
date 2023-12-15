from __future__ import annotations

from functools import reduce

from aocd import data
import pytest

import support


def get_data(s: str) -> tuple:
    color = next(c for c in "grb" if c in s)
    number = int("".join(filter(str.isdigit, s)))
    return color, number


def parse_input(s: str) -> list[str]:
    return s.replace(";", ",").split(":")[1].split(",")


def part_1(s: str) -> int:
    COLORS = {"r": 12, "g": 13, "b": 14}
    res = 0
    for i, line in enumerate(s.splitlines(), 1):
        game = map(lambda x: get_data(x), parse_input(line))
        res += i * all(n <= COLORS[c] for c, n in game)
    return res


def part_2(s: str) -> int:
    res = 0
    for line in s.splitlines():
        COLORS = {"r": 0, "g": 0, "b": 0}
        for game in map(lambda x: get_data(x), parse_input(line)):
            COLORS[game[0]] = max(COLORS[game[0]], game[1])
        res += reduce(lambda a, b: a * b, COLORS.values())

    return res


INPUT_S = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, 8, 1734),
        (str(data), 1734, 70387),
    ),
)
def test(input_s: str, expected_1: int, expected_2: int) -> None:
    if expected_1:
        assert part_1(input_s) == expected_1

    if expected_2:
        assert part_2(input_s) == expected_2


def main() -> int:
    with support.timing():
        print(part_1(str(data)))

    with support.timing():
        print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
