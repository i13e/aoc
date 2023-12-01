# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    def parse(self, s: str, part_2: bool = False) -> int:
        words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for i, word in enumerate(words * part_2, 1):
            s = s.replace(word, f"{word[0]}{i}{word[-1]}")

        a = b = ""
        for c in filter(str.isdigit, s):
            a, b = a or c, c
        return int(a + b)

    @answer(54304)
    def part_1(self) -> int:
        return sum(self.parse(line) for line in self.input)

    @answer(54418)
    def part_2(self) -> int:
        return sum(self.parse(line, True) for line in self.input)

    # @answer((1234, 5678))
    # def solve(self) -> tuple[int | str, int | str]:
    #     return (0, 0)
