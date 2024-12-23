from itertools import groupby

from aocd import data


def parse_input(s: str) -> list[int]:
    return [
        sum(int(line) for line in group)
        for key, group in groupby(s.splitlines(), key=bool)
        if key
    ]


def part_1(s: str) -> int:
    return max(parse_input(s))


def part_2(s: str) -> int:
    elves = parse_input(s)
    return sum(sorted(elves)[-3:])


def main() -> int:
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
