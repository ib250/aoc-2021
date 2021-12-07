from aoc_2021 import day1, day2, day3, day4, input_dir


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


def test_day4_input_parser():

    day4_example = day4.PuzzleInput(
        draws=[
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ],
        boards=[
            day4.Board(
                size=5,
                contents=[
                    22,
                    13,
                    17,
                    11,
                    0,
                    8,
                    2,
                    23,
                    4,
                    24,
                    21,
                    9,
                    14,
                    16,
                    7,
                    6,
                    10,
                    3,
                    18,
                    5,
                    1,
                    12,
                    20,
                    15,
                    19,
                ],
            ),
            day4.Board(
                size=5,
                contents=[
                    3,
                    15,
                    0,
                    2,
                    22,
                    9,
                    18,
                    13,
                    17,
                    5,
                    19,
                    8,
                    7,
                    25,
                    23,
                    20,
                    11,
                    10,
                    24,
                    4,
                    14,
                    21,
                    16,
                    12,
                    6,
                ],
            ),
            day4.Board(
                size=5,
                contents=[
                    14,
                    21,
                    17,
                    24,
                    4,
                    10,
                    16,
                    15,
                    9,
                    19,
                    18,
                    8,
                    23,
                    26,
                    20,
                    22,
                    11,
                    13,
                    6,
                    5,
                    2,
                    0,
                    12,
                    3,
                    7,
                ],
            ),
        ],
    )
    with open(input_dir / "day4/example.txt") as f:
        assert day4.parse_input(f) == day4_example, day4_example.boards[0]

    assert day4.solve_part1(day4_example) == 4512
    assert day4.solve_part2(day4_example) == 1924
