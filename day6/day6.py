# AOC2021 https://adventofcode.com/2021/day/6
#
# DAY  SIX

import re

# Stores number of fish that has a fish timer value equal to the index
fish_timers = [0,0,0,0,0,0,0,0,0]

with open('input.txt') as f:
    input = [int(x) for x in re.findall(r'\d+', f.readline())]

for fish in input:
    fish_timers[fish] += 1

for _ in range(256): # part 1 -> range(80), part 2 -> range(256)
    # pop will shift the list so no subraction is necessary
    reproduced_fish = fish_timers.pop(0) 
    fish_timers[6] += reproduced_fish
    fish_timers.append(reproduced_fish)

print(f"Answer is :{sum(fish_timers)}")



    