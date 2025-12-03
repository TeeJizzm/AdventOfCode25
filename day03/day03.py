## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 03

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables



############################
# Functions

def findBiggest(nums, size=2):
    biggest = []
    y = 0

    for x in range(size-1, -1, -1):
        high = max(nums[:len(nums) - x])
        y = nums.index(high) + 1
        nums = nums[y:]
        biggest.append(high)
    
    return int("".join(map(str, biggest)))


def day03(text):
    print("Day 03 - Lobby")
    
    part1, part2 = 0, 0
    
    banks = tl.toList(text)
    for bank in banks:
        nums = [int(n) for n in bank]

        part1 += findBiggest(nums, 2)
        part2 += findBiggest(nums, 12)
    
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day03/inc" 
    
    # Change file
    #######
    file = "ex.txt"
    file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day03(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############