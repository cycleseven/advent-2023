import itertools
import math
import sys


def parse(input_lines):
    instructions = list(input_lines[0].rstrip())

    nodes = {}
    for line in input_lines[2:]:
        node, rest = line.rstrip().split(' = ')
        left, right = rest[1:-1].split(', ')
        nodes[node] = {'L': left, 'R': right}

    return {'instructions': instructions, 'nodes': nodes}


def solve(nodes, instructions):
    start_nodes = [n for n in nodes.keys() if n[-1] == 'A']
    node_distances = {}

    for start_node in start_nodes:
        prior_states = set()
        node_distances[start_node] = {}
        current_node = start_node
        steps = 0

        while steps == 0 or (current_node, steps % len(instructions)) not in prior_states:
            prior_states.add((current_node, steps % len(instructions)))
            instruction = instructions[steps % len(instructions)]
            current_node = nodes[current_node][instruction]
            steps += 1

            if current_node[-1] == 'Z' and current_node not in node_distances[start_node]:
                node_distances[start_node][current_node] = steps

    # Each "A" node only links to one "Z" node in my puzzle input, so this code
    # only considers that case
    z_distances = sorted(
        itertools.chain.from_iterable(x.values() for x in node_distances.values()),
        reverse=True
    )

    return math.lcm(*z_distances)


puzzle_input = parse(sys.stdin.readlines())
solution = solve(puzzle_input['nodes'], puzzle_input['instructions'])
print(solution)
