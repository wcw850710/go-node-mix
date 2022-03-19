package main

import (
	"errors"
	"fmt"
)

func test() (int, error) {
	return 1, errors.New("bad")
}

func main() {
	var i int
	i = 20
	fmt.Println(i)

	i2 := 2
	fmt.Println(i2)

	a, b, c := 1, 2, 3
	fmt.Println(a, b, c)

	var (
		age  int
		name string
	)
	age = 18
	name = "frnak"
	fmt.Println(age, name)

	_, err := test()
	if err != nil {
		fmt.Println(err)
	}
	const PI = 3.1415926
	r := 2.0
	fmt.Println(2 * PI * r)

	const (
		Unknown = 0
		Female  = 1
		Male    = 2 // 長亮定義不使用不抱錯
	)

	const (
		x int = 16
		y     // 無值同上
		s = "abc"
		z
	)
	fmt.Println("y, z:", y, z)

	// const iota 長亮計數器, iota 表行數
	const (
		a1 = iota
		a2
		a3
		a4
	)
	fmt.Println(a1, a2, a3, a4) // 0 1 2 3

}
