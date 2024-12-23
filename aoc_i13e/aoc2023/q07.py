from collections import Counter
from typing import Iterator

from aocd import data


def get_rank(s: str, pt_1: int) -> int:
    count = Counter(s)
    if not pt_1:
        count["J"] = 0
        count[max(count, key=lambda x: count[x])] += s.count("J")

    if 5 in count.values():
        return 6
    elif 4 in count.values():
        return 5
    elif 3 in count.values():
        return 3 + int(2 in count.values())
    return sum(count == 2 for count in count.values())


def get_scores(hands: list[str], pt_1: int) -> Iterator[tuple[int, str]]:
    suits = {"T": "10", "Q": "12", "K": "13", "A": "14"}
    suits["J"] = str(pt_1) + "1"

    for hand in hands:
        hand_score = "".join(suits.get(c, "0" + c) for c in hand)
        yield (get_rank(hand, pt_1), hand_score)


def part_1(s: str) -> int:
    hands, bids = zip(*(c.split() for c in s.splitlines()))
    scores = get_scores(hands, 1)
    bids = (bid for _, bid in sorted(zip(scores, bids)))

    return sum(i * int(bid) for i, bid in enumerate(bids, 1))


def part_2(s: str) -> int:
    hands, bids = zip(*(c.split() for c in s.splitlines()))
    scores = get_scores(hands, 0)
    bids = (bid for _, bid in sorted(zip(scores, bids)))

    return sum(i * int(bid) for i, bid in enumerate(bids, 1))


def main() -> int:
    print(part_1(str(data)))
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
