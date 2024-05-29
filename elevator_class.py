from config import *


class elevator:

    def __init__(self, i):
        
        self.availability_time = 10
        self.destination_floor = []
        self.availability_floor = 7
        self.current_floor = None
        self.current_time = 0

        
    def set_destination(self):
        #self.destination_floor.append(floor)
        # return destination_floor
        return self.availability_time

    def set_availability(self, floor):
        #self.availability_time += # parameter from the main function, or dlobal veriable what seved the time from the main function
        self.availability_floor = floor


    def manager(self):
        


        pass