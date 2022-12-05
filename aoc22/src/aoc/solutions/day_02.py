from aoc import utils as aoc_utils


my_pick_points = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
result_points = {"L": 0, "D": 3, "W": 6}


def add_points(result: str, hand: str):
    points = 0
    points += my_pick_points[hand]
    points += result_points[result]

    # print(f"Adding {points} for {result} with {hand}")

    return points


def run_day_two() -> None:
    print("Day 2")

    # Part one
    pt_one_scores = {"AY": "W", "AZ": "L", "BX": "L", "BZ": "W", "CX": "W", "CY": "L"}
    pt_one_pts = 0

    # Part two
    result_mapper = {"X": "L", "Y": "D", "Z": "W"}
    picks_no_draw = {"AW": "Y", "AL": "Z", "BW": "Z", "BL": "X", "CW": "X", "CL": "Y"}
    pt_two_pts = 0

    lines = aoc_utils.read_lines_from_file("day_two.txt")
    for line in lines:
        # Prep
        line = line.replace("\n", "")
        split_line = line.split(" ")
        player = split_line[1]
        opponent = split_line[0]

        # Pt One
        result = (
            "D"
            if not line.replace(" ", "") in list(pt_one_scores.keys())
            else pt_one_scores[line.replace(" ", "")]
        )
        pt_one_pts += add_points(result, player)

        # Pt Two
        ## pt 2
        result_to_check = split_line[1]
        result = result_mapper[result_to_check]

        try:
            hand = picks_no_draw[f"{opponent}{result}"]
        except KeyError:
            hand = opponent

        pt_two_pts += add_points(result, hand)

    print("  Part one")
    print(f"    Total points: {pt_one_pts}\n")

    print("  Part two")
    print(f"    Total points: {pt_two_pts}\n")


if __name__ == "__main__":
    run_day_two()
