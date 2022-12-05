from aoc import utils as aoc_utils


def run_day_one() -> None:
    print("Day One")

    lines = aoc_utils.read_lines_from_file("day_one.txt")
    current_elf_items: list[int] = []
    groups_sum: list[int] = []

    for line in lines:
        if line == "\n":
            sum = aoc_utils.get_sum_of_list(current_elf_items)
            groups_sum.append(sum)
            current_elf_items = []
            continue
        current_elf_items.append(int(line))
    sum = aoc_utils.get_sum_of_list(current_elf_items)
    groups_sum.append(sum)

    groups_sum.sort(reverse=True)

    print("  Part one")
    print(f"    Biggest sum is: {groups_sum[0]}\n")

    pt_two_sum = 0
    for idx in range(0, 3):
        pt_two_sum += groups_sum[idx]

    print("  Part two")
    print(f"    The sum of three biggest is: {pt_two_sum}\n")


if __name__ == "__main__":
    run_day_one()
