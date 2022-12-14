package main

import (
	"fmt"
	"net/http"
	"strconv"
)

var counter = 0

func increment(w http.ResponseWriter, r *http.Request) {
	counter++
	fmt.Fprintf(w, strconv.Itoa(counter))
}

func decrement(w http.ResponseWriter, r *http.Request) {
	counter--
	fmt.Fprintf(w, strconv.Itoa(counter))
}

func reset(w http.ResponseWriter, r *http.Request) {
	counter = 0
	fmt.Fprintf(w, strconv.Itoa(counter))
}

func main() {
	http.HandleFunc("/increment", increment)
	http.HandleFunc("/decrement", decrement)
	http.HandleFunc("/reset", reset)
	http.ListenAndServe(":8080", nil)
}
