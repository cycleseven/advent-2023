# General idea: pray that the sequence of states repeats. Once we see a state we've
# already seen, we know for sure how the sequence will continue from there. At that
# point we can just look up the end state from the history recorded so far, based on
# <remaining number of spin cycles> % <sequence length>

import sys


def solve():
    state = [list(line.strip()) for line in sys.stdin.readlines() if not line.isspace()]
    state_history = [state]
    state_history_lookup = {freeze(state): 0}

    while True:
        next_state = tilt(state_history[-1], "north")
        next_state = tilt(next_state, "west")
        next_state = tilt(next_state, "south")
        next_state = tilt(next_state, "east")

        frozen_state = freeze(next_state)

        if frozen_state in state_history_lookup:
            remaining_spin_cycles = 1_000_000_000 - len(state_history)
            sequence_start_index = state_history_lookup[frozen_state]
            sequence_end_index = len(state_history) - 1
            sequence_length = sequence_end_index - sequence_start_index + 1
            end_state_index = sequence_start_index + (remaining_spin_cycles % sequence_length)
            return measure_north_beam_load(state_history[end_state_index])
        else:
            state_history.append(next_state)
            state_history_lookup[frozen_state] = len(state_history) - 1


# South/east/west tilts are implemented by rearranging, tilting north, then undoing the original rearrangement.
# This is a lazy approach, probably quite inefficient. But the solution executes quickly enough so I don't care too
# much :D
def tilt(state, direction):
    if direction == "north":
        next_state = []

        for i in range(len(state)):
            if i == 0:
                next_state.append([*state[i]])
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
    elif direction == "south":
        return list(reversed(tilt(list(reversed(state)), "north")))
    elif direction == "west":
        return [
            list(row) for row in
            zip(*tilt([list(row) for row in zip(*state)], "north"))
        ]
    elif direction == "east":
        # TODO: list conversions getting ridic, any better way?
        return [
            list(reversed(row)) for row in
            zip(*tilt(list(reversed([list(row) for row in zip(*state)])), "north"))
        ]
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


def freeze(state):
    return tuple(tuple(row) for row in state)

solution = solve()
print(solution)