# Elevator management

Elevator management is a Python program for managing elevators.
This project simulates the behavior of elevators in a building using Pygame.

## Overview

The simulation consists of three main classes:

1. `Building`: Represents the building containing floors and elevators.
2. `Floor`: Represents a floor in the building with buttons and timers.
3. `Elevator`: Represents an elevator with functionality for movement and scheduling.

## Classes

### 1. Building Class

The `Building` class initializes and manages the building structure. It contains methods for updating and drawing the building on the screen.

### 2. Floor Class

The `Floor` class represents a floor in the building. It handles the buttons for calling elevators and timers for indicating elevator arrival times. The class is responsible for user interaction and updating the floor status.

### 3. Elevator Class

The `Elevator` class represents an elevator. It manages its movement, scheduling, and availability. This class updates the elevator position and status based on user input and simulation logic.

## Features

- Multiple elevators with configurable parameters such as speed and capacity.
- Simulation of elevator movement and arrival times.
- User interaction to call elevators and select destinations.

## Structure

The project has the following structure:

- `config.py`: Configuration file containing parameters such as elevator speed, floor height, and button colors.
- `main.py`: Main script to run the simulation.
- `Building_class.py`: Class definition for the Building.
- `floor_class.py`: Class definition for the Floor.
- `elevator_class.py`: Class definition for the Elevator.
- `stopwatch_class.py`: Class definition for a stopwatch used for timing.
- `timer_class.py`: Class definition for a timer used for scheduling.

## Installation and Usage

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/elevator-simulation.git
```
2. Install Pygame:
```
python main.py
```

### Usage
1. Run the main script:
```
python main.py
```
2. Click on a floor button to call an elevator.

### Configuration
The behavior of the elevators can be configured using the `config.py fil`'. Parameters such as elevator speed, floor height, and button colors can be adjusted to customize the simulation.

## Walkthrough of the program
When running the main.py file, we create an object of Building, who then creates all the other objects in their starting positions.

When a button is pressed the building will find the best elevator to send to that floor, then we run the manager() function on that elevator, which takes care of the rest.

In each iteration of the pygame loop we update all the objects, and then put them on the screen.






![elv](https://github.com/yisroelk/Elevator-management/assets/96789748/95bc76aa-3f77-497a-8ec5-786394694998)

