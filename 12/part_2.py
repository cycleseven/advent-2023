import sys
from functools import cache


def main():
    num_arrangements = 0

    for line in sys.stdin:
        springs, constraints = parse_line(line)
        num_arrangements += count_valid_arrangements(springs, constraints)

    print(num_arrangements)


def parse_line(line):
    springs, constraints = line.split()
    springs = '?'.join(springs for _ in range(5))
    constraints = ','.join(constraints for _ in range(5))

    return springs, tuple(int(x) for x in constraints.split(','))


@cache
def count_valid_arrangements(springs, constraints):
    if len(constraints) == 0:
        return 0 if '#' in springs else 1

    if len(springs) == 0:
        return 1 if len(constraints) == 0 else 0

    count = 0
    c = springs[0]

    if c in '.?':
        count += count_valid_arrangements(springs[1:], constraints)

    if c in '#?':
        target_group_size = constraints[0]

        if (
            target_group_size <= len(springs)
            and '.' not in springs[:target_group_size]
            and (
                target_group_size == len(springs)
                or springs[target_group_size] != '#'
            )
        ):
            count += count_valid_arrangements(
                springs[target_group_size + 1:],
                constraints[1:]
            )

    return count


main()
