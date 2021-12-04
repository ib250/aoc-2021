import itertools
from typing import Iterator, Tuple


def load_input() -> Iterator[int]:
    with open("../inputs/day1/part1.txt") as f:
        for line in f:
            yield int(line)


def count_increases(seq: Iterator[int]) -> int:
    fst, snd = itertools.tee(seq)
    next(snd)
    count = 0
    for before, after in zip(fst, snd):
        if after > before:
            count += 1
    return count


def solve_part1(seq: Iterator[int]) -> int:
    return count_increases(seq)


def solve_part2(seq: Iterator[int]) -> int:
    def make_three_bin_sum(seq_in: Iterator[int]) -> Iterator[int]:
        fst, snd, trd = itertools.tee(seq_in, 3)
        next(snd)
        next(trd)
        next(trd)
        for x1, x2, x3 in zip(fst, snd, trd):
            yield x1 + x2 + x3

    return count_increases(make_three_bin_sum(seq))


if __name__ == "__main__":
    print(f"solve_part1(inputs/day1.txt) = {solve_part1(load_input())}")
    print(f"solve_part2(inputs/day1.txt) = {solve_part2(load_input())}")
