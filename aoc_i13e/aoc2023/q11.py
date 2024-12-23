from itertools import combinations

from aocd import data


def expand_points(val: int, empty_lines: set[int], multiplier: int) -> int:
    return len(tuple(filter(lambda i: i < val, empty_lines))) * (multiplier - 1)


def part_1(s: str) -> int:
    lines = s.splitlines()

    empty_y = [y for y, line in enumerate(lines) if "#" not in line]
    empty_x = [x for x, line in enumerate(zip(*lines)) if all(c == "." for c in line)]

    points = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                points.append(
                    (
                        x + sum(c_x < x for c_x in empty_x),
                        y + sum(c_y < y for c_y in empty_y),
                    )
                )

    res = 0
    for (x1, y1), (x2, y2) in combinations(points, 2):
        res += abs(x1 - x2) + abs(y1 - y2)
    return res


def part_2(s: str, ex: int = 1000000 - 1) -> int:
    lines = s.splitlines()

    empty_y = [y for y, line in enumerate(lines) if "#" not in line]
    empty_x = [x for x, line in enumerate(zip(*lines)) if all(c == "." for c in line)]

    points = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                points.append(
                    (
                        x + ex * sum(c_x < x for c_x in empty_x),
                        y + ex * sum(c_y < y for c_y in empty_y),
                    )
                )

    res = 0
    for (x1, y1), (x2, y2) in combinations(points, 2):
        res += abs(x1 - x2) + abs(y1 - y2)
    return res


def main() -> int:
    print(part_1(str(data)))
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
