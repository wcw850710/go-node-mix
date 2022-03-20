package main

import (
	"fmt"
	"strings"
)

func main() {
	var name string = "frank:零八"
	// 返回自結長度, 英文用 ascii, 中文用 unicode
	// go 用 utf8, 1 自結表英文, 3 自結表中文
	fmt.Println(len(name)) // 12

	name_arr := []rune(name)
	fmt.Println(len(name_arr)) // 8

	var name2 string = "ffrank:l8"
	fmt.Println(strings.Contains(name2, "l8"))
	fmt.Println(strings.Index(name2, "l8"))
	fmt.Println(strings.Count(name2, "f"))
	fmt.Println(strings.HasPrefix(name2, "f"))
	fmt.Println(strings.HasSuffix(name2, "f"))
	fmt.Println(strings.ToUpper(name2))
	fmt.Println(strings.ToLower(name2))
	fmt.Println(strings.Compare("a", "b")) // -1 字符串比較就是 ascii 比較, -1 1 0
	fmt.Println(strings.Compare("b", "a")) // 1
	fmt.Println(strings.Compare("b", "b")) // 0
	fmt.Println(strings.TrimSpace(" hello world "))
	fmt.Println(strings.Trim(" hello world ", " "))
	fmt.Println(strings.Split(name2, ":"))
	fmt.Println(strings.Join(strings.Split(name2, ":"), " "))
	fmt.Println(strings.Replace(name2+"l8", "l8", "零八", 1))
}
