# AOC2021 https://adventofcode.com/2021/day/3
#
# DAY  THREE
# --------- part 2 ------------

with open('input.txt') as f:
    #Create a list of all the binary numbers where each binary number is represented by a list of int
    input_list = [[int(x) for x in line[0:-1]] for line in f] 
    
def sort_indicies(possibilities, current_index):
    by_bit = {
        0: [],
        1: [],
    }
    for entry in possibilities:
        if entry[current_index] is 0:
            by_bit[0].append(entry)
        else:
            by_bit[1].append(entry)
    return by_bit

# Oxygen calculation
current_index = 0
possible_oxygen_indexes = input_list

while len(possible_oxygen_indexes) > 1:
    by_bit = sort_indicies(possible_oxygen_indexes, current_index)
    
    if len(by_bit[0]) > len(by_bit[1]):
        possible_oxygen_indexes = by_bit[0]
    else:
        possible_oxygen_indexes = by_bit[1]

    current_index += 1

# Co2 calculation
current_index = 0
possible_co2_indexes = input_list

while len(possible_co2_indexes) > 1:
    by_bit = sort_indicies(possible_co2_indexes, current_index)

    if len(by_bit[0]) > len(by_bit[1]):
        possible_co2_indexes = by_bit[1]
    else:
        possible_co2_indexes = by_bit[0]

    current_index += 1

def bin_to_dec(bin_number_as_list):
    dec_value = 0
    length = len(bin_number_as_list)

    for index in range(length):
        if bin_number_as_list[index] is 1:
            dec_value += pow(2,length-index-1)
    return dec_value

oxygen_rate = bin_to_dec(possible_oxygen_indexes[0])
co2_rate = bin_to_dec(possible_co2_indexes[0])

print(f"Oxygen rate: {oxygen_rate} Co2 rate:{co2_rate}")
print(f"Answer: {oxygen_rate*co2_rate}")