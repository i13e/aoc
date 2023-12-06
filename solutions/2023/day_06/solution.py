# puzzle prompt: https://adventofcode.com/2023/day/6

from functools import reduce

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 6

    def count_wins(self, time: int, distance: int) -> int:
        return sum(t * (time - t) > distance for t in range(1, time))

    @answer(3316275)
    def part_1(self) -> int:
        races = zip(*(map(int, line.split()[1:]) for line in self.input))

        return reduce(lambda res, race: res * self.count_wins(*race), races, 1)

    @answer(27102791)
    def part_2(self) -> int:
        time, distance = [int("".join(line.split()[1:])) for line in self.input]
        return self.count_wins(time, distance)
