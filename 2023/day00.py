from __future__ import annotations

from aocd import data
import pytest

from support import support


def part_1(s: str) -> int:
    numbers = support.parse_numbers_split(s)
    for n in numbers:
        pass

    lines = s.splitlines()
    for line in lines:
        pass
    # TODO: implement solution here!
    return 0


def part_2(s: str) -> int:
    numbers = support.parse_numbers_split(s)
    for n in numbers:
        pass

    lines = s.splitlines()
    for line in lines:
        pass
    # TODO: implement solution here!
    return 0


INPUT_S = """\

"""
EXPECTED_1 = 1
EXPECTED_2 = 2


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, EXPECTED_1, EXPECTED_2),
        # (str(data), ANSWER_1, ANSWER_2),
    ),
)
def test_d(input_s: str, expected_1: int, expected_2: int) -> None:
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
