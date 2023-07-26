package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

type Movie struct {
	Title     string `json:"title"`
	EpisodeID int    `json:"episode_id"`
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Useage: <app> <movieID>")
		return
	}

	movieID := os.Args[1]
	url := "https://swapi-api.alx-tools.com/api/films/"

	response, err := http.Get(url + movieID)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		fmt.Println(err)
		return
	}

	var movie Movie
	err = json.Unmarshal(body, &movie)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(movie.Title)
}
