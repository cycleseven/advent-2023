import sys


def parse(input_lines):
    return [list(line.rstrip()) for line in input_lines]


def solve(pipe_map):
    frontier = [
        (i, j)
        for i, row in enumerate(pipe_map)
        for j, tile in enumerate(row)
        if tile == "S"
    ]

    loop = [*frontier]

    while len(frontier) > 0:
        pipe = frontier.pop()
        next_pipes = find_next_pipes(pipe, pipe_map, loop)
        loop += next_pipes

        if len(next_pipes) > 0:
            frontier += next_pipes

    if len(loop) % 2 != 0:
        raise ValueError(f'Loop has uneven length of {len(loop)}')

    return int(len(loop) * 0.5)


def find_next_pipes(pipe, pipe_map, loop):
    i, j = pipe
    pipe_type = pipe_map[i][j]

    if pipe_type == 'S':
        valid_neighbours = {
            (i - 1, j): ['|', 'F', '7'],
            (i + 1, j): ['|', 'L', 'J'],
            (i, j - 1): ['-', 'F', 'L'],
            (i, j + 1): ['-', '7', 'J'],
        }

        discovered_neighbours = [
            (i, j)
            for (i, j), valid_types in valid_neighbours.items()
            if 0 <= i < len(pipe_map) and 0 <= j < len(pipe_map[0]) and pipe_map[i][j] in valid_types
        ]

        if len(discovered_neighbours) != 2:
            raise ValueError('Starting tile is not in a strict loop')

        return discovered_neighbours

    # Assume loop never goes out of bounds
    if pipe_type == '|':
        neighbours = [(i - 1, j), (i + 1, j)]
    elif pipe_type == '-':
        neighbours = [(i, j - 1), (i, j + 1)]
    elif pipe_type == 'L':
        neighbours = [(i - 1, j), (i, j + 1)]
    elif pipe_type == 'J':
        neighbours = [(i - 1, j), (i, j - 1)]
    elif pipe_type == '7':
        neighbours = [(i, j - 1), (i + 1, j)]
    elif pipe_type == 'F':
        neighbours = [(i + 1, j), (i, j + 1)]
    else:
        raise ValueError(f'Invalid pipe type "{pipe_type}"')

    # My algorithm is not as fast as it could be. Probably because of this bit,
    # since we iterate over the entire loop for the "not in" check.
    #
    # Part 2 uses a faster algorithm to find the loop but I can't be bothered updating
    # part 1 to match it lol
    discovered_neighbours = [tile for tile in neighbours if tile not in loop]

    if len(discovered_neighbours) > 1:
        raise ValueError(f'Invalid neighbours "{discovered_neighbours}" for loop "{loop}"')

    return discovered_neighbours


pipe_map = parse(sys.stdin)
solution = solve(pipe_map)
print(solution)
