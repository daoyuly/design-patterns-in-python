package case1

import (
	"fmt"
	"testing"
	"time"
)

func TextCommandDemo(t *testing.T) {
	eventChan := make(chan string)
	defer close(eventChan)

	// 用于测试，模拟来自客户端的事件
	go func() {
		events := []string{"turnOn", "turnOff", "turnOn"}
		for _, e := range events {
			eventChan <- e
		}
	}()

	// 使用命令队列缓存命令
	commands := make(chan ICommand, 1000)
	defer close(commands)

	go func() {
		for {
			event, ok := <-eventChan

			if !ok {
				return
			}

			var command ICommand
			switch event {
			case "turnOn":
				command = NewTurnOnCommand()
			case "turnOff":
				command = NewTurnOffCommand()
			}

			commands <- command
		}
	}()

	for {
		select {
		case c := <-commands:
			ok := c.execute()
			if ok != nil {
				print("executing error")
			}
		case <-time.After(2 * time.Second):
			fmt.Println("timeout 2s")
			return

		}
	}

}
