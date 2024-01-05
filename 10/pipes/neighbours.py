# I have a strong feeling there's a way simpler solution for the area
# inside a loop, probably a maths-y one.
# Gone for this horrible grind instead where the neighbouring tiles
# are enumerated for each different pipe type.
# The "polarity" (A vs B) represents where the "inside" of the loop
# is relative to the pipe
_neighbour_maps = {
    "F": {
        "loop_neighbours": [
            [".", ".", "."],
            [".", "F", "o"],
            [".", "o", "."],
        ],
        "area_neighbours": {
            "A": [
                [".", ".", "."],
                [".", "F", "o"],
                [".", "o", "o"],
            ],
            "B": [
                ["o", "o", "o"],
                ["o", "F", "o"],
                ["o", "o", "."],
            ],
        },
    },
    "7": {
        "loop_neighbours": [
            [".", ".", "."],
            ["o", "7", "."],
            [".", "o", "."],
        ],
        "area_neighbours": {
            "A": [
                [".", ".", "."],
                ["o", "7", "."],
                ["o", "o", "."],
            ],
            "B": [
                ["o", "o", "o"],
                ["o", "7", "o"],
                [".", "o", "o"],
            ],
        },
    },
    "L": {
        "loop_neighbours": [
            [".", "o", "."],
            [".", "L", "o"],
            [".", ".", "."],
        ],
        "area_neighbours": {
            "A": [
                [".", "o", "o"],
                [".", "L", "o"],
                [".", ".", "."],
            ],
            "B": [
                ["o", "o", "."],
                ["o", "L", "o"],
                ["o", "o", "o"],
            ],
        },
    },
    "J": {
        "loop_neighbours": [
            [".", "o", "."],
            ["o", "J", "."],
            [".", ".", "."],
        ],
        "area_neighbours": {
            "A": [
                ["o", "o", "."],
                ["o", "J", "."],
                [".", ".", "."],
            ],
            "B": [
                [".", "o", "o"],
                ["o", "J", "o"],
                ["o", "o", "o"],
            ],
        },
    },
    "|": {
        "loop_neighbours": [
            [".", "o", "."],
            [".", "|", "."],
            [".", "o", "."],
        ],
        "area_neighbours": {
            "A": [
                ["o", "o", "."],
                ["o", "|", "."],
                ["o", "o", "."],
            ],
            "B": [
                [".", "o", "o"],
                [".", "|", "o"],
                [".", "o", "o"],
            ],
        },
    },
    "-": {
        "loop_neighbours": [
            [".", ".", "."],
            ["o", "-", "o"],
            [".", ".", "."],
        ],
        "area_neighbours": {
            "A": [
                ["o", "o", "o"],
                ["o", "-", "o"],
                [".", ".", "."],
            ],
            "B": [
                [".", ".", "."],
                ["o", "-", "o"],
                ["o", "o", "o"],
            ],
        },
    },
    ".": {
        "area_neighbours": [
            ["o", "o", "o"],
            ["o", ".", "o"],
            ["o", "o", "o"],
        ],
    },
}

_polarity_map = {
    "F": {
        "-": {"A": "B", "B": "A"},
        "|": {"A": "B", "B": "A"},
        "7": {"A": "A", "B": "B"},
        "L": {"A": "A", "B": "B"},
        "J": {"A": "B", "B": "A"},
    },
    "7": {
        "-": {"A": "B", "B": "A"},
        "|": {"A": "A", "B": "B"},
        "F": {"A": "A", "B": "B"},
        "L": {"A": "B", "B": "A"},
        "J": {"A": "A", "B": "B"},
    },
    "L": {
        "-": {"A": "A", "B": "B"},
        "|": {"A": "B", "B": "A"},
        "F": {"A": "A", "B": "B"},
        "7": {"A": "B", "B": "A"},
        "J": {"A": "A", "B": "B"},
    },
    "J": {
        "-": {"A": "A", "B": "B"},
        "|": {"A": "A", "B": "B"},
        "F": {"A": "B", "B": "A"},
        "7": {"A": "A", "B": "B"},
        "L": {"A": "A", "B": "B"},
    },
    "-": {
        "-": {"A": "A", "B": "B"},
        "F": {"A": "B", "B": "A"},
        "7": {"A": "B", "B": "A"},
        "L": {"A": "A", "B": "B"},
        "J": {"A": "A", "B": "B"},
    },
    "|": {
        "|": {"A": "A", "B": "B"},
        "F": {"A": "B", "B": "A"},
        "7": {"A": "A", "B": "B"},
        "L": {"A": "B", "B": "A"},
        "J": {"A": "A", "B": "B"},
    },
}


def _parse_neighbour_map(neighbour_map, center):
    center_i, center_j = center
    i_range = [center_i - 1, center_i, center_i + 1]
    j_range = [center_j - 1, center_j, center_j + 1]

    neighbours = []

    for a, i in zip(range(3), i_range):
        for b, j in zip(range(3), j_range):
            if neighbour_map[a][b] == "o":
                neighbours.append((i, j))

    return neighbours


def get_loop_neighbours(tile_type, coord):
    neighbour_map = _neighbour_maps[tile_type]["loop_neighbours"]
    return _parse_neighbour_map(neighbour_map, coord)


def get_area_neighbours(tile_type, polarity, coord):
    if tile_type == ".":
        neighbour_map = _neighbour_maps['.']["area_neighbours"]
    else:
        neighbour_map = _neighbour_maps[tile_type]["area_neighbours"][polarity]

    return _parse_neighbour_map(neighbour_map, coord)


def resolve_polarity(prev_tile_type, prev_polarity, next_tile_type):
    return _polarity_map[prev_tile_type][next_tile_type][prev_polarity]
