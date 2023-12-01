import sys

calibration_sum = 0

for line in sys.stdin:
    digits = [c for c in line if ord(c) in range(ord('0'), ord('9') + 1)]
    calibration_sum += 10 * int(digits[0]) + int(digits[-1])

print(calibration_sum)
