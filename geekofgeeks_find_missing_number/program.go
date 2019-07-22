package main

import (
	"fmt"
)

func getMissingNumber(a [5]int) {
	sum := 0
	for i := 0; i < len(a); i++ {
		sum += a[i]
	}

	alen := len(a)
	total := (alen + 1) * (alen + 2) / 2
	missingNumber := total - sum
	fmt.Println(missingNumber)

}

func main() {
	a := [5]int{1, 2, 4, 5, 6}
	getMissingNumber(a)
}
