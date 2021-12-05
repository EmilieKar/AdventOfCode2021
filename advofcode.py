# DAY ONE
# ---------part 2 ------------ 
"""
depth = [0,0,0]
count = 0
increased = 0

with open('input.txt') as f:
    for line in f:
        i = count % 3
        if count > 2:   #fill list initially
            if  int(line) > depth[i]:
                increased += 1
                print(f"{depth} old is {depth[i]} and new value is {int(line)}")
        depth[i] = int(line)    
        count += 1
print(increased)
"""
# DAY 2
#------part 1------------
"""
direction = 0
x = 0

horizontal_position = 0
depth = 0
with open('input.txt') as f:
    for line in f:
        direction = line[0:-3]
        x = int(line[-2])
        if direction == "forward":
            horizontal_position += x
        elif direction == "down":
            depth += x
        elif direction == "up":
            depth -= x
print(f"Horizontal position is {horizontal_position}, depth is {depth}")
print(f"Answer is {horizontal_position * depth}")
"""
#---------part2-------------
"""
direction = 0
x = 0

horizontal_position = 0
depth = 0
aim = 0
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
"""
# DAY 3
#----------part1--------------
"""
with open('input.txt') as f:
    one_count = [int(x) for x in f.readline()[0:-1]]
    instance_count = 1
    binary_length = len(one_count)
    for line in f:
        for i in range(binary_length):
            x = line[i]
            if x == "1":
                one_count[i] += 1
        instance_count += 1

print(f"OneCount {one_count} number of instances {instance_count}")

gamma = 0
epsilon = 0


for i in range(binary_length):
    if one_count[i] > (instance_count/2):
        gamma += pow(2,binary_length-i-1)
    else:
        epsilon += pow(2, binary_length-i-1)

print(f"Gamma: {gamma} Epsilon:{epsilon} Answer(power consumption):{gamma*epsilon}")
"""
#----------part2--------------
"""
with open('input.txt') as f:
    #Create a list of all the binary numbers where each binary number is represented by a list of int
    input_list = [[int(x) for x in line[0:-1]] for line in f] 
    oxygen_indexes = input_list
    co2_indexes = input_list

def sort_indicies(possibilities, current_pos):
    by_bit = {
        0: [],
        1: [],
    }
    for entry in possibilities:
        if entry[current_pos] is 0:
            by_bit[0].append(entry)
        else:
            by_bit[1].append(entry)
    return by_bit

# Oxygen calculation
current_pos = 0
while len(oxygen_indexes) > 1:
    by_bit = sort_indicies(oxygen_indexes, current_pos)
    
    if len(by_bit[0]) > len(by_bit[1]):
        oxygen_indexes = by_bit[0]
    else:
        oxygen_indexes = by_bit[1]

    current_pos += 1

# Co2 calculation
current_pos = 0
while len(co2_indexes) > 1:
    by_bit = sort_indicies(co2_indexes, current_pos)

    if len(by_bit[0]) > len(by_bit[1]):
        co2_indexes = by_bit[1]
    else:
        co2_indexes = by_bit[0]

    current_pos += 1

def bin_to_dec(bin_list):
    dec_value = 0
    length = len(bin_list)
    for i in range(length):
        if bin_list[i] is 1:
            dec_value += pow(2,length-i-1)
    return dec_value

oxygen_value = bin_to_dec(oxygen_indexes[0])
co2_value = bin_to_dec(co2_indexes[0])
print(f"Oxygen: {oxygen_value} Co2:{co2_value}")
print(f"Answer: {oxygen_value*co2_value}")
"""
# Day 4
"""
with open('input.txt') as f:
    line = f.readline()[0:-1]
    numbers_to_call = [int(s) for s in line.split(',')]
    f.readline()
    bingo_tiles = []
    bingo_tile_as_string = []

    for line in f:
        if line == '\n':
            bingo_tiles.append(bingo_tile_as_string)
            bingo_tile_as_string = []
        else:
            bingo_tile_as_string += [int(s) for s in line.split() if s.isdigit()]


def mark_number(drawn_number, bingo_tiles):
    return [[x if x != drawn_number else -1 for x in tile] for tile in bingo_tiles]


def calculate_answer(tile, input_number):
    answer = 0
    for number in tile:
        if number != -1:
            answer += number

    answer *= input_number
    print(answer)
#---------part 1----------

def check_bingo():
    for tile in bingo_tiles:
        for i in range(5):
            if all(x == -1 for x in tile[0+i*5:5+i*5]) or all(x == -1 for x in tile[i::5]):
                print("bingo")
                return tile
    print("no bingo")
    return None

for number in numbers_to_call:
    bingo_tiles = mark_number(number, bingo_tiles)
    tmp = check_bingo()
    if tmp is not None:
        winning_tile = tmp
        last_number = number
        break

calculate_answer(winning_tile, last_number)

#----------part 2----------

def check_bingo(bingo_tiles):
    for tile in bingo_tiles:
        for i in range(5):
            if all(x == -1 for x in tile[0+i*5:5+i*5]) or all(x == -1 for x in tile[i::5]):
                bingo_tiles.remove(tile)
                break
    return bingo_tiles
    
for number in numbers_to_call:
    bingo_tiles = mark_number(number, bingo_tiles)
    
    if len(bingo_tiles) == 1:
        last_tile = bingo_tiles[0]

    bingo_tiles = check_bingo(bingo_tiles)

    if len(bingo_tiles) == 0:
        last_number = number 
        print(last_tile)
        print(last_number)
        break

calculate_answer(last_tile, last_number)
"""
"""
# Day 5
import re
import numpy as np

vents_map = np.zeros((1000,1000))

def range_fix(a1, a2):
    bounds = (0,0)
    if a1 > a2:
        bounds = (a2, a1+1)
    else:
        bounds = (a1, a2+1)
    return bounds

with open('input.txt') as f:
    for line in f:
        vent_info = [int(x) for x in re.findall(r'\d+', line)]

        if vent_info[0] == vent_info[2]: # if horizontal
            bounds = range_fix(vent_info[1], vent_info[3])
            for i in range(bounds[0], bounds[1]):
                vents_map[vent_info[0], i] += 1

        elif vent_info[1] == vent_info[3]: # if vertical
            bounds = range_fix(vent_info[0], vent_info[2])
            for i in range(bounds[0], bounds[1]):
                vents_map[i, vent_info[1]] += 1
        
        #--------- part 2 -------------

        else: 
            if vent_info[0] < vent_info[2]:
                left_point = vent_info[:2]
                right_point = vent_info[2:]
            else:
                left_point = vent_info[2:]
                right_point = vent_info[:2]

            x_diff = right_point[0] - left_point[0]
            if right_point[1] > left_point[1]:
                y_dir =  1 
            else:
                y_dir = -1
            for i in range(x_diff + 1):
                vents_map[left_point[0]+i, left_point[1]+i*y_dir] += 1


intersections = np.argwhere(vents_map > 1)
print(len(intersections))
"""