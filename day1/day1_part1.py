# AOC2021 https://adventofcode.com/2021/day/1
#
# DAY  ONE
# --------- part 1 ------------

increased = 0

with open('input.txt') as f:
    depth = int(f.readline())
    for line in f:
        if int(line) > depth:
            increased += 1
        depth = int(line)    

print(f"Answer to part 1: {increased}")


