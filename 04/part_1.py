import sys


def parse(input_line):
    _, useful_stuff = input_line.split(":")
    left_part, right_part = useful_stuff.split("|")

    return (
        set(int(x) for x in left_part.split()),
        set(int(x) for x in right_part.split()),
    )


points = 0

for line in sys.stdin:
    winning_numbers, my_numbers = parse(line)
    intersection = winning_numbers & my_numbers

    if len(intersection) == 0:
        continue

    points += 2 ** (len(intersection) - 1)

print(points)
