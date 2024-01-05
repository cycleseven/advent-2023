import sys

from pipes.neighbours import get_area_neighbours, get_loop_neighbours, resolve_polarity


def parse(input_lines):
    return [list(line.rstrip()) for line in input_lines]


def solve(raw_pipe_map):
    start, pipe_map = decode_start_tile(raw_pipe_map)
    loop = find_loop(pipe_map, start)
    return count_enclosed_tiles(pipe_map, loop)


# 🤢
def decode_start_tile(pipe_map):
    # Assume only one "S"
    i, j = [
        (i, j)
        for i, row in enumerate(pipe_map)
        for j, tile in enumerate(row)
        if tile == "S"
    ][0]

    valid_neighbours = {
        (i - 1, j): ["|", "F", "7"],
        (i + 1, j): ["|", "L", "J"],
        (i, j - 1): ["-", "F", "L"],
        (i, j + 1): ["-", "7", "J"],
    }

    loop_neighbours = set(
        (i, j)
        for (i, j), valid_types in valid_neighbours.items()
        if 0 <= i < len(pipe_map)
        and 0 <= j < len(pipe_map[0])
        and pipe_map[i][j] in valid_types
    )

    if len(loop_neighbours) != 2:
        raise ValueError("Starting tile is not in a strict loop")

    # 🤦
    if loop_neighbours == {(i - 1, j), (i + 1, j)}:
        start_type = "|"
    elif loop_neighbours == {(i - 1, j), (i, j - 1)}:
        start_type = "J"
    elif loop_neighbours == {(i - 1, j), (i, j + 1)}:
        start_type = "L"
    elif loop_neighbours == {(i + 1, j), (i, j - 1)}:
        start_type = "7"
    elif loop_neighbours == {(i + 1, j), (i, j + 1)}:
        start_type = "F"
    elif loop_neighbours == {(i, j - 1), (i, j + 1)}:
        start_type = "-"
    else:
        raise ValueError(
            f"Cannot identify starting tile from neighbours: {loop_neighbours}"
        )

    decoded_pipe_map = [
        [start_type if tile == "S" else tile for tile in row] for row in pipe_map
    ]

    return (i, j), decoded_pipe_map


def find_loop(pipe_map, start):
    loop = []
    prev_pipe = None
    current_pipe = start

    while len(loop) == 0 or current_pipe != start:
        loop.append(current_pipe)

        i, j = current_pipe
        next_pipes = get_loop_neighbours(pipe_map[i][j], current_pipe)

        if not prev_pipe:
            assert len(next_pipes) == 2
        else:
            next_pipes = [x for x in next_pipes if x != prev_pipe]
            assert len(next_pipes) == 1

        prev_pipe = current_pipe
        current_pipe = next_pipes[0]

    return loop


def count_enclosed_tiles(pipe_map, loop):
    top_left_corner = sorted(loop)[0]
    top_left_index = loop.index(top_left_corner)
    ordered_loop = loop[top_left_index:] + loop[:top_left_index]

    oriented_loop = [
        (top_left_corner, "F", "A")
    ]

    # Walk around the loop again to resolve the polarity of loop tiles
    for i, j in ordered_loop[1:]:
        tile_type = pipe_map[i][j]
        oriented_loop.append((
            (i, j),
            tile_type,
            resolve_polarity(
                oriented_loop[-1][1],
                oriented_loop[-1][2],
                tile_type,
            ),
        ))

    frontier = set(oriented_loop)
    enclosed_area = set()
    loop_tiles = set(loop)

    # Expand frontier to neighbouring areas
    while len(frontier) > 0:
        coord, type, polarity = frontier.pop()
        enclosed_area.add(coord)

        for neighbour in get_area_neighbours(type, polarity, coord):
            if neighbour not in enclosed_area and neighbour not in loop_tiles:
                frontier.add((neighbour, ".", None))

    return len(enclosed_area) - len(loop_tiles)


raw_pipe_mape = parse(sys.stdin)
solution = solve(raw_pipe_mape)
print(solution)
