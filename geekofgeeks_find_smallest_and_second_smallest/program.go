package main

import "fmt"

const MaxUint = ^uint(0)

func findSmallestAndSecondSmallest(a []uint) {
	first := MaxUint
	second := MaxUint

	if len(a) == 0 {
		return
	}

	for i := 0; i < len(a); i++ {
		if a[i] < first {
			second = first
			first = a[i]
		} else if a[i] < second && a[i] != first {
			second = a[i]
		}
	}

	fmt.Println(first, second)
}

func main() {
	a := []uint{1, 2, 3, 4, 5}
	findSmallestAndSecondSmallest(a)
}
