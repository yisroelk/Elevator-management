from config import *
from floor_class import *
from elevator_class import *
# from GUI import *


class Building:

    def __init__(self):
        self.floors = [floor(i) for i in range(NUMBER_FLOORS)]
        self.elevators = [elevator(i) for i in range(NUMBER_ELEVATORS)]


    def draw_building(self, screen):
        # self.floors[0].draw_floor(screen)
        # self.floors[0].draw_button(screen)
        for f in self.floors:
            f.draw_floor(screen)
            f.draw_button(screen)
        for e in self.elevators:
            e.draw_elevator(screen, time.time())
        

    def conversion_button(self, x, y):
        if BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) < x < BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) + BUTTON_WIDTH:
            return ((math.ceil(y/FLOOR_HEIGHT)) - 1)
        

    def order_elevator(self, order_floor):
        min = float('inf')
        object_elevator = None
        for e in self.elevators:
            time, floor = e.availability()
            travel = abs(floor - order_floor) * TIME_PASS_FLOOR + time
            if travel < min:
                min = travel
                object_elevator = e
        object_elevator.manager(order_floor, min)
        self.floors[order_floor].elevator_arrive(min)
        return min, order_floor





        min = 0
        pass






