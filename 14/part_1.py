import sys


def solve():
    state = [list(line.strip()) for line in sys.stdin.readlines() if not line.isspace()]
    next_state = tilt(state, "north")
    return measure_north_beam_load(next_state)


def tilt(state, direction):
    if direction == "north":
        next_state = []

        for i in range(len(state)):
            if i == 0:
                next_state.append(state[i])
                continue

            row = []

            for j in range(len(state[0])):
                if state[i][j] == "O":
                    target_i = None

                    for possible_target_i in range(i - 1, -1, -1):
                        if next_state[possible_target_i][j] == ".":
                            target_i = possible_target_i
                        else:
                            break

                    if target_i is not None:
                        next_state[target_i][j] = "O"
                        row.append(".")
                    else:
                        row.append("O")
                else:
                    row.append(state[i][j])

            next_state.append(row)

        return next_state
    else:
        raise ValueError(f"Invalid direction {direction}")

def measure_north_beam_load(state):
    total_load = 0

    for i in range(len(state)):
        load = len(state) - i

        for j in range(len(state[0])):
            if state[i][j] == "O":
                total_load += load

    return total_load

solution = solve()
print(solution)