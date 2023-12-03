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


def has_adjacent_entity(entity, possible_neighbours):
    for possible_neighbour in possible_neighbours:
        for a in entity['coords']:
            for b in possible_neighbour['coords']:
                if abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1:
                    return True

    return False


schematic = parse_schematic(sys.stdin)
part_number_sum = sum([
    part['value']
    for part in schematic['part']
    if has_adjacent_entity(part, schematic['symbol'])
])
print(part_number_sum)
