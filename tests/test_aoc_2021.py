from aoc_2021 import day1, day2, day3


def test_day1():
    seq = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert day1.solve_part1(iter(seq)) == 7
    assert day1.solve_part2(iter(seq)) == 5


def test_day2():
    seq = [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]
    part1_solution = day2.Position(horizontal=15, depth=10)
    assert day2.solve_part1(iter(seq)) == part1_solution

    part2_solution = day2.Position(15, 60)
    assert day2.solve_part2(iter(seq)) == part2_solution


def test_day3():
    seq = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    part1_solution = day3.Consumption(gamma=22, epsilon=9)
    assert day3.solve_part1(seq=iter(seq), nbits=5) == part1_solution

    part2_solution = day3.LifeSupportRating(oxygen=23, co2=10)
    assert day3.solve_part2(seq=iter(seq), nbits=5) == part2_solution
