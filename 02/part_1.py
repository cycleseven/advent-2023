import sys

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

valid_games_sum = 0

for line in sys.stdin:
    game_id_string, rounds_string = line.rstrip().split(': ')
    game_id = game_id_string.split(' ')[1]
    valid = True

    for reveals in rounds_string.split('; '):
        for reveal in reveals.split(', '):
            n, cube = reveal.split(' ')

            if int(n) > limits[cube]:
                valid = False

    if valid:
        valid_games_sum += int(game_id)

print(valid_games_sum)
