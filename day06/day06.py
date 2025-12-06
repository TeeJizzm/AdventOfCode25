## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 06

############################
# Imports

import os
import re

import tools.texttolists as tl
import tools.grids as gr
import tools.listmath as lm

############################
# Variables



############################
# Functions

def calcpart2(text):
    total = 0
    g = list(map(list, zip(*tl.toGrid(text))))
    cols = ["".join(map(str, c)) for c in g]

    #print(cols)
    nums = []

    for col in reversed(cols):
        #print(col)
        n = re.findall(r"\d+", col)
        if n:
            #print(n[0])
            nums.append(int(n[0]))
        o = re.findall(r"[*+]", col)
        if o:
            if o[0] == "*":
                total += (lm.multiplyList(nums))
            elif o[0] == "+":
                total += sum(nums)
            nums = []

    return total

def calcpart1(text):

    lines = tl.toLines(text)

    nums = [re.findall(r"\d+", line) for line in lines[:-1]]
    ops = re.findall(r"[+*]", lines[-1])

    total = 0
    for i, o in enumerate(ops):
        #print(i ,o)
        if o == "*":
            x = 1
        elif o == "+":
            x = 0
        for num in nums:
            #print(i, num[i], o)
            if o == "*":
                x *= int(num[i]) 
            elif o == "+":
                x += int(num[i])
        total += x


    return total

def day06(text):
    print("Day 06 - Trash Compactor")

    part1 = calcpart1(text)

    part2 = calcpart2(text)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day06/inc" 
    
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

    part1, part2 = day06(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############