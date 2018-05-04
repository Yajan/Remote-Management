package main

import (
	"fmt"
	"net/http"
	"time"
)

var url = "https://www.google.com"
var users = 10
var count = 10

func say(result chan time.Duration) {
	startTime := time.Now()
	resp, err := http.Get(url)
	duration := time.Now().Sub(startTime)

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(resp.Status, duration)
	result <- duration
}

func average(result []time.Duration) {
	var total time.Duration
	for i := 0; i < len(result); i++ {
		total = total + result[i]
	}
	avrg := total.Nanoseconds() / int64(len(result))
	fmt.Println(avrg)
}

func main() {
	report := make([]time.Duration, users)
	summary := make([][]time.Duration, count)
	result := make(chan time.Duration)
	for j := 0; j < count; j++ {

		for i := 0; i < users; i++ {
			time.Sleep(100 * time.Millisecond)
			go say(result)
			report[i] = <-result
		}
		summary[j] = report
		average(report)
		fmt.Println("---------------", j, "--------------------")
	}
}
