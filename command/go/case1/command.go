package case1

import "fmt"

type ICommand interface {
	execute() error
}

type TurnOnCommand struct{}

func NewTurnOnCommand() *TurnOnCommand {
	return &TurnOnCommand{}
}

func (t *TurnOnCommand) execute() error {
	fmt.Println("command: turn on")
	return nil
}

type TurnOffCommand struct{}

func NewTurnOffCommand() *TurnOffCommand {
	return &TurnOffCommand{}
}

func (t *TurnOffCommand) execute() error {
	fmt.Println("command: turn off")
	return nil
}
