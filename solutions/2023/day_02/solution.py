# puzzle prompt: https://adventofcode.com/2023/day/2
from functools import reduce

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    def get_data(self, s: str) -> tuple:
        color = next(c for c in "grb" if c in s)
        number = int("".join(filter(str.isdigit, s)))
        return color, number

    def parse_input(self, s: str) -> list[str]:
        return s.replace(";", ",").replace(":", ",").split(",")[1:]

    @answer(1734)
    def part_1(self) -> int:
        COLORS = {"r": 12, "g": 13, "b": 14}
        res = 0
        for i, line in enumerate(self.input, 1):
            game = map(lambda x: self.get_data(x), self.parse_input(line))
            res += i * all(n <= COLORS[c] for c, n in game)
        return res

    @answer(70387)
    def part_2(self) -> int:
        res = 0
        for line in self.input:
            COLORS = {"r": 0, "g": 0, "b": 0}
            for game in map(lambda x: self.get_data(x), self.parse_input(line)):
                COLORS[game[0]] = max(COLORS[game[0]], game[1])
            res += reduce(lambda a, b: a * b, COLORS.values())

        return res

    # @answer((1234, 5678))
    # def solve(self) -> tuple[int | str, int | str]:
    #     return (0, 0)
