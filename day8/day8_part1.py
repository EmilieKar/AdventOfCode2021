# AOC2021 https://adventofcode.com/2021/day/8
#
# DAY  EIGHT
# --------- part 1 ------------
digit_counts = 0

with open('input.txt') as f:
    for line in f:
        four_digits = line.split('|')[1]
        for digit in four_digits.split():
            if len(digit) in [2,4,3,7]:
                digit_counts += 1

print(f"Answer to part1 is: {digit_counts}")

