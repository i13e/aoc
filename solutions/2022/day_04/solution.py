# prompt: https://adventofcode.com/2022/day/4

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 4

    @answer(503)
    def part_1(self, res=0) -> int:
        for pair in self.input:
            one, two = pair.split(",")
            s1, e1 = one.split("-")
            s2, e2 = two.split("-")
            r1 = set(range(int(s1), int(e1) + 1))
            r2 = set(range(int(s2), int(e2) + 1))
            if r1 <= r2 or r1 >= r2:
                res += 1
        return res

    @answer(827)
    def part_2(self, res=0) -> int:
        for pair in self.input:
            one, two = pair.split(",")
            s1, e1 = one.split("-")
            s2, e2 = two.split("-")
            r1 = set(range(int(s1), int(e1) + 1))
            r2 = set(range(int(s2), int(e2) + 1))
            if r1 & r2:
                res += 1
        return res
