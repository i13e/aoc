# puzzle prompt: https://adventofcode.com/2023/day/5
from collections import defaultdict

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 5
    Range = tuple[int, int]

    def get_maps(self, lines: list[str]) -> dict[int, dict[Range, Range]]:
        maps = defaultdict(dict)
        key = 0
        for line in filter(lambda x: ":" not in x, lines[2:]):
            if line:
                line = list(map(int, line.strip().split()))
                dst = (line[0], line[0] + line[2])
                src = (line[1], line[1] + line[2])
                maps[key][src] = dst
            else:
                key += 1
        return maps

    @answer(240320250)
    def part_1(self) -> int:
        seeds = list(map(int, self.input[0].split(":")[1].strip().split()))
        maps = self.get_maps(self.input)
        for ranges in maps.values():
            for i, seed in enumerate(seeds):
                for src, dst in ranges.items():
                    if seed in range(*src):
                        seeds[i] = seed - src[0] + dst[0]
        return min(seeds)

    @answer(28580589)
    def part_2(self) -> int:
        seeds = list(map(int, self.input[0].split(":")[1].strip().split()))
        seeds = [[s, s + e] for s, e in zip(seeds[::2], seeds[1::2])]
        maps = self.get_maps(self.input)

        for ranges in maps.values():
            for i, (start, end) in enumerate(seeds):
                for src, dst in ranges.items():
                    if start in range(*src):
                        if end not in range(*src):
                            seeds.append([src[1], end])
                        seeds[i][0] = start - src[0] + dst[0]
                        seeds[i][1] = min(end - src[1], 0) + dst[1]

        return min(seeds)[0]

    # @answer((1234, 5678))
    # def solve(self) -> tuple[int | str, int | str]:
    #     return (0, 0)
