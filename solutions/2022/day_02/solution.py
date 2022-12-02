# prompt: https://adventofcode.com/2022/day/2
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 2

    @answer(12855)
    def part_1(self) -> int:
        res, nums = 0, [1, 2, 3]
        for match in self.input:
            if ord(match[-1]) - ord(match[0]) in {22, 25}:
                res += 0 + nums[ord(match[0]) - ord("B")]
            elif ord(match[-1]) - ord(match[0]) == 23:
                res += 3 + nums[ord(match[0]) - ord("A")]
            else:
                res += 6 + nums[ord(match[0]) - ord("C")]
        return res

    @answer(13726)
    def part_2(self) -> int:
        res, nums = 0, [1, 2, 3]
        for match in self.input:
            if match[-1] == "X":
                res += 0 + nums[ord(match[0]) - ord("B")]
            elif match[-1] == "Y":
                res += 3 + nums[ord(match[0]) - ord("A")]
            else:
                res += 6 + nums[ord(match[0]) - ord("C")]
        return res
