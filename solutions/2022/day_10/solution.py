# prompt: https://adventofcode.com/2022/day/10

# from typing import Tuple
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 10

    @answer(14860)
    def part_1(self, res=0) -> int:
        t, x = 0, 1
        for i in self.input:
            t += 1
            res += [0, x * t][not (t + 20) % 40]
            if i != "noop":
                t += 1
                res += [0, x * t][not (t + 20) % 40]
                x += int(i.split()[1])
        return res

    @answer("RGZEHURK")
    def part_2(self) -> str:
        R = [[] for _ in range(6)]
        t, x = 0, 1
        for i in self.input:
            R[t // 40].append([" ", "#"][abs(x - (t % 40)) <= 1])
            t += 1
            if i != "noop":
                R[t // 40].append([" ", "#"][abs(x - (t % 40)) <= 1])
                t += 1
                x += int(i.split()[-1])
        for r in range(6):
            print("".join(R[r]))
        return input("Enter output: ")
