# prompt: https://adventofcode.com/2022/day/8

# from typing import Tuple
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 8

    @answer(1825)
    def part_1(self) -> int:
        R, C = len(self.input), len(self.input[0])
        nums, self.trees = self.input, []

        def motion(r: int, c: int, d: tuple, h: int) -> bool:
            if r in {0, R - 1} or c in {0, C - 1}:
                return True
            nr, nc = r + d[0], c + d[1]
            if nr in range(R) and nc in range(C) and h > int(nums[nr][nc]):
                return motion(nr, nc, d, h)
            return False

        for r in range(R):
            for c in range(C):
                for d in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
                    if motion(r, c, d, int(nums[r][c])):
                        self.trees.append((r, c))
                        break
        return len(self.trees)

    @answer(235200)
    def part_2(self, res=0) -> int:
        R, C = len(self.input), len(self.input[0])
        nums, trees = self.input, self.trees

        def motion(r: int, c: int, d: tuple, h: int) -> int:
            nr, nc = r + d[0], c + d[1]
            if nr in range(R) and nc in range(C):
                if h > int(nums[nr][nc]):
                    return 1 + motion(nr, nc, d, h)
                return 1
            return 0

        for r, c in trees:
            score = 1
            for d in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
                score *= motion(r, c, d, int(nums[r][c]))
            res = max(res, score)

        return res
