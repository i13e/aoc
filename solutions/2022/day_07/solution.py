# prompt: https://adventofcode.com/2022/day/7

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 7

    @answer(1582412)
    def part_1(self) -> int:
        self.size, path = {}, []
        for line in self.input:
            words = line.split()
            if words[1] == "cd":
                if words[2] == "..":
                    path.pop()
                else:
                    path.append(words[2])
            elif words[0].isnumeric():
                file = int(words[0])
                for i in range(len(path)):
                    dir = path[0] + "/".join(path[1 : i + 1])
                    self.size[dir] = self.size.get(dir, 0) + file

        return sum(v for v in self.size.values() if v <= 100000)

    @answer(3696336)
    def part_2(self) -> int:
        limit = self.size["/"] - 40000000
        return min(v for v in self.size.values() if v >= limit)
