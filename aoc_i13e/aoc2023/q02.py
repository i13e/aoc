from functools import reduce

from aocd import data


def get_data(s: str) -> tuple:
    color = next(c for c in "grb" if c in s)
    number = int("".join(filter(str.isdigit, s)))
    return color, number


def parse_input(s: str) -> list[str]:
    return s.replace(";", ",").split(":")[1].split(",")


def part_1(s: str) -> int:
    COLORS = {"r": 12, "g": 13, "b": 14}
    res = 0
    for i, line in enumerate(s.splitlines(), 1):
        game = map(lambda x: get_data(x), parse_input(line))
        res += i * all(n <= COLORS[c] for c, n in game)
    return res


def part_2(s: str) -> int:
    res = 0
    for line in s.splitlines():
        COLORS = {"r": 0, "g": 0, "b": 0}
        for game in map(lambda x: get_data(x), parse_input(line)):
            COLORS[game[0]] = max(COLORS[game[0]], game[1])
        res += reduce(lambda a, b: a * b, COLORS.values())

    return res


def main() -> int:
    print(part_1(str(data)))
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
