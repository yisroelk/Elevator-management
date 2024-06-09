from config import *
from Stopwatch import *
from Timer import *


class Elevator:
    """
    Represents an elevator within the building.
    """

    def __init__(self, elv_num):
        """
        Initializes the Elevator object.

        Args:
        - i (int): Number identifier of the elevator.
        """
        self.array_order = []  # List of floors the elevator needs to stop at
        self.availability_floor = 0  # Floor where the elevator will be available next
        self.pixels_travel = 0  # Pixels the elevator has traveled
        self.availability_time = 0  # Time when the elevator will be available next
        self.sum_availability_time = 0  # Sum of availability time and time to stop at a floor
        self.current_floor = 0  # Current floor of the elevator
        self.previous_floor = 0  # Previous floor of the elevator
        self.travel = 0  # Time needed for the elevator to travel between floors
        self.time_waiting = 0  # Time the elevator spends waiting at a floor
        self.display_current_floor = (1 + self.current_floor) * FLOOR_HEIGHT  # Current floor displayed on the screen
        self.num_elv = elv_num  # Number identifier of the elevator
        self.tt = StopWatch()  # Stopwatch for time tracking
        self.and_delay_on_floor = 0  # Timer for the delay when the elevator stops at a floor
        # Load and scale the elevator image
        self.img = pygame.image.load(ELEVATOR_IMG)
        self.img = pygame.transform.scale(self.img, (FLOOR_HEIGHT, FLOOR_HEIGHT))


    def manager(self, floor, availabil_time):
        """
        Manages the elevator's movement and availability.

        Args:
        - floor (int): Floor where the elevator is ordered to go.
        - availabil_time (int): Time when the elevator will be available at the specified floor.

        This method updates the elevator's order list, availability time, and floor based on new orders.
        It also sets up a timer for the delay when the elevator stops at a floor.
        """
        self.array_order.append(floor)  # Add the specified floor to the elevator's order list
        self.sum_availability_time = availabil_time + TIME_STOP_FLOOR  # Set the availability time with stop floor time
        self.availability_time = availabil_time  # Set the availability time without stop floor time
        self.availability_floor = floor  # Set the availability floor
        self.and_delay_on_floor = Timer(self.availability_time + TIME_STOP_FLOOR)  # Set up delay timer


    # Returns a tuple containing the availability time and the floor where it will be available.
    def availability(self):
        """
        Returns the availability time and the floor where the elevator will be available next.

        Returns:
        - tuple: A tuple containing the availability time (sum of availability time and time to stop at a floor)
                and the floor number where the elevator will be available next.
        """
        return self.sum_availability_time, self.availability_floor


    def update(self):
        """
        Updates the elevator's position and status.

        This method is called to update the elevator's position and status.
        It handles the elevator's movement between floors, waiting time at each floor,
        and triggers the elevator arrival sound when it reaches a destination floor.
        """
        # If the elevator is still waiting at a floor, update the remaining time for availability
        if self.sum_availability_time != 0:
            self.sum_availability_time = self.and_delay_on_floor.time_remaining()

        # If there are floors in the order list and the elevator is not currently waiting, move to the next floor
        if self.array_order and self.time_waiting == 0:
            self.previous_floor = self.current_floor  # Set the previous floor to the current floor
            self.current_floor = self.array_order.pop(0)  # Move to the next floor in the order list
            self.current_time = StopWatch()  # Start tracking time for this floor
            self.travel = abs(self.current_floor - self.previous_floor) * TIME_PASS_FLOOR  # Calculate travel time
            self.time_waiting = TIME_STOP_FLOOR  # Set waiting time at the floor

        # If the elevator is currently in transit between floors
        if self.travel != 0:
            t = self.current_time.get_elapsed_time()  # Get elapsed time since reaching the current floor
            # Calculate the distance traveled based on elapsed time and direction
            if self.current_floor > self.previous_floor:
                self.pixels_travel = -FLOOR_HEIGHT / TIME_PASS_FLOOR * t
            else:
                self.pixels_travel = FLOOR_HEIGHT / TIME_PASS_FLOOR * t
            # If the travel time has been exceeded, stop at the destination floor
            if t >= self.travel:
                self.travel = 0  # Reset travel time
                self.pixels_travel = 0  # Reset travel distance
                self.display_current_floor = (1 + self.current_floor) * FLOOR_HEIGHT  # Update displayed floor
                pygame.mixer.Sound(ELEVATOR_ARRIVAL_SOUND).play()  # Play arrival sound
                self.tt = StopWatch()  # Start tracking waiting time at the floor

        # If the elevator has arrived at the destination floor and waiting time is completed
        if self.travel == 0:
            t2 = self.tt.get_elapsed_time()  # Get elapsed time since arriving at the floor
            # If waiting time is completed, reset waiting time
            if t2 >= self.time_waiting:
                self.time_waiting = 0


    def draw_elevator(self, screen, x):
        """
        Draws the elevator on the screen.

        Args:
        - screen (pygame.Surface): Pygame display surface to draw the elevator on.
        - x (int): X-coordinate of the elevator's position.

        This method blits (draws) the elevator image onto the specified screen surface at the given position.
        It takes into account the current floor level and any vertical travel (pixels_travel) the elevator has made.
        """
        # Calculate the y-coordinate based on the elevator's current position and vertical travel
        y = SCREEN_HEIGHT - self.display_current_floor + self.pixels_travel
        # Draw the elevator image onto the screen at the specified coordinates
        screen.blit(self.img, (x, y))

