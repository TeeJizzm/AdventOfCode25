## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 01

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables

DIAL_START_POSITION = 50
DIAL_RANGE = 100

############################
# Functions


def move_manually(dial, dir, move):
    stop = dial + (move * dir)
    tick = 0
    for x in range(move):
        dial += dir

        if dial == -1:
            dial = 99
            tick += 1
        elif dial == 100:
            dial = 0
            tick += 1

    return (stop) % 100, tick


def move_dial(dial, move):
    stop = dial + move
    tick = 0

    tick = abs(stop // 100)

    dial = stop % 100

    return dial, tick


def manualZeroes(commands):
    part1 = 0
    part2 = 0
    dial = 50

    for dir, move in commands:
        print("Move:", dir, move)

        newpos = dial

        for i in range(move):
            newpos, tick = move_dial(newpos, dir)
            if newpos == 0:
                part2 += 1

        # print(newpos, tick)
        # part2 += tick
        if newpos == 0:
            part1 += 1
        dial = newpos

    return part1, part2


def countZeroes(commands):
    part1 = 0
    part2 = 0
    dial = 50

    for move in commands:
        newpos, tick = move_dial(dial, move)

        if dial == 0:
            part1 += 1
        part2 += tick

        # print(dial, move, newpos, tick)
        dial = newpos

    return part1, part2


def day01(text):
    print("Day 01 - Secret Entrance")

    rotations = tl.toList(text)
    moves = []
    commands = []
    for each in rotations:
        if each[0] == "L":
            x = -1
        elif each[0] == "R":
            x = 1
        else:
            x = 0
        moves.append(int(each[1:]) * x)
        commands.append((x, int(each[1:])))

    part1, part2 = manualZeroes(commands)

    # print(part1, part2)
    # part1, part2 = countZeroes(moves)
    # print(commands)

    return part1, part2


############################
# Run main

if __name__ == "__main__":
    day = "day01/inc"

    # Change file
    #######
    file = "ex.txt"
    file = "in.txt"
    #######

    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)

    # Open file, clean up memory after
    with open(filepath, "r") as file:
        text = file.read()  # Read data

    part1, part2 = day01(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)

########### EOF ############
