from aocd import data


def parse(s: str, part_2: bool = False) -> int:
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, word in enumerate(words * part_2, 1):
        s = s.replace(word, f"{word[0]}{i}{word[-1]}")

    a = b = ""
    for c in filter(str.isdigit, s):
        a, b = a or c, c
    return int(a + b)


def part_1(s: str) -> int:
    return sum(parse(line) for line in s.splitlines())


def part_2(s: str) -> int:
    return sum(parse(line, True) for line in s.splitlines())


def main() -> int:
    print(part_1(str(data)))

    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
