# AOC2021 https://adventofcode.com/2021/day/7
#
# DAY  SEVEN

import re 
import numpy as np

with open('input.txt') as f:
    horizontal_positions = np.array([int(x) for x in re.findall(r'\d+', f.readline())])

max_pos = np.max(horizontal_positions)

# --------- part 1 ------------
# min_sum initialized to sum of movement at horizontal position 0
min_sum = distance_to_move = np.sum(horizontal_positions) 

# Test which horizontal position gives the smallest sum of horizontal movement 
for pos in range(max_pos):
    pos_sum = np.sum(abs(horizontal_positions - pos + 1))
    if pos_sum < min_sum:
        min_sum = pos_sum

print(f"Answer to part 1 is: {min_sum}")

# --------- part 2 ------------
# Use arithmetic sum to calculate the horizontal movement cost
# Sum = (number of terms/2)*(first term + last term)

# min_sum initialized to cost sum of movement at horizontal position 0
min_sum = distance_to_move = np.sum((horizontal_positions/2)*(1+horizontal_positions)) 

# Test which horizontal position gives the smallest cost sum of horizontal movement 
for pos in range(max_pos):
    movement = abs(horizontal_positions - pos + 1)
    pos_sum = np.sum((movement/2)*(1+movement))
    if pos_sum < min_sum:
        min_sum = pos_sum

print(f"Answer to part 2 is: {min_sum}")
