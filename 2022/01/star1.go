package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var top_3 [3]int64

func sort_top3(current int64) {
	if current > top_3[0] {
		top_3[2] = top_3[1]
		top_3[1] = top_3[0]
		top_3[0] = current
	} else if current > top_3[1] {
		top_3[2] = top_3[1]
		top_3[1] = current
	} else if current > top_3[2] {
		top_3[2] = current
	}
}

func getMaxCalories(fileName string) {
	var current int64 = 0
	readFile, err := os.Open(fileName)

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		var line string = fileScanner.Text()
		var lineIntValue int64 = 0

		if line == "" {
			sort_top3(current)
			current = 0
		} else {
			lineIntValue, _ = strconv.ParseInt(line, 10, 64)
			current = current + lineIntValue
		}
	}

	readFile.Close()
	sort_top3(current)
}

func main() {
	top_3[0] = 0
	top_3[1] = 0
	top_3[2] = 0

	getMaxCalories("large_input")
	fmt.Println(top_3[2] + top_3[1] + top_3[0])
}
