import math
import sys


def parse(lines):
    patterns = [[]]

    for line in lines:
        if line.isspace():
            patterns.append([])
        else:
            patterns[-1].append(line.rstrip())

    return patterns


def summarize_reflections(patterns):
    summary = 0

    for pattern in patterns:
        rows = {"pattern": pattern, "multiplier": 100}
        columns = {"pattern": list(zip(*pattern)), "multiplier": 1}

        for layout in [rows, columns]:
            reflection_point = find_reflection_point(layout["pattern"])

            if reflection_point:
                summary += reflection_point * layout["multiplier"]
                break

    return summary


def find_reflection_point(pattern):
    for i in range(1, len(pattern)):
        reflection_size = i if i <= math.floor(len(pattern) * 0.5) else len(pattern) - i
        before = pattern[i - reflection_size : i]
        after = pattern[i : i + reflection_size]

        if sum(edit_distance(a, b) for a, b in zip(reversed(before), after)) == 1:
            return i


def edit_distance(a, b):
    distance = 0

    for a, b in zip(a, b):
        if a != b:
            distance += 1

    return distance


def main():
    patterns = parse(sys.stdin)
    print(summarize_reflections(patterns))


main()
