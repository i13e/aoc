from collections import Counter

from aocd import data


def process_row(s: str) -> set[int]:
    _, win, hand = s.replace(":", "|").split("|")
    win = set(map(int, filter(str.isdigit, win.split(" "))))
    hand = set(map(int, filter(str.isdigit, hand.split(" "))))
    return win & hand


def part_1(s: str) -> int:
    return sum(
        2 ** (len(row) - 1)
        for row in map(lambda x: process_row(x), s.splitlines())
        if row
    )


def part_2(s: str) -> int:
    graph = Counter()
    lines = s.splitlines()
    for i, row in enumerate(map(lambda x: process_row(x), s.splitlines())):
        for j in range(i + 1, min(len(lines), i + 1 + len(row))):
            graph[j] += graph[i] + 1
    return sum(graph.values()) + len(lines)


def main() -> int:
    print(part_1(str(data)))
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
