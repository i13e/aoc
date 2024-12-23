from __future__ import annotations
from collections import Counter

from aocd import data

# from aocd import submit
import pytest

# import advent.support


def parse(s: str, part_2: bool = False):
    return zip(*(map(int, line.split()) for line in s.splitlines()))


def part_1(s: str) -> int:
    return sum(abs(a - b) for a, b in zip(*map(sorted, parse(s))))


def part_2(s: str) -> int:
    x, y = parse(s)
    y = Counter(y)
    return sum(y[a] * a for a in x)


INPUT_S = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, 11, 31),
        (str(data), 2192892, 22962826),
    ),
)
def test(input_s: str, expected_1: int, expected_2: int) -> None:
    if expected_1:
        assert part_1(input_s) == expected_1

    if expected_2:
        assert part_2(input_s) == expected_2


def main() -> int:
    # with advent.support.timing():
    print(part_1(str(data)))

    # with advent.support.timing():
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
