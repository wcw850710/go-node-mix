package main

import "fmt"

func main() {
	name := "frank"
	age := 18
	// %s 字串
	// %d 數字
	// %v 直接打直
	// %#v 類型特徵打字
	// %T 類型
	fmt.Printf("name:%s, age:%d\n", name, age)
	fmt.Printf("name:%v, age:%v\n", name, age)
	desc := fmt.Sprintf("name:%s, age:%d\n", name, age)
	fmt.Println(desc)

	var (
		n string
		a int8
	)
	fmt.Println("請輸入姓名和年齡")
	fmt.Scanln(&n, &a)
	fmt.Println(n, a)
	fmt.Println("請輸入姓名和年齡2")
	fmt.Scanf("%s %d", &n, &a)
	fmt.Println(n, a)
}
