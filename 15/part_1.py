import sys


def solve():
    initialization_sequence = ''.join(
        line.strip() for line in sys.stdin.readlines() if not line.isspace()
    ).split(',')

    return sum(compute_hash(step) for step in initialization_sequence)


def compute_hash(str):
    current_value = 0

    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    return current_value


solution = solve()
print(solution)