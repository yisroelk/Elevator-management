from config import *
from floor_class import *
from elevator_class import *


class Building:
    """
    Represents a building with floors and elevators.

    Attributes:
    - floors (list): List of Floor objects representing each floor in the building.
    - elevators (list): List of Elevator objects representing each elevator in the building.
    - dis (pygame.Surface): Pygame display surface for rendering the building.
    """

    def __init__(self):
        """
        Initializes the Building object.

        Creates floors and elevators according to the configuration settings.
        """
        self.floors = [Floor(i) for i in range(NUMBER_FLOORS)]  # Create list of Floor objects
        self.elevators = [Elevator(i) for i in range(NUMBER_ELEVATORS)]  # Create list of Elevator objects
        self.dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Initialize display surface

    def draw_building(self, screen):
        """
        Draws the building on the given screen.

        Args:
        - screen (pygame.Surface): Pygame display surface to draw the building on.
        """
        distance_between_elevators = BUILDING_SIDE_MARGIN + FLOOR_WIDTH - FLOOR_HEIGHT
        # Draw each floor
        for floor in self.floors:
            floor.draw_building(screen)

        # Draw each elevator
        for elevator in self.elevators:
            elevator.draw_elevator(screen, distance_between_elevators + FLOOR_HEIGHT)
            distance_between_elevators += FLOOR_HEIGHT


    def button_pressed(self, x, y):
        """
        Determines the floor number based on the button pressed.

        Args:
        - x (int): x-coordinate of the place of the click.
        - y (int): y-coordinate of the place of the click.

        Returns:
        - int or None: Floor number if a valid button is pressed, None otherwise.
        """
        # Calculate the x-coordinate range for the button
        left_x = BUILDING_SIDE_MARGIN + FLOOR_WIDTH // 2 - (BUTTON_WIDTH // 2)
        right_x = left_x + BUTTON_WIDTH
        # Check if the button press falls within the x-coordinate range
        if left_x < x < right_x:
            # Calculate the floor number based on the button press
            floor_number = math.ceil((SCREEN_HEIGHT - y) / FLOOR_HEIGHT) - 1
            return floor_number  # Return the floor number
        else:
            return None  # Return None if the press is outside the valid range of a button



    def order_elevator(self, x, y):
        """
        orders an elevator based on the floor number the button was pressed on.

        Args:
        - x (int): x-coordinate of the button pressed.
        - y (int): y-coordinate of the button pressed.
        """
        # Determine the floor number based on the button pressed
        order_floor = self.button_pressed(x, y)
        if order_floor is None:
            return  # If no valid floor button was pressed, exit the method
        # Check if the floor is available for an elevator to pick up
        availabil = self.floors[order_floor].update_floor_availability()
        if availabil is False:
            return  # If the floor is not available, exit the method
        # Find the best elevator to respond to the order
        best_time = float('inf')
        object_elevator = None
        for elv in self.elevators:
            time, floor = elv.availability()
            # Calculate the min time for the elevator to reach the order floor
            travel = abs(floor - order_floor) * TIME_PASS_FLOOR + time
            if travel < best_time:
                best_time = travel
                object_elevator = elv
        # Send the elevator to the order floor
        object_elevator.manager(order_floor, best_time)
        # Notify the floor that an elevator is arriving in X time
        self.floors[order_floor].elevator_arrive(best_time)


    def update(self):
        """
        Updates the elevators in the building.

        This method updates each elevator in the building by calling their respective
        update methods to handle their position and status.
        """
        # Iterate through each elevator in the building
        for elevator in self.elevators:
            # Update the elevator's position and status
            elevator.update()

