package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

type Movie struct {
	Title     string `json:"title"`
	EpisodeID int    `json:"episode_id"`
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: <app> <movieID>")
		return
	}

	movieID := os.Args[1]
	url := "https://swapi-api.alx-tools.com/api/films/"

	response, err := http.Get(url + movieID)
	if err != nil {
		log.Fatalln(err)
	}
	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		log.Fatalf("Failed to read response body: %s", err)
	}

	var movie Movie
	err = json.Unmarshal(body, &movie)
	if err != nil {
		log.Fatalf("Failed to unmarshal movie details: %s", err)
	}

	fmt.Println(movie.Title)

}
