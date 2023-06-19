# Operating System Scheduler Simulator

OS scheduling simulator:

1. First Come First Serve (FCFS)
2. Round Robin

## For Grading

run:

`python -m simulator examples/test1.in`

The output will be found in the directory `schedules`.

## Getting Started

To run:

`python -m simulator <filename>`

Input file should have the format for each line:

`<process id> <arriving time> <burst time>`

The program will write a line in the following format every time the CPU
performs a context switch:

`(<timestamp>, <process id>)`

And lastly output the average waiting time:

`Average waiting time <waiting time>`

The outputs will be written in the folder called `schedules`.
