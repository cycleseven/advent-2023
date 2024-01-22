# Inefficient and stinky code

import sys
from itertools import product


def main():
    num_arrangements = 0

    for line in sys.stdin:
        print(line.strip())
        row, group_sizes = parse_line(line)
        possible_arrangements = count_possible_arrangements(row, group_sizes)
        print(possible_arrangements)
        print()
        num_arrangements += possible_arrangements

    print(num_arrangements)


def parse_line(line):
    left, right = line.split()
    row = list(left)
    group_sizes = [int(x) for x in right.split(',')]

    return row, group_sizes


def count_possible_arrangements(row, groups):
    n = len([x for x in row if x == '?'])
    valid_arrangements = 0

    # TODO: product() is a list of size 2^n where most candidates will clearly
    # not fit the group constraint, I'm certain this is nowhere near optimal
    for candidate in product('#.', repeat=n):
        arrangement = create_arrangement(row, candidate)

        if count_contiguous_groups(arrangement) == groups:
            valid_arrangements += 1

    return valid_arrangements


def create_arrangement(row, candidate):
    arrangement = []
    wildcard_index = 0

    for indicator in row:
        if indicator == '?':
            arrangement.append(candidate[wildcard_index])
            wildcard_index += 1
        else:
            arrangement.append(indicator)

    return arrangement


def count_contiguous_groups(row):
    groups = []

    for prev, next in zip([None, *row], [*row, None]):
        if prev != '#' and next == '#':
            groups.append(1)
        elif next == '#':
            groups[-1] += 1

    return groups


main()
