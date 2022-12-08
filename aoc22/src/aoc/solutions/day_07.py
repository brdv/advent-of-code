from aoc import utils as aoc_utils


class Directory:
    def __init__(self, name: str, parent: "Directory|None" = None) -> None:
        self.name: str = name
        self.parent: "Directory" = parent
        self.files: list[int] = []
        self.subdirs: list["Directory"] = []

    def total_size(self) -> int:
        file_sum = sum(self.files)

        sum_of_sub = sum([x.total_size() for x in self.subdirs])

        return file_sum + sum_of_sub


def run_day_seven():
    print("============================================================")
    print("Day Seven")

    lines = aoc_utils.read_lines_from_file("day_seven.txt")

    current_dir: Directory = None
    all_dirs: list[Directory] = []

    for line in lines:
        if line.startswith("dir") or line.startswith("$ ls"):
            continue
        if line.startswith("$ cd"):
            _, cmd, to = line.split(" ")
            to = to.rstrip()

            if current_dir is None:
                current_dir = Directory("/")
                all_dirs.append(current_dir)

            if to == "..":
                current_dir = current_dir.parent
            else:
                new_dir = Directory(to, current_dir)
                current_dir.subdirs.append(new_dir)
                all_dirs.append(new_dir)
                current_dir = new_dir

        else:
            current_dir.files.append(int(line.split(" ")[0]))

    del all_dirs[0]

    total = sum([x.total_size() for x in all_dirs if x.total_size() <= 100_000])
    print("  Part One")
    print("    Sum of dirs: ", total)

    total_space = 70_000_000
    needed_space = 30_000_000
    space_left = total_space - all_dirs[0].total_size()
    to_free = needed_space - space_left

    options = [dir.total_size() for dir in all_dirs if dir.total_size() >= to_free]
    best_option = min(options)

    print("  Part Two")
    print("    Size of best option:", best_option)
    print()


if __name__ == "__main__":
    run_day_seven()
