/* ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## */

// Day 17

// -----------------------------------

package main

// Imports
import (
	// Input/Output
	"fmt"
	"io/ioutil"
	// String manipulation
	//"strings"
	//"strconv"
	// Other required imports
)

/* -----------------------------------
// Functions */

func main() {
	fmt.Println("Day 17 - *NAME*")

	// ------------ File -------------

	//*/ - File switch
	file, err := ioutil.ReadFile("day17/inc/ex.txt")
	/*/ //
	file, err := ioutil.ReadFile("day17/inc/in.txt")
	// --- End --- */

	if err != nil {
		fmt.Println(err)
	}

	text := string(file)
	//fmt.Print(text)

	// ----------- Setup -------------

	part1 := ""
	part2 := ""

	// ----------- Output ------------

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

// -----------------------------------
