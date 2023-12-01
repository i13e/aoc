# puzzle prompt: https://adventofcode.com/2023/day/1

from itertools import combinations

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(54304)
    def part_1(self) -> int | str:
        res = 0
        for line in self.input:
            nums = [int(n) for n in line if n.isdigit()]
            res += nums[0] * 10 + nums[-1]
        return res

    @answer(54418)
    def part_2(self) -> int | str:
        words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        rmap = {w: i for i, w in enumerate(words, 1)}
        res = 0
        for line in self.input:
            nums = []
            for i, j in combinations(range(len(line) + 1), 2):
                cur = line[i:j]
                if cur.isdigit():
                    nums.append(int(cur))
                elif cur in rmap:
                    nums.append(rmap[cur])
            res += nums[0] * 10 + nums[-1]
        return res

    # @answer((1234, 5678))
    # def solve(self) -> tuple[int | str, int | str]:
    #     return (0, 0)
