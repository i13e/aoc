# prompt: https://adventofcode.com/2022/day/4

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 4

    @answer(503)
    def part_1(self, res=0) -> int:
        for pair in self.input:
            one, two = pair.split(",")
            s1, e1 = (int(c) for c in one.split("-"))
            s2, e2 = (int(c) for c in two.split("-"))
            if s1 <= s2 <= e2 <= e1 or s2 <= s1 <= e1 <= e2:
                res += 1
        return res

    @answer(827)
    def part_2(self, res=0) -> int:
        for pair in self.input:
            one, two = pair.split(",")
            s1, e1 = (int(c) for c in one.split("-"))
            s2, e2 = (int(c) for c in two.split("-"))
            if s2 <= e1 and s1 <= e2:
                res += 1
        return res
