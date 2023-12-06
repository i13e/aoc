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
                        offset = seed - src[0]
                        seeds[i] = dst[0] + offset
        return min(seeds)

    @answer(28580589)
    def part_2(self) -> int:
        seeds = list(map(int, self.input[0].split(":")[1].strip().split()))
        q = []
        for i in range(0, len(seeds), 2):
            q.append((seeds[i], seeds[i] + seeds[i + 1]))
        maps = self.get_maps(self.input)

        for i in range(len(maps)):
            tmp = []
            for start, end in q:
                for src, dst in maps[i].items():
                    if start in range(*src):
                        overlap = [start - src[0], min(end - src[1], 0)]
                        if src[1] < end:
                            q.append((src[1], end))
                        tmp.append((dst[0] + overlap[0], dst[1] + overlap[1]))
                        break
                else:
                    tmp.append((start, end))
            q = tmp
        return min(q)[0]

    # @answer((1234, 5678))
    # def solve(self) -> tuple[int | str, int | str]:
    #     return (0, 0)
