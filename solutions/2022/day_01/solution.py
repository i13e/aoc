# prompt: https://adventofcode.com/2022/day/1
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 1

    @answer(74394)
    def part_1(self) -> int:
        self.res, elf = [], 0
        for cal in self.input:
            if cal:
                elf += int(cal)
            else:
                self.res.append(elf)
                elf = 0
        self.res.sort()
        return self.res[-1]

    @answer(212836)
    def part_2(self) -> int:
        return sum(self.res[-3:])
