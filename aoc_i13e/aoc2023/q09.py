from itertools import pairwise

from aocd import data


def simplify(nums: list[int]) -> list[list[int]]:
    res = [nums]
    while any(e for e in res[-1]):
        res.append([b - a for a, b in pairwise(res[-1])])
    return res


def extrapolate(layers: list[list[int]]) -> int:
    for a, b in pairwise(layers[::-1]):
        b.append(a[-1] + b[-1])
    return layers[0][-1]


def part_1(s: str) -> int:
    histories = [list(map(int, line.split())) for line in s.splitlines()]
    return sum(extrapolate(simplify(h)) for h in histories)


def part_2(s: str) -> int:
    histories = [list(map(int, line.split())) for line in s.splitlines()]
    return sum(extrapolate(simplify(h[::-1])) for h in histories)


def main() -> int:
    print(part_1(str(data)))
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
