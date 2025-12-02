## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 02

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables



############################
# Functions

def checkInvalid(num, n=2):
    if len(num) % n != 0:
        return 0
    size = len(num) // n

    #print("--", num[0:half], num[half:], num[0:half] == num[half:])

    split = [num[i:i+size] for i in range(0, len(num), size)]
    #print(split, set(split), len(set(split)))
    if len(set(split)) == 1:
        #print("Added")
        return int(num)

    return 0

    """ if num[0:half] == num[half:]:
        #print("+", int(num))
        return int(num)
    else:
        return 0 """


def day02(text):
    print("Day 02 - Gift Shop")
    
    ranges = tl.to2dLists(text, ",", "-")

    part1, part2 = 0, 0

    for each in ranges:
        for i in range(int(each[0]), int(each[1])+1):
            #print(i, len(str(i)))
            part1 += checkInvalid(str(i))
            for x in range(2, len(str(i))+1):
                #print(x)
                res = checkInvalid(str(i), x)
                if res > 0:
                    part2 += res
                    break

    
    
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day02/inc" 
    
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

    part1, part2 = day02(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############