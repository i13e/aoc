from functools import reduce

from aocd import data


def count_wins(time: int, distance: int) -> int:
    return sum(t * (time - t) > distance for t in range(1, time))


def part_1(s: str) -> int:
    lines = s.splitlines()
    races = zip(*(map(int, line.split()[1:]) for line in lines))

    return reduce(lambda res, race: res * count_wins(*race), races, 1)


def part_2(s: str) -> int:
    lines = s.splitlines()
    time, distance = [int("".join(line.split()[1:])) for line in lines]
    return count_wins(time, distance)


def main() -> int:
    print(part_1(str(data)))
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
