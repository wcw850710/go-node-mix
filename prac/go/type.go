package main

import (
	"fmt"
	"strconv"
)

func main() {
	var gender bool = false
	fmt.Println(gender)
	var age uint8 = 2
	fmt.Println(age)

	var a1 = 1.05
	var a2 = int(a1)
	fmt.Println(a2)

	var c int64 = 56
	fmt.Printf("%T %c\n", strconv.Itoa(int(c)), c)
	data, err := strconv.Atoi("12")
	if err == nil {
		fmt.Println(data)
	}
	fmt.Println(strconv.ParseBool("false"))
	fmt.Println(strconv.FormatBool(true))
}
