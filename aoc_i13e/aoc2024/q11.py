from aocd import data

from aoc_i13e import support

def part_1(s: str) -> int:
    numbers = support.parse_numbers_split(s)

    def _transmute(n: int) -> tuple[int, ...]:
        if n == 0:
            return (1,)
        elif len(str(n)) % 2 == 0:
            nstr = str(n)
            midp = len(nstr) // 2
            return int(nstr[:midp]), int(nstr[midp:])
        else:
            return (2024 * n,)

    for _ in range(25):
        numbers = [m for n in numbers for m in _transmute(n)]

    return len(numbers)
