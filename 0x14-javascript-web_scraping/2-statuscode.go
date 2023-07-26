package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: <app> <URL>")
		return
	}
	myUrl := os.Args[1]

	response, err := http.Get(myUrl)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer response.Body.Close()

	fmt.Println("Code:", response.StatusCode)
}
