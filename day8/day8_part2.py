# AOC2021 https://adventofcode.com/2021/day/8
#
# DAY  EIGHT
# --------- part 2 ------------

# Checks if all elements in a list is present in another list b
def a_in_b(a,b):
    if_true = False
    if (all(elem in b for elem in a)):
        if_true = True
    return if_true

with open('input.txt') as f:
    final_sum = 0

    for line in f:
        # Split last four digits (input[1]) from our 10 signal patterns(input[0])
        input = line.split('|')

        # Stores the correct signal pattern for each digit corresponding to the index
        decoded_digits = [0,0,0,0,0,0,0,0,0,0]
        len_5_digits = [] # Contains signal patterns for 2,3,5 in unknown order
        len_6_digits = [] # Contains signal patterns for 0,6,9 in unknown order

        # Sort an save all digits with known lengths
        for digit in input[0].split():
            digit = sorted(digit)
            nmb_of_segments = len(digit)
            if nmb_of_segments == 5:
                len_5_digits.append(digit)
            elif nmb_of_segments == 6:
                len_6_digits.append(digit)
            elif nmb_of_segments == 2:
                decoded_digits[1] = digit
            elif nmb_of_segments == 3:
                decoded_digits[7] = digit
            elif nmb_of_segments == 4:
                decoded_digits[4] = digit
            else:
                decoded_digits[8] = digit
        
        # Determine digits of length 6
        for digit in len_6_digits:
            if a_in_b(decoded_digits[4], digit): # only 9 contains all signals in 4
                decoded_digits[9] = digit
                len_6_digits.remove(digit)
                break
        
        if a_in_b(decoded_digits[7], len_6_digits[0]): # only 0 contains all signals in 7
            decoded_digits[0] = len_6_digits[0]
            decoded_digits[6] = len_6_digits[1]
        else:
            decoded_digits[0] = len_6_digits[1]
            decoded_digits[6] = len_6_digits[0]
        
        # Determine digits of length 5
        for digit in len_5_digits:
            if a_in_b(decoded_digits[7], digit): # only 3 contains all signals in 7
                decoded_digits[3] = digit
                len_5_digits.remove(digit)
                break
        
        if a_in_b(len_5_digits[0], decoded_digits[6]): # only 5 in fully contained in 6
            decoded_digits[5] = len_5_digits[0]
            decoded_digits[2] = len_5_digits[1]
        else:
            decoded_digits[5] = len_5_digits[1]
            decoded_digits[2] = len_5_digits[0]
        
        # Decode last four digits
        four_digit_value = "" 
        for digit in input[1].split():
            four_digit_value += str(decoded_digits.index(sorted(digit)))

        final_sum += int(four_digit_value)

print(f"Answer for part2: {final_sum}")