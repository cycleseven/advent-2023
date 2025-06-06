import sys


def solve():
    contraption_map = [list(line.strip()) for line in sys.stdin.readlines() if not line.isspace()]

    def in_bounds(location):
        i, j = location
        return 0 <= i < len(contraption_map) and 0 <= j < len(contraption_map[0])

    def count_energized_tiles(initial_beam_head):
        energized_locations = set()
        beam_history = set()
        beam_heads = [initial_beam_head]

        while len(beam_heads) > 0:
            beam_head = beam_heads.pop(0)

            if (beam_head["location"], beam_head["next_delta"]) in beam_history:
                continue
            else:
                beam_history.add((beam_head["location"], beam_head["next_delta"]))

            next_location = (
                beam_head["location"][0] + beam_head["next_delta"][0],
                beam_head["location"][1] + beam_head["next_delta"][1],
            )

            if not in_bounds(next_location):
                continue

            next_contraption_element = contraption_map[next_location[0]][next_location[1]]

            if next_contraption_element == "|" and beam_head["next_delta"][0] == 0 and beam_head["next_delta"][1] != 0:
                beam_heads.append({"location": next_location, "next_delta": (-1, 0)})
                beam_heads.append({"location": next_location, "next_delta": (1, 0)})
            elif next_contraption_element == "-" and beam_head["next_delta"][0] != 0 and beam_head["next_delta"][1] == 0:
                beam_heads.append({"location": next_location, "next_delta": (0, -1)})
                beam_heads.append({"location": next_location, "next_delta": (0, 1)})
            elif next_contraption_element == "\\":
                if beam_head["next_delta"] == (0, 1):
                    next_delta = (1, 0)
                elif beam_head["next_delta"] == (0, -1):
                    next_delta = (-1, 0)
                elif beam_head["next_delta"] == (1, 0):
                    next_delta = (0, 1)
                elif beam_head["next_delta"] == (-1, 0):
                    next_delta = (0, -1)
                else:
                    raise ValueError(f"Invalid delta {beam_head['next_delta']}")

                beam_heads.append({
                    "location": next_location,
                    "next_delta": next_delta
                })
            elif next_contraption_element == "/":
                if beam_head["next_delta"] == (0, 1):
                    next_delta = (-1, 0)
                elif beam_head["next_delta"] == (0, -1):
                    next_delta = (1, 0)
                elif beam_head["next_delta"] == (1, 0):
                    next_delta = (0, -1)
                elif beam_head["next_delta"] == (-1, 0):
                    next_delta = (0, 1)
                else:
                    raise ValueError(f"Invalid delta {beam_head['next_delta']}")

                beam_heads.append({
                    "location": next_location,
                    "next_delta": next_delta
                })
            else:
                beam_heads.append({
                    "location": next_location,
                    "next_delta": beam_head["next_delta"]
                })

            energized_locations.add(next_location)

        return len(energized_locations)

    initial_beam_heads = [
        *[
            {"location": (-1, j), "next_delta": (1, 0)}
            for j in range(len(contraption_map[0]))
        ],
        *[
            {"location": (i, len(contraption_map[0])), "next_delta": (0, -1)}
            for i in range(len(contraption_map))
        ],
        *[
            {"location": (len(contraption_map), j), "next_delta": (-1, 0)}
            for j in range(len(contraption_map[0]))
        ],
        *[
            {"location": (i, -1), "next_delta": (0, 1)}
            for i in range(len(contraption_map))
        ],
    ]

    max_energy = 0

    for initial_beam_head in initial_beam_heads:
        energy = count_energized_tiles(initial_beam_head)
        if energy > max_energy:
            max_energy = energy

    return max_energy


solution = solve()
print(solution)