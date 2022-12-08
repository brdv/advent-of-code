from aoc import utils as aoc_utils


def run_day_eight() -> None:
    print("============================================================")
    print("Day Eight")

    lines = [l.rstrip() for l in aoc_utils.read_lines_from_file("day_eight.txt")]
    dlist: list[list[int]] = []

    h = len(lines)
    w = len(lines[1])
    total_visible = 0
    top_scenic = 0

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            tree = lines[y][x]
            ftop = [lines[i][x] for i in range(y)[::-1]]
            fleft = list(lines[y][:x][::-1])
            fright = list(lines[y][x + 1 :])
            fbot = [lines[i][x] for i in range(y + 1, h)]
            mtop = max(ftop)
            mleft = max(fleft)
            mright = max(fright)
            mbot = max(fbot)

            if mtop < tree or mleft < tree or mright < tree or mbot < tree:
                total_visible += 1
                scenes = [0, 0, 0, 0]
                for t in ftop:
                    scenes[0] = scenes[0] + 1
                    if t >= tree:
                        break
                for t in fleft:
                    scenes[1] = scenes[1] + 1
                    if t >= tree:
                        break
                for t in fright:
                    scenes[2] = scenes[2] + 1
                    if t >= tree:
                        break
                for t in fbot:
                    scenes[3] = scenes[3] + 1
                    if t >= tree:
                        break

                scene_score = scenes[0] * scenes[1] * scenes[2] * scenes[3]
                top_scenic = max(top_scenic, scene_score)

    total_visible = total_visible + h * 2 + (w - 2) * 2
    print("  Part One:")
    print("    Total trees visible: ", total_visible)
    print("  Part Two:")
    print("    Top scenic score: ", top_scenic)
    print()


if __name__ == "__main__":
    run_day_eight()
