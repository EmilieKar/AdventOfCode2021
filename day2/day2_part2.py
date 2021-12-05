# AOC2021 https://adventofcode.com/2021/day/2
#
# DAY  TWO
# --------- part 2 ------------

horizontal_position = 0
depth = 0
aim = 0

direction = 0   # string describing direction (eg. forward)
x = 0           # how many units of movement is performed 

with open('input.txt') as f:
    for line in f:
        direction = line[0:-3]
        x = int(line[-2])

        if direction == "forward":
            horizontal_position += x
            depth += aim * x
        elif direction == "down":
            aim += x
        elif direction == "up":
            aim -= x
            
print(f"Horizontal position is {horizontal_position}, depth is {depth}")
print(f"Answer is {horizontal_position * depth}")