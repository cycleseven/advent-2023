import itertools
import sys


def main():
    raw_galaxy_map = parse(sys.stdin)
    expanded_galaxy_map = expand_cosmos(raw_galaxy_map)
    galaxies = find_galaxies(expanded_galaxy_map)

    print(sum(len(shortest_path(a, b, expanded_galaxy_map)) for a, b in pairs(galaxies)))


def parse(input_lines):
    return [list(line.strip()) for line in input_lines]


def expand_cosmos(galaxy_map):
    expanded_rows = []

    for row in galaxy_map:
        if all(cell == '.' for cell in row):
            expanded_rows += [row, row]
        else:
            expanded_rows.append(row)

    expanded_columns = []
    for column in zip(*expanded_rows):
        if all(cell == '.' for cell in column):
            expanded_columns += [column, column]
        else:
            expanded_columns.append(column)

    return list(zip(*expanded_columns))


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
def shortest_path(a, b, galaxy_map):
    path = [a]

    while path[-1] != b:
        i1, j1 = path[-1]
        neighbours = [
            (manhattan_distance((i2, j2), b), (i2, j2))
            for i2, j2 in [(i1 - 1, j1), (i1, j1 - 1), (i1, j1 + 1), (i1 + 1, j1)]
            if 0 <= i2 < len(galaxy_map) and 0 <= j2 < len(galaxy_map[0])
        ]
        path.append(sorted(neighbours)[0][1])

    return path[1:]


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


main()
