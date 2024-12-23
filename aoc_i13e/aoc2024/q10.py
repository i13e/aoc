from __future__ import annotations

from aoc_i13e import support

def part_1(s: str) -> int:
    world = support.parse_coords_int(s)

    def _score(pos: tuple[int, int]) -> int:
        completed = set()
        todo = [(pos, 0)]
        while todo:
            pos, size = todo.pop()

            if size == 9:
                completed.add(pos)
                continue

            for coord in support.adjacent_4(*pos):
                if world.get(coord, -1) == size + 1:
                    todo.append((coord, size + 1))

        return len(completed)

    return sum(_score(k) for k, v in world.items() if v == 0)

def part_2(s: str) -> int:
    world = support.parse_coords_int(s)

    def _score(pos: tuple[int, int]) -> int:
        completed = 0
        todo = [(pos, 0)]
        while todo:
            pos, size = todo.pop()

            if size == 9:
                completed += 1
                continue

            for coord in support.adjacent_4(*pos):
                if world.get(coord, -1) == size + 1:
                    todo.append((coord, size + 1))

        return completed

    return sum(_score(k) for k, v in world.items() if v == 0)
