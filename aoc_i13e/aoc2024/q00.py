from __future__ import annotations

from aocd import data

from aoc_i13e import support


def part_1(s: str) -> str:
    numbers = support.parse_numbers_split(s)
    res = 0
    for n in numbers:
        pass

    lines = s.splitlines()
    for line in lines:
        pass
    return str(res)


def part_2(s: str) -> str:
    numbers = support.parse_numbers_split(s)
    res = 0
    for n in numbers:
        pass

    lines = s.splitlines()
    for line in lines:
        pass
    return str(res)


def main() -> int:
    with support.timing():
        print(part_1(str(data)))

    with support.timing():
        print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
