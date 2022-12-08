import os


def read_lines_from_file(file_name: str) -> list[str]:
    lines: str
    addit = "" if "/aoc22" in os.getcwd() else "/aoc22"
    with open(f"{os.getcwd()}{addit}/src/aoc/input/{file_name}") as f:
        lines = f.readlines()

    return lines


def get_sum_of_list(items: list[int]) -> int:
    sum: int = 0
    for item in items:
        sum += item
    return sum
