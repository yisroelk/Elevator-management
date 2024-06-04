from config import *
from stopwatch_class import *
from timer_class import *


class elevator:

    def __init__(self, i):
        self.array_order = []
        self.availability_floor = 0

        self.pixels_travel = 0
        self.availability_time = 0
        self.sum_availability_time = 0
        self.current_floor = 0
        self.prevous_floor = 0
        self.travel = 0
        self.time_past = 0
        self.time_waiting = 0
        self.current_time = 0
        self.display_current_floor = self.current_floor * FLOOR_HEIGHT
        self.num_elv = i
        self.tt = StopWatch()

        self.img = pygame.image.load('elv.png')
        self.img = pygame.transform.scale(self.img, (FLOOR_HEIGHT, FLOOR_HEIGHT))
    
        self.and_delay_on_floor = 0



    def manager(self, floor, availabil_time):
        self.array_order.append(floor) 
        self.sum_availability_time = availabil_time + TIME_STOP_FLOOR
        self.availability_time = availabil_time
        self.availability_floor = floor
        self.and_delay_on_floor = Timer(self.availability_time + TIME_STOP_FLOOR)


    # Returns a tuple containing the availability time and the floor where it will be available
    def availability(self):
        return self.sum_availability_time, self.availability_floor
    


    def update(self):
        if self.sum_availability_time != 0:
            self.sum_availability_time = self.and_delay_on_floor.time_remaining()
        if self.array_order and self.time_waiting == 0:
            self.prevous_floor = self.current_floor
            self.current_floor = self.array_order.pop(0)
            self.current_time = StopWatch()
            self.travel = abs(self.current_floor - self.prevous_floor) * TIME_PASS_FLOOR
            self.time_waiting = TIME_STOP_FLOOR
        if self.travel != 0:
            t = self.current_time.get_elapsed_time()
            if self.current_floor > self.prevous_floor:
                self.pixels_travel = FLOOR_HEIGHT/TIME_PASS_FLOOR * t
            else:
                self.pixels_travel = -FLOOR_HEIGHT/TIME_PASS_FLOOR * t
            if t >= self.travel:
                self.travel = 0
                self.pixels_travel = 0
                self.display_current_floor = self.current_floor * FLOOR_HEIGHT
                pygame.mixer.Sound('ding.mp3').play()
                self.tt = StopWatch()
        if self.travel == 0:
            t2 = self.tt.get_elapsed_time()
            if t2 >= self.time_waiting:
                self.time_waiting = 0

    # Draws the elevator, based on variables that are constantly updated with the updated location
    def draw_elevator(self, screen, x,):
        screen.blit(self.img, (x, self.display_current_floor + self.pixels_travel))
