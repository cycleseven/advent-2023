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
    current_node = 'AAA'
    steps = 0

    while current_node != 'ZZZ':
        instruction = instructions[steps % len(instructions)]
        current_node = nodes[current_node][instruction]
        steps += 1

    return steps


puzzle_input = parse(sys.stdin.readlines())
solution = solve(puzzle_input['nodes'], puzzle_input['instructions'])
print(solution)
