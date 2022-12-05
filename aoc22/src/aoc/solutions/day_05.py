from aoc import utils as aoc_utils
import re


def run_day_five() -> None:
    print("Day Five")

    lines = aoc_utils.read_lines_from_file("day_five.txt")
    crates_view = lines[0:8]
    instructions = lines[10:]

    pt_one_stacks: list[list] = []
    pt_two_stacks: list[list] = []

    total_stacks = int(lines[8].rstrip().split(" ").pop())

    for num in range(0, total_stacks):
        pt_one_stacks.append([])
        pt_two_stacks.append([])

    for line in crates_view:
        counter = 1
        row = 0
        stack = 0
        while counter < len(lines[0]):
            if line[counter] != " ":
                pt_one_stacks[stack].insert(0, line[row : row + 3])
                pt_two_stacks[stack].insert(0, line[row : row + 3])
            counter += 4
            row += 4
            stack += 1

    for line in instructions:
        num_list = re.findall(r"\d+", line)

        num = int(num_list[0])
        take_from = int(num_list[1])
        to = int(num_list[2])
        f = pt_one_stacks[take_from - 1]
        t = pt_one_stacks[to - 1]
        fpt = pt_two_stacks[take_from - 1]
        tpt = pt_two_stacks[to - 1]

        items = fpt[len(fpt) - num :]
        tpt.extend(items)

        for i in range(0, num):
            fpt.pop()
            item = f.pop()
            t.append(item)

    top_letters: list[str] = []
    pt_two_letters: list[str] = []

    for stack in pt_one_stacks:
        top_letters.append(stack.pop())

    for stack in pt_two_stacks:
        pt_two_letters.append(stack.pop())

    print("  Part one:")
    print("    " + "".join(top_letters))
    print("  Part two")
    print("    " + "".join(pt_two_letters) + "\n")


if __name__ == "__main__":
    run_day_five()
