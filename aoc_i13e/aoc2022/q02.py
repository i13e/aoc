from aocd import data


def part_1(s: str) -> int:
    res = 0
    for i in s.splitlines():
        res += (ord(i[-1]) - ord(i[0]) - 1) % 3 * 3
        res += ord(i[-1]) - ord("W")
    return res


def part_2(s: str) -> int:
    res = 0
    for i in s.splitlines():
        res += (ord(i[-1]) + ord(i[0]) - 1) % 3 + 1
        res += (ord(i[-1]) - ord("X")) * 3
    return res


def main() -> int:
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
