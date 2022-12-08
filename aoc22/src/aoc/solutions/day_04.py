from aoc import utils as aoc_utils


def get_range_of_elf(elf: str) -> set:
    split = elf.split("-")
    start = int(split[0])
    end = int(split[1])
    r: list[int] = []
    for num in range(start, end + 1):
        r.append(num)

    return set(r)


def run_day_four() -> None:
    print("============================================================")
    print("Day Four")

    total_subsets = 0
    total_overlaps = 0

    lines = aoc_utils.read_lines_from_file("day_four.txt")

    for line in lines:
        line = line.rstrip()
        split_line = line.split(",")
        elf1 = split_line[0]
        elf2 = split_line[1]

        elf1_range: set[int] = get_range_of_elf(elf1)
        elf2_range: set[int] = get_range_of_elf(elf2)

        # Pt One
        if elf1_range.issubset(elf2_range) or elf1_range.issuperset(elf2_range):
            total_subsets += 1

        # Pt Two
        if len(elf1_range.intersection(elf2_range)) != 0:
            total_overlaps += 1

    print("  Part One")
    print(f"    Total subsets: {total_subsets}")

    print("  Part Two")
    print(f"    Total overlaps: {total_overlaps}")
    print()


if __name__ == "__main__":
    run_day_four()
