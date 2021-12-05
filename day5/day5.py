# AOC2021 https://adventofcode.com/2021/day/5
#
# DAY  FIVE

import re
import numpy as np

vents_map = np.zeros((1000,1000))

# helper function to fix ranges
def range_fix(a1, a2):
    bounds = (0,0)
    if a1 > a2:
        bounds = (a2, a1+1)
    else:
        bounds = (a1, a2+1)
    return bounds

with open('input.txt') as f:
    for line in f:
        # extract all numbers from input string as list of ints
        input_list = [int(x) for x in re.findall(r'\d+', line)]
        vent ={
            'x1': input_list[0],
            'y1': input_list[1],
            'x2': input_list[2],
            'y2': input_list[3]
        }

        if vent['x1'] == vent['x2']: # if horizontal
            bounds = range_fix(vent['y1'], vent['y2']) # range helper funtion
            for i in range(bounds[0], bounds[1]):
                vents_map[vent['x1'], i] += 1

        elif vent['y1'] == vent['y2']: # if vertical
            bounds = range_fix(vent['x1'], vent['x2']) # range helper funtion
            for i in range(bounds[0], bounds[1]):
                vents_map[i, vent['y1']] += 1
        
        #--------- part 2 -------------
        # comment out this block to get answer for part 1

        else: 
            if vent['x1'] < vent['x2']:
                left_x = vent['x1']
                left_y = vent['y1']
                right_x = vent['x2']
                right_y = vent['y2']
            else:
                left_x = vent['x2']
                left_y = vent['y2']
                right_x = vent['x1']
                right_y = vent['y1']

            x_diff = right_x - left_x
            if right_y > left_y:
                y_dir =  1 # the diagonal goes up from the leftmost point
            else:
                y_dir = -1 # the diagonal goes down from the leftmost point
            for i in range(x_diff + 1):
                vents_map[left_x+i, left_y+i*y_dir] += 1
        
        #---------------------------------

intersections = np.argwhere(vents_map > 1)
print(f"Answer is: {len(intersections)}")