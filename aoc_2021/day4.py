from __future__ import annotations

import itertools
import typing as t
from dataclasses import dataclass

from aoc_2021 import input_dir


@dataclass(repr=False)
class Board:
    size: int
    contents: t.List[int]

    def __repr__(self) -> str:
        row_order_repr = ";".join(map(repr, self.column_order()))
        return f"Board(size={self.size=}, contents=({row_order_repr}))"

    def column_order(self) -> t.Iterator[t.List[int]]:
        for start in range(self.size):
            yield self.contents[start :: self.size]

    def row_order(self) -> t.Iterator[t.List[int]]:
        for start in range(self.size):
            start_ = start * self.size
            yield self.contents[start_ : start_ + self.size]

    def wins(self, calls: t.List[int]) -> bool:
        for row, col in zip(self.row_order(), self.column_order()):
            if set(row).issubset(calls):
                return True
            if set(col).issubset(calls):
                return True
        return False

    def get_current_score(self, calls: t.List[int]) -> t.Optional[int]:
        def unmarked() -> t.Iterator[int]:
            for entry in self.contents:
                if entry not in calls:
                    yield entry

        return sum(unmarked()) * calls[-1]


@dataclass
class PuzzleInput:
    draws: t.List[int]
    boards: t.List[Board]


def parse_input(seq: t.Iterator[t.Text]) -> PuzzleInput:
    draws = map(int, next(seq).strip().split(","))

    def rows(stream: t.Iterable[t.Text]) -> t.Iterator[t.Tuple[int, t.List[int]]]:
        for lines in stream:
            row = list(map(int, lines.strip().split()))
            if row:
                yield (len(row), row)

    def next_board(stream: t.Iterator[t.Tuple[int, t.List[int]]]) -> Board:
        size, first_row = next(stream)
        rest = itertools.chain.from_iterable(
            row for _, row in itertools.islice(stream, size - 1)
        )
        return Board(size=size, contents=[*first_row, *rest])

    def boards(stream: t.Iterator[t.Tuple[int, t.List[int]]]) -> t.Iterator[Board]:
        while True:
            try:
                yield next_board(stream)
            except StopIteration:
                break

    _boards = boards(rows(seq))
    return PuzzleInput(draws=list(draws), boards=list(_boards))


def win_order(p: PuzzleInput) -> t.Iterator[t.Tuple[int, Board]]:
    call_index = 0
    alread_won_index = set()
    for call_index in range(len(p.draws)):
        for ix, board in enumerate(p.boards):
            if ix not in alread_won_index and board.wins(p.draws[:call_index]):
                alread_won_index.add(ix)
                yield (call_index, board)

            if len(p.boards) == len(alread_won_index):
                return


def solve_part1(p: PuzzleInput) -> t.Optional[int]:
    if (result := next(win_order(p), None)) :
        call_index, board = result
        return board.get_current_score(p.draws[:call_index])
    return None


def solve_part2(p: PuzzleInput) -> t.Optional[int]:
    reversed_winners = reversed(list(win_order(p)))
    if (result := next(reversed_winners, None)) :
        call_index, board = result
        return board.get_current_score(p.draws[:call_index])
    return None


def load_input() -> PuzzleInput:
    with open(input_dir / "day4/input.txt") as f:
        return parse_input(f)


if __name__ == "__main__":
    print(f"solve_part1(day4/input.txt) = {solve_part1(load_input())}")
    print(f"solve_part2(day4/input.txt) = {solve_part2(load_input())}")
