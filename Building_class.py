from config import *
from floor_class import *
from elevator_class import *
# from GUI import *


class Building:

    def __init__(self):
        self.floors = [floor(i) for i in range(NUMBER_FLOORS)]
        self.elevators = [elevator(i) for i in range(NUMBER_ELEVATORS)]


    def draw_building(self, screen):
        x = BUILDING_POSITION_WIDTH+FLOOR_WIDTH+3 - FLOOR_HEIGHT # קבלת רוחב המעלית באמצעות גובה הקומה (המעלית מרובעת)
        for f in self.floors:
            f.draw_floor(screen)
            f.draw_button(screen)
        for e in self.elevators:
            e.draw_elevator(screen, x + FLOOR_HEIGHT, time.time())
            x += FLOOR_HEIGHT
        

    def conversion_button(self, x, y):
        if BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) < x < BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) + BUTTON_WIDTH:
            return ((math.ceil(y/FLOOR_HEIGHT)) - 1)
        

    def order_elevator(self, x, y):
        order_floor = self.conversion_button(x, y)
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
        for el in self.elevators:
            el.update()
        





        best_time = 0
        pass






