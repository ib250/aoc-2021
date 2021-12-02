import functools as fn
from enum import Enum
from dataclasses import dataclass, replace
from typing import Iterator, NewType, Tuple, TypedDict


@dataclass(repr=False, frozen=True)
class Position:
    horizontal: int
    depth: int

    def __repr__(self):
        return (
            f"Position({self.horizontal=}, "
            f"{self.depth=}, product={self.depth * self.horizontal})"
        )


class InstructionT(str, Enum):
    up = "up"
    down = "down"
    forward = "forward"


Instruction = Tuple[InstructionT, int]


def load_input() -> Iterator[Instruction]:
    with open("../inputs/day2/input.txt") as f:
        for intruction_t, unit_str in map(str.split, f):
            yield (InstructionT(intruction_t), int(unit_str))


def solve_part1(seq: Iterator[Instruction]) -> Position:
    def navigate(current: Position, command: Instruction) -> Position:
        type_, unit = command
        if type_ == InstructionT.forward:
            return replace(current, horizontal=current.horizontal + unit)
        if type_ == InstructionT.up:
            return replace(current, depth=current.depth - unit)
        if type_ == InstructionT.down:
            return replace(current, depth=current.depth + unit)
        raise TypeError(f"{type_} is not a valid Instruction")

    return fn.reduce(navigate, seq, Position(0, 0))


Aim = NewType("Aim", int)


class PositionWithAim(TypedDict):
    position: Position
    aim: Aim


def solve_part2(seq: Iterator[Instruction]) -> Position:
    def navigate(current: PositionWithAim, command: Instruction) -> PositionWithAim:
        type_, unit = command
        position = current["position"]
        aim = current["aim"]
        if type_ == InstructionT.forward:
            new_position = replace(
                position,
                horizontal=position.horizontal + unit,
                depth=position.depth + aim * unit,
            )
            return PositionWithAim(position=new_position, aim=aim)

        if type_ == InstructionT.up:
            return PositionWithAim(position=position, aim=Aim(aim - unit))

        if type_ == InstructionT.down:
            return PositionWithAim(position=position, aim=Aim(aim + unit))

        raise TypeError(f"{type_} is not a valid Instruction")

    init = PositionWithAim(position=Position(0, 0), aim=Aim(0))
    solution = fn.reduce(navigate, seq, init)
    return solution["position"]


if __name__ == "__main__":
    print(f"solve_part1(../inputs/day2/input.txt) == {solve_part1(load_input())}")
    print(f"solve_part2(../inputs/day2/input.txt) == {solve_part2(load_input())}")
