from aoc import utils as aoc_utils


def run_day_six():
    print("Day Six")

    stream = aoc_utils.read_lines_from_file("day_six.txt")[0]

    four_chars = []
    som_chars = []
    sop_nth = 0
    som_nth = 0
    sop_found = False
    som_found = False

    for char in stream:
        if not sop_found:
            if len(four_chars) == 4:
                sop_found = True
            elif char in four_chars:
                idx = four_chars.index(char)

                four_chars = four_chars[idx + 1 :]

                four_chars.append(char)

            elif char not in four_chars:
                four_chars.append(char)

            if not sop_found:
                sop_nth += 1

        if not som_found:
            if len(som_chars) == 14:
                som_found = True
            elif char in som_chars:
                idx = som_chars.index(char)
                som_chars = som_chars[idx + 1 :]
                som_chars.append(char)
            elif char not in som_chars:
                som_chars.append(char)

            if not som_found:
                som_nth += 1

    print("  Part One")
    print("    first marker after character: ", sop_nth)

    print("  Part Two")
    print("    first marker after character: ", som_nth)
    print()


if __name__ == "__main__":
    run_day_six()
