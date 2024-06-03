from config import *
from stopwatch_class import *
from timer_class import *
# from Building_class import *
# from floor_class import *
# from GUI import *

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
        self.tt = StopWatch()

        self.img = pygame.image.load('elv.png')
        self.img = pygame.transform.scale(self.img, (FLOOR_HEIGHT, FLOOR_HEIGHT))
    
        self.x = 0

        self.num_elv = i

    def manager(self, floor, availabil_time):
        self.array_order.append(floor)
        self.sum_availability_time = availabil_time + TIME_STOP_FLOOR
        self.availability_time = availabil_time
        self.availability_floor = floor
        self.x = Timer(self.availability_time + TIME_STOP_FLOOR)




    def availability(self):
        return self.sum_availability_time, self.availability_floor

        
    def move_elevator(self):
        
        # self.prevous_floor = self.current_floor
        # self.time = time.time()
        # self.array_order.pop(0)
        # self.current_floor = self.array_order(0)
        pass


    def update(self):
        if self.sum_availability_time != 0:
            self.sum_availability_time = self.x.time_remaining()
        #print(self.array_order)
        if self.array_order and self.time_waiting == 0:
            self.prevous_floor = self.current_floor
            self.current_floor = self.array_order.pop(0)
            #print(self.current_floor, self.prevous_floor)
            self.current_time = StopWatch()
            #self.time_waiting = TIME_STOP_FLOOR
            self.travel = abs(self.current_floor - self.prevous_floor) * TIME_PASS_FLOOR
            #print(self.travel)
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
                # add ding
                self.tt = StopWatch()
        if self.travel == 0:
            t2 = self.tt.get_elapsed_time()
            if t2 >= self.time_waiting:
                self.time_waiting = 0


            


    def draw_elevator(self, screen, x,):
        screen.blit(self.img, (x, self.display_current_floor + self.pixels_travel))



        # if self.availability_time == 0:
        #     return self.time
        # else:
        #     transition = (time - self.time) / TIME_PASS_FLOOR * FLOOR_HEIGHT
        #     if self.direction == 'up':
        #         self.prevous_floor + transition
        #     else:
        #         self.prevous_floor - transition
        #     return self.prevous_floor

        


    # def set_destination(self):
      # #self.destination_floor.append(floor)
       #     # return destination_floor
    #     return self.availability_time

    # def set_availability(self, floor):
    #     #self.availability_time += # parameter from the main function, or dlobal veriable what seved the time from the main function
    #     self.availability_floor = floor