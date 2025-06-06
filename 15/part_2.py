import sys


def solve():
    initialization_sequence = ''.join(
        line.strip() for line in sys.stdin.readlines() if not line.isspace()
    ).split(',')

    boxes = [[] for _ in range(256)]

    for step in initialization_sequence:
        label, operation, operand = parse_step(step)
        box = compute_hash(label)

        if operation == "=":
            index = [i for i in range(len(boxes[box])) if boxes[box][i][0] == label]

            try:
                boxes[box][index[0]] = (label, operand)
            except IndexError:
                boxes[box].append((label, operand))
        elif operation == "-":
            index = [i for i in range(len(boxes[box])) if boxes[box][i][0] == label]

            try:
                boxes[box].pop(index[0])
            except IndexError:
                pass

    focusing_power = 0

    for box_number, box in enumerate(boxes, 1):
        for slot_number, (_, focal_length) in enumerate(box, 1):
            focusing_power += box_number * slot_number * focal_length

    return focusing_power


def parse_step(step):
    label = ""
    operator = None
    operand = None

    for char in step:
        if operator == "=":
            operand = int(char)
            continue

        if char == "=":
            operator = "="
            continue

        if char == "-":
            operator = "-"
            continue

        if operator is not None:
            raise ValueError(f"Invalid step {step}")

        label += char

    return label, operator, operand

def compute_hash(str):
    current_value = 0

    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    return current_value


solution = solve()
print(solution)