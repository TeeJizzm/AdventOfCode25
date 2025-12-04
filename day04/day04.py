## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 04

############################
# Imports

import os

import tools.texttolists as tl
import tools.grids as gr

############################
# Variables

DIRS = gr.ADJ #[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

############################
# Functions


def find_accessible_rolls(grid, rolls):

    accessible = []

    for r, c in rolls:
        s = 0 # count empty surrounding spaces
        for dr, dc in DIRS:
            if grid[r+dr][c+dc] == "@":
                s += 1
        if s < 4:
            accessible.append([r, c])
        
    return accessible

def day04(text):
    print("Day 04 - Printing Department")
    
    grid = gr.padArray(tl.toGrid(text),1)

    rolls = gr.findLocs(grid, "@")
    
    a_rolls = find_accessible_rolls(grid, rolls)
    part1 = len(a_rolls)

    removed = []

    while len(a_rolls) > 0:
        rolls = gr.findLocs(grid, "@")
        a_rolls = find_accessible_rolls(grid, rolls)
        gr.setLocs(grid, a_rolls, ".") # remove accessible rolls
        for each in a_rolls:
            removed.append(each)

    part2 = len(removed)
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day04/inc" 
    
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

    part1, part2 = day04(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############