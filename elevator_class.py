from config import *
from stopwatch_class import *
# from Building_class import *
# from floor_class import *
# from GUI import *

class elevator:

    def __init__(self, i):
        self.time = time.time()
        self.availability_time = 0
        self.destination_floor = []
        self.availability_floor = 0
        self.current_floor = 0
        self.prevous_floor = 0
        self.direction = 'up'
        self.current_elevator_location = 3
        self.elevator_state = False #מצב התנועה של המעלית 
        self.img = pygame.image.load('elv.png')
        self.img = pygame.transform.scale(self.img, (FLOOR_HEIGHT, FLOOR_HEIGHT))
        self.current_time = StopWatch()
        self.time_past = 0


    # def direction(self, prevous_floor, current_floor):
    #     prevous_floor - current_floor




    def manager(self, floor, availabil_time):
        self.destination_floor.append(floor)
        self.availability_time = availabil_time + TIME_STOP_FLOOR

        # timer = availabil_time
        pass


    def availability(self):
        return self.availability_time, self.availability_floor

        
    def move_elevator(self):
        self.prevous_floor = self.current_floor
        self.time = time.time()
        self.destination_floor.pop(0)
        self.current_floor = self.destination_floor(0)


    
    def update(self):
        z = self.current_time.get_elapsed_time()
        self.time_past = 3*FLOOR_HEIGHT/0.5 * z


    def draw_elevator(self, screen, x, time):
        screen.blit(self.img, (x,self.time_past))



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