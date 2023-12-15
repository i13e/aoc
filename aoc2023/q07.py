from __future__ import annotations

from collections import Counter
from typing import Iterator

from aocd import data
import pytest

import support


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


INPUT_S = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
EXPECTED_1 = 6440
EXPECTED_2 = 5905


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, EXPECTED_1, EXPECTED_2),
        (str(data), 249638405, 249776650),
    ),
)
def test_d(input_s: str, expected_1: int, expected_2: int) -> None:
    if result_1 := part_1(input_s):
        assert result_1 == expected_1

    if result_2 := part_2(input_s):
        assert result_2 == expected_2


def main() -> int:
    with support.timing():
        print(part_1(str(data)))

    with support.timing():
        print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
