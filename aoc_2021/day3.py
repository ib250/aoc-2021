import itertools
from dataclasses import dataclass
from typing import Callable, Iterator, TypedDict, Counter


@dataclass(repr=False)
class Consumption:
    gamma: int
    epsilon: int

    def __repr__(self) -> str:
        return (
            f"Consumption({self.gamma=}, "
            f"{self.epsilon=}, consumption="
            f"{self.gamma * self.epsilon})"
        )


BitSequence = str


def transpose(seq: Iterator[BitSequence], nbits: int) -> Iterator[BitSequence]:
    as_string = "".join(seq)
    for position in range(nbits):
        yield as_string[position::nbits]


def get_gamma_epsilon(seq: Iterator[Counter[str]]) -> Iterator[BitSequence]:
    def seq_() -> Iterator[BitSequence]:
        for c in seq:
            (gamma_bit, _), *rest = c.most_common()
            if rest:
                epsilon_bit, _ = rest[-1]
                yield f"{gamma_bit}{epsilon_bit}"
            else:
                yield f"{gamma_bit}{'1' if gamma_bit == '0' else '0'}"

    return transpose(seq_(), nbits=2)


def solve_part1(*, nbits: int, seq: Iterator[BitSequence]) -> Consumption:
    counts = map(Counter[str], transpose(seq, nbits=nbits))
    gamma, epsilon = get_gamma_epsilon(counts)
    return Consumption(gamma=int(gamma, base=2), epsilon=int(epsilon, base=2))


@dataclass(repr=False)
class LifeSupportRating:
    oxygen: int
    co2: int

    def __repr__(self) -> str:
        return (
            f"LifeSupportRating({self.oxygen=}, "
            f"{self.co2=}, rating={self.oxygen * self.co2})"
        )


BitFilter = Callable[[Counter[str], int, BitSequence], bool]


def get_counter_at_position(*, seq: Iterator[BitSequence], nbits: int, position: int) -> Counter[str]:
    slice_ = list(transpose(seq, nbits=nbits))[position]
    return Counter[str](slice_)


def seive(
    readings: Iterator[BitSequence], *, nbits: int, filter_: BitFilter
) -> Iterator[BitSequence]:
    items = list(readings)
    for position in range(nbits):
        counter = get_counter_at_position(
            seq=iter(items), nbits=nbits, position=position
        )
        if any(filter_(counter, position, item) for item in items):
            items = [
                reading for reading in items if filter_(counter, position, reading)
            ]

    return iter(items)


def co2_filter(counter: Counter[str], position: int, s: BitSequence) -> bool:
    if counter.get("0") == counter.get("1"):
        return s[position] == "0"
    *_, (least_common_bit, _) = counter.most_common()
    return s[position] == least_common_bit


def oxygen_filter(counter: Counter[str], position: int, s: BitSequence) -> bool:
    if counter.get("0") == counter.get("1"):
        return s[position] == "1"
    (most_common_bit, _), *_ = counter.most_common()
    return s[position] == most_common_bit


def filter_oxygen_reading(
    readings: Iterator[BitSequence], *, nbits: int
) -> BitSequence:
    solution = seive(readings, nbits=nbits, filter_=oxygen_filter)
    return next(solution)


def filter_co2_reading(readings: Iterator[BitSequence], *, nbits: int) -> BitSequence:
    solution = seive(readings, nbits=nbits, filter_=co2_filter)
    return next(solution)


def solve_part2(*, seq: Iterator[BitSequence], nbits: int) -> LifeSupportRating:
    r1, r2 = itertools.tee(seq)
    co2 = filter_co2_reading(r2, nbits=nbits)
    oxygen = filter_oxygen_reading(r1, nbits=nbits)
    return LifeSupportRating(oxygen=int(oxygen, base=2), co2=int(co2, base=2))


class FixedSizeBitSequence(TypedDict):
    nbits: int
    seq: Iterator[BitSequence]


def load_input() -> FixedSizeBitSequence:
    def iter_() -> Iterator[str]:
        with open("../inputs/day3/input.txt") as f:
            for line in f:
                yield line.strip()

    fst = next(iter_())
    return {"nbits": len(fst), "seq": iter_()}


if __name__ == "__main__":
    print(f"solve_part1(day3/input.txt) == {solve_part1(**load_input())}")
    print(f"solve_part2(day3/input.txt) == {solve_part2(**load_input())}")
