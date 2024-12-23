from __future__ import annotations
from itertools import chain

from aocd import data

import pytest


def part_1(s: str) -> int:
    left, right = 0, len(s) - 1
    if right % 2 == 1:
        right -= 1
    nums = list(map(int, s.strip()))
    arr = []
    while left <= right:
        if left % 2 == 0:
            arr.extend([left // 2] * nums[left])
            nums[left] = 0
            left += 1
        else:
            fill = min(nums[left], nums[right])
            arr.extend([right // 2] * fill)
            nums[right] -= fill
            nums[left] -= fill
            if nums[right] == 0:
                right -= 2
            if nums[left] == 0:
                left += 1
    return sum(i * n for i, n in enumerate(arr))


def part_2(s: str) -> int:
    nums = list(map(int, s.strip()))
    arr = [[] for _ in range(len(nums))]
    stack = []
    q = []

    for i, n in enumerate(nums):
        if i % 2:
            q.append([i, n])
            arr[i] = [-1] * n
        else:
            stack.append([i, n])
            arr[i] = [i // 2] * n

    for i, n in reversed(stack):
        found = False
        loc = -1
        for k, (loc, empty) in enumerate(q):
            if empty >= n and loc < i:
                q[k][1] -= n
                found = True
                break
        if found and loc:
            arr[i] = [-1] * n
            j = 0
            while n:
                if arr[loc][j] == -1:
                    n -= 1
                    arr[loc][j] = i // 2
                j += 1

    return sum(i * n for i, n in enumerate(list(chain(*arr))) if n > -1)


INPUT_S = """\
2333133121414131402
"""


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, 1928, 2858),
        (str(data), 6323641412437, 6351801932670),
    ),
)
def test(input_s: str, expected_1: int, expected_2: int) -> None:
    if expected_1:
        assert part_1(input_s) == expected_1

    if expected_2:
        assert part_2(input_s) == expected_2


def main() -> int:
    print(part_1(str(data)))

    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
