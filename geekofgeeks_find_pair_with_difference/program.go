package main

import "fmt"

func contains(s []int, e int) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func findPair(arr []int, n int) {
	for i := 0; i < len(arr); i++ {
		if contains(arr, n+arr[i]) {
			fmt.Println(arr[i], n+arr[i])
			return
		}
	}
	fmt.Println("No such pair")
	return
}
func main() {
	arr := []int{5, 20, 3, 2, 50, 80}
	n := 78
	findPair(arr, n)
}
