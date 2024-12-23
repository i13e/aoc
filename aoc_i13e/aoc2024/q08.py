from __future__ import annotations
from collections import defaultdict
from itertools import permutations
from itertools import product

from aocd import data

# from aocd import submit
import pytest

# import advent.support


def part_1(s: str) -> int:
    graph = defaultdict(list)
    mat = []
    for row in s.splitlines():
        mat.append(list(row))

    R, C = range(len(mat)), range(len(mat[0]))
    for r, c in product(R, C):
        if mat[r][c] not in ".":
            graph[mat[r][c]].append((r, c))

    for antenna in graph:
        for a, b in permutations(graph[antenna], 2):
            r, c = 2 * a[0] - b[0], 2 * a[1] - b[1]

            if r in R and c in C and mat[r][c] != "#":
                mat[r][c] = "#"

    return sum(row.count("#") for row in mat)


def part_2(s: str) -> int:
    graph = defaultdict(list)
    mat = []
    for row in s.splitlines():
        mat.append(list(row))

    R, C = range(len(mat)), range(len(mat[0]))
    for r, c in product(R, C):
        if mat[r][c] not in ".":
            graph[mat[r][c]].append((r, c))

    for antenna in graph:
        for a, b in permutations(graph[antenna], 2):
            r, c = a[0], a[1]

            while True:
                r -= a[0] - b[0]
                c -= a[1] - b[1]
                if not (r in R and c in C):
                    break
                if mat[r][c] == "#":
                    continue
                mat[r][c] = "#"

    return sum(row.count("#") for row in mat)


INPUT_S = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, 14, 34),
        (str(data), 379, 1339),
    ),
)
def test(input_s: str, expected_1: int, expected_2: int) -> None:
    if expected_1:
        assert part_1(input_s) == expected_1

    if expected_2:
        assert part_2(input_s) == expected_2


def main() -> int:
    # with advent.support.timing():
    print(part_1(str(data)))

    # with advent.support.timing():
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
