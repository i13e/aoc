from collections import defaultdict

from aocd import data


Range = tuple[int, int]


def get_maps(lines: list[str]) -> dict[int, dict[Range, Range]]:
    maps = defaultdict(dict)
    key = 0
    for line in filter(lambda x: ":" not in x, lines[2:]):
        if line:
            line = list(map(int, line.split()))
            dst = (line[0], line[0] + line[2])
            src = (line[1], line[1] + line[2])
            maps[key][src] = dst
        else:
            key += 1
    return maps


def part_1(s: str) -> int:
    lines = s.splitlines()
    seeds = list(map(int, lines[0].split()[1:]))
    maps = get_maps(lines)
    for ranges in maps.values():
        for i, seed in enumerate(seeds):
            for src, dst in ranges.items():
                if seed in range(*src):
                    seeds[i] = seed - src[0] + dst[0]
    return min(seeds)


def part_2(s: str) -> int:
    lines = s.splitlines()
    seeds = list(map(int, lines[0].split()[1:]))
    seeds = [[s, s + e] for s, e in zip(seeds[::2], seeds[1::2])]
    maps = get_maps(lines)

    for ranges in maps.values():
        for i, (start, end) in enumerate(seeds):
            for src, dst in ranges.items():
                if start in range(*src):
                    if end not in range(*src):
                        seeds.append([src[1], end])
                    seeds[i][0] = start - src[0] + dst[0]
                    seeds[i][1] = min(end - src[1], 0) + dst[1]

    return min(seeds)[0]


def main() -> int:
    print(part_1(str(data)))
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
