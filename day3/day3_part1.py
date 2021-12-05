# AOC2021 https://adventofcode.com/2021/day/3
#
# DAY  THREE
# --------- part 1 ------------

with open('input.txt') as f:
    # one_count stores how many ones have appeared in each position of the binary numbers
    # initialized as the first binary number in the file
    one_count = [int(x) for x in f.readline()[0:-1]] 
    instance_count = 1
    binary_length = len(one_count)

    for bin_number in f:
        for index in range(binary_length):
            bit = bin_number[index]
            if bit == "1":
                one_count[index] += 1
        instance_count += 1

print(f"OneCount {one_count} number of instances {instance_count}")

gamma = 0
epsilon = 0

for index in range(binary_length):
    if one_count[index] > (instance_count/2): # Check if more 1s than 0s at index 
        gamma += pow(2,binary_length-index-1)
    else:
        epsilon += pow(2, binary_length-index-1)

print(f"Gamma: {gamma} Epsilon:{epsilon} \nAnswer(power consumption):{gamma*epsilon}")