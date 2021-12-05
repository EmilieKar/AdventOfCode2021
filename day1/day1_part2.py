# AOC2021 https://adventofcode.com/2021/day/1
#
# DAY  ONE
# --------- part 2 ------------
depth = [0,0,0] # the last 3 checked depth readings(not in order) 
increased = 0

with open('input.txt') as f:

    # fill list initially
    for i in range(3):
        depth[i] = int(f.readline())
    
    count = 3 # depth index helper

    for line in f:
        depth_index = count % 3 
        # compares new value with oldest value in depth list
        # if new value is larger increment increased count
        if  int(line) > depth[depth_index]:
            increased += 1
        depth[depth_index] = int(line)    
        count += 1

print(f"Answer to part 2: {increased}")