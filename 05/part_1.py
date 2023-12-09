import sys


def parse_maps(input_lines):
    maps = []

    for line in input_lines:
        line = line.rstrip()

        if len(line) == 0:
            continue

        if line[-1] == ':':
            maps.append([])
            continue

        destination_range_start, source_range_start, range_length = [int(num) for num in line.split()]
        maps[-1].append({
            'destination_range': (destination_range_start, destination_range_start + range_length),
            'source_range': (source_range_start, source_range_start + range_length),
        })

    return maps


def get_location(seed, maps):
    item_number = seed

    for map in maps:
        for map_range in map:
            start, end = map_range['source_range']

            if start <= item_number < end:
                item_number = map_range['destination_range'][0] + item_number - start
                break

    return item_number


input_lines = sys.stdin.readlines()
seeds = [int(seed) for seed in input_lines[0].split(':')[1].split()]
maps = parse_maps(input_lines[1:])
print(min(get_location(seed, maps) for seed in seeds))
