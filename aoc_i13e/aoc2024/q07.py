from __future__ import annotations
from functools import cache

from aocd import data

# from aocd import submit
import pytest

# import advent.support


def part_1(s: str) -> int:
    res = 0

    @cache
    def dp(i: int, n: int, x: int) -> bool:
        if x > n:
            return False

        if i == len(nums):
            return x == n

        add = dp(i + 1, n, int(nums[i]) + x)
        mul = dp(i + 1, n, int(nums[i]) * x)
        return add or mul

    for row in s.splitlines():
        total, nums = row.split(":")
        nums = list(nums.split())
        res += int(total) * dp(1, int(total), int(nums[0]))
    return res


def part_2(s: str) -> int:
    res = 0

    @cache
    def dp(i: int, n: int, x: int) -> bool:
        if x > n:
            return False

        if i == len(nums):
            return x == n

        add = dp(i + 1, n, int(nums[i]) + x)
        mul = dp(i + 1, n, int(nums[i]) * x)
        concat = dp(i + 1, n, int(str(x) + nums[i]))
        return add or mul or concat

    for row in s.splitlines():
        total, nums = row.split(":")
        nums = list(nums.split())
        res += int(total) * dp(1, int(total), int(nums[0]))
    return res


INPUT_S = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, 3749, 12839601725877),
        (str(data), 11387, 149956401519484),
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
