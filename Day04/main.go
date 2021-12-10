package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type BingoCard struct {
	solved     bool
	cardRows   [][]int
	numbersHit map[int]bool
}

func main() {
	calledNum, bingoBlocks := LoadInput()
	partOneSolution, indexStoppedAt := SolvePartOne(calledNum, bingoBlocks)

	fmt.Println("Part One Answer:", partOneSolution)
	fmt.Println("Part Two Answer:", SolvePartTwo(calledNum, bingoBlocks, indexStoppedAt))
}

func SolvePartOne(called []int, bingoCards []BingoCard) (int, int) {
	recheckSize := len(bingoCards[0].cardRows)
	for calledIndex, calledNum := range called {
		for cardIndex, card := range bingoCards {
			if ProcessCardForHit(card, calledNum) && len(card.numbersHit) >= recheckSize && IsCardComplete(card) {
				bingoCards[cardIndex].solved = true
				return calledNum * GetSummedNonHitNums(card), calledIndex
			}
		}
	}

	return -1, -1
}

func SolvePartTwo(called []int, bingoCards []BingoCard, calledIndex int) int {
	recheckSize := len(bingoCards[0].cardRows)
	unsolved := len(bingoCards) - 1

	for ; calledIndex < len(called); calledIndex++ {
		for cardIndex, card := range bingoCards {
			if !card.solved && ProcessCardForHit(card, called[calledIndex]) && len(card.numbersHit) >= recheckSize && IsCardComplete(card) {
				bingoCards[cardIndex].solved = true
				unsolved--
				if unsolved == 0 {
					return called[calledIndex] * GetSummedNonHitNums(card)
				}
			}
		}
	}

	return -1
}

func LoadInput() ([]int, []BingoCard) {
	byteArr, _ := ioutil.ReadFile("input.txt")
	inputBlocks := strings.Split(strings.ReplaceAll(string(byteArr), "\r\n", "\n"), "\n\n")
	bingoStrings := inputBlocks[1:]
	bingoCards := make([]BingoCard, len(bingoStrings))

	for i, s := range bingoStrings {
		rows := strings.Split(s, "\n")
		bingoCards[i].cardRows = make([][]int, len(rows))
		bingoCards[i].numbersHit = make(map[int]bool, 0)
		for i2, row := range rows {
			individualNums := strings.Split(strings.ReplaceAll(strings.TrimPrefix(row, " "), "  ", " "), " ")
			bingoCards[i].cardRows[i2] = make([]int, len(individualNums))
			for i3, num := range individualNums {
				bingoCards[i].cardRows[i2][i3], _ = strconv.Atoi(num)
			}
		}
	}

	calledStrArr := strings.Split(inputBlocks[0], ",")
	calledNum := make([]int, len(calledStrArr))
	for i, s := range calledStrArr {
		calledNum[i], _ = strconv.Atoi(s)
	}
	return calledNum, bingoCards
}

func ProcessCardForHit(bingoCard BingoCard, calledNum int) bool {
	for _, row := range bingoCard.cardRows {
		for _, value := range row {
			if value == calledNum {
				bingoCard.numbersHit[calledNum] = true
				return true
			}
		}
	}
	return false
}

func IsCardComplete(bingoCard BingoCard) bool {
	for i := 0; i < len(bingoCard.cardRows); i++ {
		rowValid, columnValid := true, true
		for j := 0; j < len(bingoCard.cardRows); j++ {
			rowValid = rowValid && bingoCard.numbersHit[bingoCard.cardRows[i][j]]
			columnValid = columnValid && bingoCard.numbersHit[bingoCard.cardRows[j][i]]
		}

		if rowValid || columnValid {
			return true
		}
	}

	return false
}

func GetSummedNonHitNums(bingoCard BingoCard) int {
	sum := 0
	for _, row := range bingoCard.cardRows {
		for _, val := range row {
			if !bingoCard.numbersHit[val] {
				sum += val
			}
		}
	}
	return sum
}
