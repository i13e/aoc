# prompt: https://adventofcode.com/2022/day/2
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 2

    @answer(12855)
    def part_1(self, res=0) -> int:
        for i in self.input:
            res += (ord(i[-1]) - ord(i[0]) - 1) % 3 * 3
            res += ord(i[-1]) - ord("W")
        return res

    @answer(13726)
    def part_2(self, res=0) -> int:
        for i in self.input:
            res += (ord(i[-1]) + ord(i[0]) - 1) % 3 + 1
            res += (ord(i[-1]) - ord("X")) * 3
        return res
