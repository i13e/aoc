# puzzle prompt: https://adventofcode.com/2023/day/4
from collections import Counter

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    def process_row(self, s: str) -> set[int]:
        _, win, hand = s.replace(":", "|").split("|")
        win = set(map(int, filter(str.isdigit, win.split(" "))))
        hand = set(map(int, filter(str.isdigit, hand.split(" "))))
        return win & hand

    @answer(23941)
    def part_1(self) -> int:
        return sum(
            2 ** (len(row) - 1)
            for row in map(lambda x: self.process_row(x), self.input)
            if row
        )

    @answer(5571760)
    def part_2(self) -> int:
        graph = Counter()
        for i, row in enumerate(map(lambda x: self.process_row(x), self.input)):
            for j in range(i + 1, min(len(self.input), i + 1 + len(row))):
                graph[j] += graph[i] + 1
        return sum(graph.values()) + len(self.input)

    # @answer((1234, 5678))
    # def solve(self) -> tuple[int | str, int | str]:
    #     return (0, 0)
