import sys

calibration_sum = 0

for line in sys.stdin:
    digits = [c for c in line if c.isdigit()]
    calibration_sum += int(digits[0] + digits[-1])

print(calibration_sum)
