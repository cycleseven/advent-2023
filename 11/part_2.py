import itertools
import sys


EXPANSION_FACTOR = 1_000_000


def main():
    galaxy_map = parse(sys.stdin)
    galaxies = find_galaxies(galaxy_map)
    expandables = get_expandables(galaxy_map)

    print(sum(shortest_path_length(a, b, galaxy_map, expandables) for a, b in pairs(galaxies)))


def parse(input_lines):
    return [list(line.strip()) for line in input_lines]


def get_expandables(galaxy_map):
    expandables = {'rows': set(), 'cols': set()}

    for i, row in enumerate(galaxy_map):
        if all(cell == '.' for cell in row):
            expandables['rows'].add(i)

    for i, column in enumerate(zip(*galaxy_map)):
        if all(cell == '.' for cell in column):
            expandables['cols'].add(i)

    return expandables


def find_galaxies(galaxy_map):
    return [
        (i, j)
        for i, row in enumerate(galaxy_map)
        for j, cell in enumerate(row)
        if cell == '#'
    ]


def pairs(items):
    return itertools.combinations(items, 2)


# We can be greedy since there are no obstacles to navigate around.
# Just pick the neighbour that minimises remaining manhattan distance
# to target at each step.
def shortest_path_length(a, b, galaxy_map, expandables):
    current = a
    length = 0

    while current != b:
        i1, j1 = current

        neighbours = [
            (manhattan_distance((i2, j2), b), (i2, j2))
            for i2, j2 in [(i1 - 1, j1), (i1, j1 - 1), (i1, j1 + 1), (i1 + 1, j1)]
            if 0 <= i2 < len(galaxy_map) and 0 <= j2 < len(galaxy_map[0])
        ]

        i2, j2 = sorted(neighbours)[0][1]

        additional_length = 1

        if i2 in expandables['rows']:
            additional_length *= EXPANSION_FACTOR

        if j2 in expandables['cols']:
            additional_length *= EXPANSION_FACTOR

        length += additional_length
        current = i2, j2

    return length


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


main()
