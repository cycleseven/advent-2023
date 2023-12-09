import itertools
import sys


def solve():
    almanac = parse_almanac(sys.stdin.readlines())
    item_ranges = set(almanac['seeds'])

    for layer in almanac['layers']:
        item_ranges_to_splice = set(item_ranges)
        splice_points = set(itertools.chain.from_iterable(mapping[0] for mapping in layer))
        next_item_ranges = set()

        while len(item_ranges_to_splice) > 0:
            item_range = item_ranges_to_splice.pop()
            spliced = splice_range(item_range, splice_points)

            if len(spliced) == 1:
                fully_spliced = spliced[0]

                relevant_mappings = [
                    (source, dest)
                    for source, dest in layer
                    if source[0] <= fully_spliced[0] < fully_spliced[1] <= source[1]
                ]

                if len(relevant_mappings) > 1:
                    raise ValueError(f'Fully spliced input range overlaps multiple mapping ranges (spliced range {spliced}, overlapping mappings are {relevant_mappings}')

                if len(relevant_mappings) == 0:
                    next_item_ranges.add(spliced[0])
                    continue

                next_item_ranges.add(apply_mapping(spliced[0], relevant_mappings[0]))
            else:
                item_ranges_to_splice = item_ranges_to_splice.union(spliced)

        item_ranges = next_item_ranges

    return min(itertools.chain.from_iterable(item_ranges))


def parse_almanac(input_lines):
    almanac = {
        'seeds': [
            (start, start + range_size)
            for start, range_size
            in pairs([int(x) for x in input_lines[0].split(': ')[1].split()])
        ],
        'layers': []
    }

    for line in input_lines[2:]:
        line = line.rstrip()

        if line.endswith(':'):
            almanac['layers'].append([])
            continue

        if len(line) == 0:
            continue

        dest_start, source_start, range_size = [int(x) for x in line.split()]
        source_range = (source_start, source_start + range_size)
        dest_range = (dest_start, dest_start + range_size)
        almanac['layers'][-1].append((source_range, dest_range))

    return almanac


def splice_range(target, splice_points):
    start, end = target
    splice_points = [x for x in splice_points if start < x < end]
    range_markers = [start, *splice_points, end]

    return [(a, b) for a, b in zip(range_markers, range_markers[1:])]


def apply_mapping(spliced_range, mapping):
    source, dest = mapping

    return (
        spliced_range[0] + dest[0] - source[0],
        spliced_range[1] + dest[1] - source[1],
    )


def pairs(items):
    return (items[i:i + 2] for i in range(0, len(items), 2))


solution = solve()
print(solution)
