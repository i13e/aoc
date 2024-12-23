import re

def mul(x: int, y: int) -> int:
    return x * y

def part_1(s: str):
    res = 0
    for line in s.splitlines():
        pattern = r"mul\(\d+,\s*\d+\)"
        matches = re.findall(pattern, line)
        for m in matches:
            res += eval(m)
    return res


def part_2(s: str):
    res = 0
    ctx = 1
    for line in s.splitlines():
        pattern = r"mul\(\d+,\s*\d+\)|do\(\)|don\'t\(\)"
        matches = re.findall(pattern, line)
        for m in matches:
            if m == "do()":
                ctx = 1
            elif m == "don't()":
                ctx = 0
            elif ctx:
                res += eval(m)
    return res

