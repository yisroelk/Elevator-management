import time


#Timer class, receives time, and can return the remaining time.
class Timer:
    def __init__(self, set_time):
        self.start_time = time.time() 
        self.remaining_time = 0 
        self.set_time = set_time

    # A function that returns the remaining time from the set time.
    def time_remaining(self):
        current_time = time.time()
        if self.start_time + self.set_time > current_time:
            self.remaining_time = self.start_time + self.set_time - time.time()
            return self.remaining_time
        else:
            return 0



