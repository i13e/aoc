# prompt: https://adventofcode.com/2022/day/2
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 2

    @answer(12855)
    def part_1(self) -> int:
        win = {"A": "Y", "B": "Z", "C": "X"}
        draw = {"A": "X", "B": "Y", "C": "Z"}
        res = 0
        for line in self.input:
            if win[line[0]] == line[-1]:
                res += 6
            elif draw[line[0]] == line[-1]:
                res += 3
            res += ord(line[-1]) - ord("W")
        return res

    @answer(13726)
    def part_2(self) -> int:
        win = {"A": 2, "B": 3, "C": 1}
        lose = {"A": 3, "B": 1, "C": 2}
        draw = {"A": 1, "B": 2, "C": 3}
        res = 0
        for match in self.input:
            if match[-1] == "X":
                res += 0 + lose[match[0]]
            elif match[-1] == "Y":
                res += 3 + draw[match[0]]
            else:
                res += 6 + win[match[0]]
        return res
