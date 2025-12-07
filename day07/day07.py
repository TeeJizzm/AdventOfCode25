## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 07

############################
# Imports

import os
from copy import deepcopy as dc

import tools.texttolists as tl
import tools.grids as gr

############################
# Variables


############################
# Functions

def quantumLine(prev, curr):
    for idx, val in enumerate(prev):
        if isinstance(val, int) and val > 0:
            val = val if isinstance(val, int) else 1
            if curr[idx] == "^" or curr[idx] == "*":
                curr[idx] = "*"
                curr[idx - 1] = val + curr[idx-1]
                curr[idx + 1] = val + curr[idx+1]
            elif isinstance(curr[idx], int):
                curr[idx] - val
            else:
                curr[idx] = val if isinstance(val, int) else 1
    return curr

def updateLine(prev, curr):

    for idx, val in enumerate(prev):
        if val == "S" or val == "|":
            if curr[idx] == "^":
                curr[idx] = "*"
                curr[idx - 1] = "|"
                curr[idx + 1] = "|"
            else:
                curr[idx] = "|"
    return curr
    

def day07(text):
    print("Day 07 - Laboratories")
    
    part1, part2 = 0, 0
    
    #grid = tl.toGrid(text)
    grid = gr.padArray(tl.toGrid(text), 1)
    gr.setLocs(grid, gr.findLocs(grid, "."), 0)
    gr.setLocs(grid, gr.findLocs(grid, "S"), 1)

    for r in range(len(grid[:-1])):
        #grid[r+1] = updateLine(grid[r],grid[r+1])
        grid[r+1] = quantumLine(grid[r],grid[r+1])

    for x, line in enumerate(grid):
        part1 += line.count("*")
        print(line)


    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day07/inc" 
    
    # Change file
    #######
    file = "ex.txt"
    #file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day07(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############