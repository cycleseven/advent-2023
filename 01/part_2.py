import sys

digit_strings = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}

reverse_digit_strings = {key[::-1]: value for key, value in digit_strings.items()}


def find_first_digit(string, dictionary):
    matches = []

    for target, value in dictionary.items():
        index = string.find(target)

        if index >= 0:
            matches.append((index, value))

    return min(matches)[1]


calibration_sum = 0

for line in sys.stdin:
    first_digit = find_first_digit(line, digit_strings)
    last_digit = find_first_digit(line[::-1], reverse_digit_strings)
    calibration_sum += 10 * first_digit + last_digit

print(calibration_sum)
