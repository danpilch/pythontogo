package main

import "fmt"

func main() {
	// Create a new array
	go_array := []int{1, 2, 3}

	// Print array
	fmt.Println(go_array)
	//[1 2 3]

	// Add to array
	go_array = append(go_array, 4)
	//[1 2 3 4]

	for _, v := range go_array {
		fmt.Println(v)
	}
}
