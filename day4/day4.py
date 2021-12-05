# AOC2021 https://adventofcode.com/2021/day/4
#
# DAY  FOUR

with open('input.txt') as f:
    line = f.readline()[0:-1]
    numbers_to_call = [int(s) for s in line.split(',')]

    f.readline() # get rid of blank line before bingo tiles start

    bingo_tiles = []            # List of all bingo tiles stored as lists of ints            
    bingo_tile_as_list = []     # Helper to parse input

    for line in f:
        if line == '\n':        # Empty string marks end of bingo tile in input
            bingo_tiles.append(bingo_tile_as_list)
            bingo_tile_as_list = []
        else:
            bingo_tile_as_list += [int(s) for s in line.split() if s.isdigit()]

# replace all occurences of drawn number with -1 for all bingo tiles
def mark_number(drawn_number, bingo_tiles):
    return [[x if x != drawn_number else -1 for x in tile] for tile in bingo_tiles]

# helper function for final answer calculation
def calculate_answer(tile, input_number):
    answer = 0
    for entity in tile:
        if entity != -1:
            answer += entity

    answer *= input_number
    return answer

#---------part 1----------

def check_bingo_part1():
    winner_tile = None
    for tile in bingo_tiles:
        for i in range(5):
            # check if all elements are -1 in row and column for each diagonal entity in tile
            # -1 marks a called number
            if all(x == -1 for x in tile[0+i*5:5+i*5]) or all(x == -1 for x in tile[i::5]):
                winner_tile = tile
    return winner_tile

for number in numbers_to_call:
    bingo_tiles = mark_number(number, bingo_tiles)
    winner_tile = check_bingo_part1()
    if winner_tile is not None:
        last_number = number
        break

print(f"Answer for part 1: {calculate_answer(winner_tile, last_number)}")

#----------part 2----------

def check_bingo_part2(bingo_tiles):
    for tile in bingo_tiles:
        for i in range(5):
            # check if all elements are -1 in row and column for each diagonal entity in tile
            # -1 marks a called number
            if all(x == -1 for x in tile[0+i*5:5+i*5]) or all(x == -1 for x in tile[i::5]):
                bingo_tiles.remove(tile)
                break
    return bingo_tiles
    
for number in numbers_to_call:
    bingo_tiles = mark_number(number, bingo_tiles)
    
    if len(bingo_tiles) == 1:
        looser_tile = bingo_tiles[0]

    bingo_tiles = check_bingo_part2(bingo_tiles)

    if len(bingo_tiles) == 0:
        last_number = number 
        break

print(f"Answer for part 2: {calculate_answer(looser_tile, last_number)}")