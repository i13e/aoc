from aocd import data


def part_1(s: str) -> int:
    res = 0
    for i in s.splitlines():
        n = len(i) // 2
        c = (set(i[:n]) & set(i[n:])).pop()
        res += ord(c.lower()) - ord("a") + [1, 27][c.isupper()]
    return res


def part_2(s: str) -> int:
    res = 0
    for i in range(0, len(s.splitlines()), 3):
        l1, l2, l3 = s.splitlines()[i : i + 3]
        c = (set(l1) & set(l2) & set(l3)).pop()
        res += ord(c.lower()) - ord("a") + [1, 27][c.isupper()]
    return res


def main() -> int:
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
