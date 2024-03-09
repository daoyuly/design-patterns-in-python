package semaphore_pattern

import (
	"errors"
	"os"
	"time"
)

var (
	ErrNoTickets      = errors.New("semaphore: could not aquire semaphore")
	ErrIllegalRelease = errors.New("semaphore: can't release the semaphore without acquiring it first")
)

type Interface interface {
	Acquire() error
	Release() error
}

type implementation struct {
	sem     chan struct{}
	timeout time.Duration
}

func (s *implementation) Acquire() error {
	select {
	case s.sem <- struct{}{}:
		return nil
	case <-time.After(s.timeout):
		return ErrNoTickets
	}
}

func (s *implementation) Release() error {
	select {
	case _ = <-s.sem:
		return nil
	case <-time.After(s.timeout):
		return ErrIllegalRelease
	}
}

func NewSemaphore(tickets int, timeout time.Duration) Interface {
	return &implementation{
		sem:     make(chan struct{}, tickets),
		timeout: timeout,
	}
}

func SemaphoreWithTimeouts() {
	tickets, timeout := 0, 3*time.Second
	s := NewSemaphore(tickets, timeout)
	if err := s.Acquire(); err != nil {
		if !errors.Is(err, ErrNoTickets) {
			panic(err)
		}
		os.Exit(1)
	}
}
