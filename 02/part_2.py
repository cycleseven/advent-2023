import math
import sys

power_sum = 0

for line in sys.stdin:
    game_id_string, rounds_string = line.rstrip().split(': ')
    game_id = game_id_string.split(' ')[1]

    min_cube_counts = {
        'blue': 0,
        'green': 0,
        'red': 0
    }

    for reveals in rounds_string.split('; '):
        for reveal in reveals.split(', '):
            raw_n, cube = reveal.split(' ')
            n = int(raw_n)

            if n > min_cube_counts[cube]:
                min_cube_counts[cube] = n

    power_sum += math.prod(min_cube_counts.values())

print(power_sum)
