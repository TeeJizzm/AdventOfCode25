## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 05

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables



############################
# Functions

def day05(text):
    print("Day 05 - Cafeteria")
    
    part1, part2 = 0, 0
    
    ranges, ingredients = text.split("\n\n")
    ranges = ranges.split("\n")
    ranges = [[int(v) for v in r.split("-")] for r in ranges]
    ingredients = [int(i) for i in ingredients.split("\n")]

    # Part 1
    for i in ingredients:
        for r in ranges:
            if r[0] <= i <= r[1]:
                part1 += 1
                break

    # Part 2
    ranges.sort()
    pbot, ptop = 0, 0
    for bot, top in ranges:
        if bot > ptop: # Not intersecting, add full range
            part2 += (top - bot) + 1
            pbot, ptop = bot, top
        elif bot <= ptop and top > ptop: # Intersection, extend to new range
            part2 += (top - ptop)
            ptop = top
        #print(pbot, ptop, bot, top, part2)
    print(part2)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day05/inc" 
    
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

    part1, part2 = day05(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############