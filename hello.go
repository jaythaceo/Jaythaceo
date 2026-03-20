package main
"""This is a simple Go program that demonstrates basic syntax, including comments, variable declaration, if/else statements, and for loops."""

import "fmt"

func main() {

	# This is a comment
	# print fmt
	fmt.Println("Hello World")

	var a int = 222
	var b int = 23

	# if/else statement
	if a > b {
		fmt.Println("A is less than b")
	} else {
		fmt.Println(("A is not less than b"))
	}

	# for loop
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}


}