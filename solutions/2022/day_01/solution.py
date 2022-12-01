# prompt: https://adventofcode.com/2022/day/1

from typing import List
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 1

    @answer(74394)
    def part_1(self) -> int:
        self.res, tmp = [], 0
        for line in self.input:
            if not line:
                self.res.append(tmp)
                tmp = 0
            else:
                tmp += int(line)
        self.res.sort()
        return self.res[-1]

    @answer(212836)
    def part_2(self) -> int:
        return sum(self.res[-3:])

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
