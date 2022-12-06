# prompt: https://adventofcode.com/2022/day/6

# from typing import Tuple
from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2022
    _day = 6

    @answer(1134)
    def part_1(self) -> int:
        for i in range(4, len(self.input)):
            if len({*self.input[i - 4 : i]}) == 4:
                return i
        return -1

    @answer(2263)
    def part_2(self) -> int:
        for i in range(14, len(self.input)):
            if len({*self.input[i - 14 : i]}) == 14:
                return i
        return -1

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
