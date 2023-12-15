from __future__ import annotations

from collections import defaultdict

from aocd import data
import pytest

import support


Range = tuple[int, int]


def get_maps(lines: list[str]) -> dict[int, dict[Range, Range]]:
    maps = defaultdict(dict)
    key = 0
    for line in filter(lambda x: ":" not in x, lines[2:]):
        if line:
            line = list(map(int, line.split()))
            dst = (line[0], line[0] + line[2])
            src = (line[1], line[1] + line[2])
            maps[key][src] = dst
        else:
            key += 1
    return maps


def part_1(s: str) -> int:
    lines = s.splitlines()
    seeds = list(map(int, lines[0].split()[1:]))
    maps = get_maps(lines)
    for ranges in maps.values():
        for i, seed in enumerate(seeds):
            for src, dst in ranges.items():
                if seed in range(*src):
                    seeds[i] = seed - src[0] + dst[0]
    return min(seeds)


def part_2(s: str) -> int:
    lines = s.splitlines()
    seeds = list(map(int, lines[0].split()[1:]))
    seeds = [[s, s + e] for s, e in zip(seeds[::2], seeds[1::2])]
    maps = get_maps(lines)

    for ranges in maps.values():
        for i, (start, end) in enumerate(seeds):
            for src, dst in ranges.items():
                if start in range(*src):
                    if end not in range(*src):
                        seeds.append([src[1], end])
                    seeds[i][0] = start - src[0] + dst[0]
                    seeds[i][1] = min(end - src[1], 0) + dst[1]

    return min(seeds)[0]


INPUT_S = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
EXPECTED_1 = 35
EXPECTED_2 = 46


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, EXPECTED_1, EXPECTED_2),
        (str(data), 240320250, 28580589),
    ),
)
def test_d(input_s: str, expected_1: int, expected_2: int) -> None:
    if result_1 := part_1(input_s):
        assert result_1 == expected_1

    if result_2 := part_2(input_s):
        assert result_2 == expected_2


def main() -> int:
    with support.timing():
        print(part_1(str(data)))

    with support.timing():
        print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
