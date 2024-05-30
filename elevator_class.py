from config import *
# from Building_class import *
# from floor_class import *
# from GUI import *

class elevator:

    def __init__(self, i):
        self.time = time.time()
        self.availability_time = 0
        self.destination_floor = [0]
        self.availability_floor = 0
        self.current_floor = None
        self.prevous_floor = None
        self.direction = 'up'
        # self.current_time = 0


    def manager(self, floor, availabil_time):
        self.destination_floor.append(floor)
        self.availability_time = availabil_time + TIME_STOP_FLOOR

        # timer = availabil_time
        pass


    def availability(self):
        return self.availability_time, self.availability_floor

        
    def move_elevator(self):
        self.prevous_floor = self.current_floor
        self.time = self.pop_elevator(time.time())




    def pop_elevator(self, time):
        self.current_floor = self.destination_floor.pop(0)
        return time


        current = self.destination_floor[0]
        destination = self.destination_floor[1]
        x = abs(current - destination)*TIME_PASS_FLOOR

        self.availability_floor.pop(0)
        

    def draw_elevator(self, screen, time):
        if self.availability_time == 0:
            return self.time
        else:
            transition = (time - self.time) / TIME_PASS_FLOOR * FLOOR_HEIGHT
            if self.direction == 'up':
                self.prevous_floor + transition
            else:
                self.prevous_floor - transition

        pass


    # def set_destination(self):
      # #self.destination_floor.append(floor)
       #     # return destination_floor
    #     return self.availability_time

    # def set_availability(self, floor):
    #     #self.availability_time += # parameter from the main function, or dlobal veriable what seved the time from the main function
    #     self.availability_floor = floor