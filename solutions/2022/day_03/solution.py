# prompt: https://adventofcode.com/2022/day/3
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 3

    @answer(7766)
    def part_1(self, res=0) -> int:
        for i in self.input:
            n = len(i) // 2
            (c,) = set(i[:n]) & set(i[n:])
            res += ord(c.lower()) - ord("a") + [1, 27][c.isupper()]
        return res

    @answer(2415)
    def part_2(self, res=0) -> int:
        for i in range(0, len(self.input), 3):
            l1, l2, l3 = self.input[i : i + 3]
            (c,) = set(l1) & set(l2) & set(l3)
            res += ord(c.lower()) - ord("a") + [1, 27][c.isupper()]
        return res
