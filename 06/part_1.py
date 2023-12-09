import math
import sys


def solve():
    races = parse(sys.stdin.readlines())
    ways_to_win = []

    for race in races:
        ways_to_win.append(0)

        for button_hold_duration in range(race['time'] + 1):
            speed = button_hold_duration
            travel_duration = race['time'] - button_hold_duration
            distance_traveled = speed * travel_duration

            if distance_traveled > race['record']:
                ways_to_win[-1] += 1

    return math.prod(ways_to_win)


def parse(input_lines):
    times = [int(token) for token in input_lines[0].split(':')[1].split()]
    distances = [int(token) for token in input_lines[1].split(':')[1].split()]

    return [
        {'time': time, 'record': distance}
        for time, distance in zip(times, distances)
    ]


solution = solve()
print(solution)
