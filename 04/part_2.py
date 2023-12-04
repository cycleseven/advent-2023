import sys
from collections import defaultdict


def parse(input_line):
    _, useful_stuff = input_line.split(":")
    left_part, right_part = useful_stuff.split("|")

    return (
        set(int(x) for x in left_part.split()),
        set(int(x) for x in right_part.split()),
    )


card_frequencies = defaultdict(int)

for i, line in enumerate(sys.stdin, 1):
    card_frequencies[i] += 1
    self_frequency = card_frequencies[i]

    winning_numbers, my_numbers = parse(line)
    intersection = winning_numbers & my_numbers

    for j in range(i + 1, i + len(intersection) + 1):
        card_frequencies[j] += self_frequency

print(sum(card_frequencies.values()))
