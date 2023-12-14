import sys

sum = 0

for line in sys.stdin:
    values = [[int(x) for x in line.split()]]

    while not all(x == 0 for x in values[-1]):
        values.append([b - a for a, b in zip(values[-1], values[-1][1:])])

    predicted_value = 0
    for row in reversed(values[:-1]):
        predicted_value = row[0] - predicted_value

    sum += predicted_value

print(sum)
