package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage:<app> <fileToWrite> <stringToWrite>")
		return
	}
	filePath := os.Args[1]
	content := os.Args[2]

	err := os.WriteFile(filePath, []byte(content), 0666)
	if err != nil {
		log.Fatal(err)
	}
}
