from __future__ import annotations
from itertools import pairwise

from aocd import data

# from aocd import submit
import pytest

# import advent.support


def parse(s: str, part_2: bool = False):
    yield from (list(map(int, row.split())) for row in s.splitlines())


def is_safe(row: list[int]) -> int:
    diffs = [a - b for a, b in pairwise(row)]
    is_monotonic = all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    is_in_range = all(0 < abs(d) < 4 for d in diffs)
    return is_monotonic and is_in_range


def part_1(s: str) -> int:
    return sum(is_safe(report) for report in parse(s))


def part_2(s: str) -> int:
    res = 0
    for report in parse(s):
        res += any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))
    return res


INPUT_S = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, 2, 4),
        (str(data), 516, 561),
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
