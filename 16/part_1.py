import sys


def solve():
    contraption_map = [list(line.strip()) for line in sys.stdin.readlines() if not line.isspace()]

    def in_bounds(location):
        i, j = location
        return 0 <= i < len(contraption_map) and 0 <= j < len(contraption_map[0])

    energized_locations = set()
    beam_history = set()
    beam_heads = [
        {"location": (0, -1), "next_delta": (0, 1)}
    ]

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


solution = solve()
print(solution)