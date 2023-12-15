from __future__ import annotations

from aocd import data
import pytest

import support


def parse(s: str, part_2: bool = False) -> int:
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, word in enumerate(words * part_2, 1):
        s = s.replace(word, f"{word[0]}{i}{word[-1]}")

    a = b = ""
    for c in filter(str.isdigit, s):
        a, b = a or c, c
    return int(a + b)


def part_1(s: str) -> int:
    return sum(parse(line) for line in s.splitlines())


def part_2(s: str) -> int:
    return sum(parse(line, True) for line in s.splitlines())


INPUT_S = """\

"""


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, 0, 0),
        (str(data), 54304, 54418),
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
