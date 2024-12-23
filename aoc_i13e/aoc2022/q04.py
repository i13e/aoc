from aocd import data


def part_1(s: str) -> int:
    res = 0
    for pair in s.splitlines():
        one, two = pair.split(",")
        s1, e1 = (int(c) for c in one.split("-"))
        s2, e2 = (int(c) for c in two.split("-"))
        # Check if one range fully contains the other
        if s1 <= s2 <= e2 <= e1 or s2 <= s1 <= e1 <= e2:
            res += 1
    return res


def part_2(s: str) -> int:
    res = 0
    for pair in s.splitlines():
        one, two = pair.split(",")
        s1, e1 = (int(c) for c in one.split("-"))
        s2, e2 = (int(c) for c in two.split("-"))
        # Check if the ranges overlap
        if s2 <= e1 and s1 <= e2:
            res += 1
    return res


def main() -> int:
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
