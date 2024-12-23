from __future__ import annotations

from collections.abc import Generator

def parse_numbers_split(s: str) -> list[int]:
    return [int(x) for x in s.split()]

def parse_numbers_comma(s: str) -> list[int]:
    return [int(x) for x in s.strip().split(',')]

def parse_coords_int(s: str) -> dict[tuple[int, int], int]:
    coords = {}
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            coords[(x, y)] = int(c)
    return coords

def adjacent_4(x: int, y: int) -> Generator[tuple[int, int]]:
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y


def adjacent_8(x: int, y: int) -> Generator[tuple[int, int]]:
    for y_d in (-1, 0, 1):
        for x_d in (-1, 0, 1):
            if y_d == x_d == 0:
                continue
            yield x + x_d, y + y_d
