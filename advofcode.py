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