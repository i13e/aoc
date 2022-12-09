# prompt: https://adventofcode.com/2022/day/9

# from typing import Tuple
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 9

    @answer(5874)
    def part_1(self) -> int:
        self.d = d = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
        seen, H, T = set(), [0, 0], [0, 0]
        seen.add((0, 0))
        for line in self.input:
            motion, step = line.split()
            dx, dy = d[motion]
            for _ in range(int(step)):
                H = [H[0] + dx, H[1] + dy]
                if H[0] == T[0] and abs(H[1] - T[1]) > 1:
                    T[1] += [-1, 1][H[1] > T[1]]
                elif H[1] == T[1] and abs(H[0] - T[0]) > 1:
                    T[0] += [-1, 1][H[0] > T[0]]
                elif abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1:
                    T[0] += [-1, 1][H[0] > T[0]]
                    T[1] += [-1, 1][H[1] > T[1]]
                seen.add(tuple(T))
        return len(seen)

    @answer(2467)
    def part_2(self) -> int:
        seen, d = set(), self.d
        knot = [[0, 0] for _ in range(10)]
        for line in self.input:
            motion, step = line.split()
            dx, dy = d[motion]
            for _ in range(int(step)):
                knot[0] = [knot[0][0] + dx, knot[0][1] + dy]
                for i in range(9):
                    H, T = knot[i], knot[i + 1]
                    if H[0] == T[0] and abs(H[1] - T[1]) > 1:
                        T[1] += [-1, 1][H[1] > T[1]]
                    elif H[1] == T[1] and abs(H[0] - T[0]) > 1:
                        T[0] += [-1, 1][H[0] > T[0]]
                    elif abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1:
                        T[0] += [-1, 1][H[0] > T[0]]
                        T[1] += [-1, 1][H[1] > T[1]]
                    else:
                        break
                seen.add(tuple(knot[9]))
        return len(seen)
