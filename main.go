package main

import (
	"context"
	"log"
	"net/http"
	"time"

	"github.com/AlexanderGrom/go-starter"
)

func main() {
	mux := http.FileServer(http.Dir("."))

	srv := &http.Server{
		Addr:    ":8000",
		Handler: mux,
	}

	// Registration function: Close listening port
	starter.Bind(func() {
		ctx, _ := context.WithTimeout(context.Background(), 60*time.Second)
		srv.Shutdown(ctx)
	})

	go func() {
		if err := srv.ListenAndServe(); err != nil {
			log.Println("Error Serve:", err)
		}
	}()

	// Wait until all functions completes
	starter.Wait()
}
