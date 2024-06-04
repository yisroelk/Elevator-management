from config import *
from floor_class import *
from elevator_class import *


class Building:

    def __init__(self):
        # Creating an array containing elevator objects according to the number of elevators in the config file.
        self.floors = [floor(i) for i in range(NUMBER_FLOORS)] 
        # Creating an array containing elevator objects according to the number of elevators in the config file.
        self.elevators = [elevator(i) for i in range(NUMBER_ELEVATORS)] 
        self.dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    def draw_building(self, screen):
        distance_between_elevators = BUILDING_POSITION_WIDTH+FLOOR_WIDTH+3 - FLOOR_HEIGHT
        for floor in self.floors:
            floor.draw_building(screen)

        for elevator in self.elevators:
            elevator.draw_elevator(screen, distance_between_elevators + FLOOR_HEIGHT)
            distance_between_elevators += FLOOR_HEIGHT

        

    def button_pressed(self, x, y):
        if BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) < x < BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) + BUTTON_WIDTH:
            return ((math.ceil(y/FLOOR_HEIGHT)) - 1)
        

    def order_elevator(self, x, y):
        order_floor = self.button_pressed(x, y)
        if order_floor is None:
            return
        a = self.floors[order_floor].update_floor_availability()
        if a is False:
            return
        best_time = float('inf')
        object_elevator = None
        for e in self.elevators:
            time, floor = e.availability()
            travel = abs(floor - order_floor) * TIME_PASS_FLOOR + time
            if travel < best_time:
                best_time = travel
                object_elevator = e
        object_elevator.manager(order_floor, best_time)
        self.floors[order_floor].elevator_arrive(best_time)


    def update(self):
        for elevator in self.elevators:
            elevator.update()
        