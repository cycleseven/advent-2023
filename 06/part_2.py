import sys


def solve():
    race = parse(sys.stdin.readlines())
    ways_to_win = 0

    for button_hold_duration in range(race['time'] + 1):
        speed = button_hold_duration
        travel_duration = race['time'] - button_hold_duration
        distance_traveled = speed * travel_duration

        if distance_traveled > race['record']:
            ways_to_win += 1

    return ways_to_win


def parse(input_lines):
    return {
        'time': int(input_lines[0].split(':')[1].replace(' ', '')),
        'record': int(input_lines[1].split(':')[1].replace(' ', ''))
    }


solution = solve()
print(solution)
