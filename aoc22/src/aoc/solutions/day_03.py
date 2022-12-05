from aoc import utils as aoc_utils

letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]


def pt_one(line: str) -> int:
    first_half = line[: len(line) // 2]
    second_half = line[len(line) // 2 :]

    # make tuple of both halves
    first_half_tuple = set(list(first_half))
    second_half_tuple = set(list(second_half))

    # get intersection
    in_both = first_half_tuple.intersection(second_half_tuple)
    # calc points.

    letter = in_both.pop()
    return letters.index(letter) + 1


def pt_two(lines: list[str]):
    match = set(lines[0]) & set(lines[1]) & set(lines[2])
    letter = match.pop()

    return letter


def run_day_three():
    print("Day Three")

    pts_pt_one = 0
    pts_pt_two = 0

    lines = aoc_utils.read_lines_from_file("day_three.txt")
    group_lines: list[str] = []
    badge_letters: list[str] = []

    for line in lines:
        pts_pt_one += pt_one(line)
        if len(group_lines) == 3:
            badge_letters.append(pt_two(group_lines))
            group_lines = []
        group_lines.append(line.strip("\n"))
    badge_letters.append(pt_two(group_lines))

    for letter in badge_letters:
        pts_pt_two += letters.index(letter) + 1

    print("  Pt One")
    print(f"    Priority: {pts_pt_one}")

    print("  Pt Two")
    print(f"    Priority: {pts_pt_two}\n")


if __name__ == "__main__":
    run_day_three()
