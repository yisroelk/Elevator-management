# Elevator management

Elevator management is a Python program for managing elevators.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.

```bash
pip install pygame
```


## Class Responsibility
In total there are 5 classes: Building, Elevator, Floor, Timer and StopWatch.

### Building responsibilities:
Initiate all the other objects 
Check for new calls from buttons
When a new call is identified, calculate the best elevator and send the new call to it, and start the timer on the floor
Update all the objects in the pygame loop 
Draw all the objects in the pygame loop

### Elevator responsibilities:
When a new call is received, add it correctly to the queue
Update the position of the elevator 
Draw the elevator on the screen
Managing the queue 
Activate the ding and enter rest mode when arriving at a destination

### Floor responsibilities:
Draw the floor on the screen

### Timer responsibilities:
Update the time left on the timer 
Draw the timer on the screen

### StopWatch responsibilities:
Update the time left on the timer 
Draw the timer on the screen

## Walkthrough of the program
When running the main.py file, we create an object of Building, who then creates all the other objects in their starting positions.

When a button is pressed the building will find the best elevator to send to that floor, then we run the manager() function on that elevator, which takes care of the rest.

In each iteration of the pygame loop we update all the objects, and then put them on the screen.





