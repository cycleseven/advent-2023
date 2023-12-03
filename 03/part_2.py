import math
import sys


# 🤢
def parse_schematic(schematic_input):
    schematic = {
        'part': [],
        'symbol': [],
    }

    for i, line in enumerate(schematic_input):
        current_entity = None

        for j, char in enumerate(line.rstrip()):
            if current_entity:
                if current_entity['type'] == 'part' and char.isdigit():
                    current_entity = {
                        **current_entity,
                        'value': current_entity['value'] + char,
                        'coords': [*current_entity['coords'], (i, j)],
                    }
                    continue

                schematic_item = {
                    'coords': current_entity['coords'],
                    'value': (
                        int(current_entity['value'])
                        if current_entity['type'] == 'part'
                        else current_entity['value']
                    )
                }

                schematic[current_entity['type']].append(schematic_item)
                current_entity = None

            if char.isdigit():
                current_entity = {
                    'type': 'part',
                    'value': char,
                    'coords': [(i, j)]
                }
            elif char != '.':
                current_entity = {
                    'type': 'symbol',
                    'value': char,
                    'coords': [(i, j)],
                }

    return schematic


def is_adjacent(entity_a, entity_b):
    for a in entity_a['coords']:
        for b in entity_b['coords']:
            if abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1:
                return True

    return False


def sum_gear_ratios(schematic):
    gear_ratio_sum = 0

    for symbol in schematic['symbol']:
        if symbol['value'] != '*':
            continue

        adjacent_parts = []
        for part in schematic['part']:
            if is_adjacent(part, symbol):
                adjacent_parts.append(part['value'])

        if len(adjacent_parts) == 2:
            gear_ratio_sum += math.prod(adjacent_parts)

    return gear_ratio_sum


schematic = parse_schematic(sys.stdin)
print(sum_gear_ratios(schematic))
