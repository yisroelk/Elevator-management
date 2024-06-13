from config import *
from Floor import *
from Elevator import *


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
        self.floors = [Floor(i) for i in range(NUMBER_FLOORS)]
        self.elevators = [Elevator(i) for i in range(NUMBER_ELEVATORS)]
        #self.dis = pygame.display.set_mode((SCREEN_WIDTH, FLOOR_HEIGHT * NUMBER_FLOORS))
        

    def draw_building(self, world):
        """
        Draws the building on the given screen.

        Args:
        - screen (pygame.Surface): Pygame display surface to draw the building on.
        """
        distance_between_elevators = BUILDING_SIDE_MARGIN + FLOOR_WIDTH - FLOOR_HEIGHT
        # Draw each floor
        for floor in self.floors:
            floor.draw_building(world)
        # Draw each elevator
        for elevator in self.elevators:
            elevator.draw_elevator(world, distance_between_elevators + FLOOR_HEIGHT)
            distance_between_elevators += FLOOR_HEIGHT


    def order_elevator(self, x, y):
        """
        orders an elevator based on the floor number the button was pressed on.

        Args:
        - x (int): x-coordinate of the button pressed.
        - y (int): y-coordinate of the button pressed.
        """
        # Determine the floor number based on the button pressed
        order_floor = None
        for floor in self.floors:
            order_floor = floor.button_pressed(x, y)
            if order_floor is not None:
                break
        if order_floor is None:
            return
        # Check if the floor is available for an elevator to pick up
        availabil = self.floors[order_floor].update_floor_availability()
        if availabil is False:
            return
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
        # Iterate through each elevator in the building and update
        for elevator in self.elevators:
            elevator.update()

