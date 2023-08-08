package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage:<app> <fileToRead>")
		return
	}
	filePath := os.Args[1]

	content, err := os.ReadFile(filePath)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(content))
}
