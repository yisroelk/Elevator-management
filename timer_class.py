import time
class Timer:
    def __init__(self, set_time):
        self.startTime = time.time()
        self.remaining_time = 0
        self.set_time = set_time

    def time_remaining(self):
        current_time = time.time()
        if self.startTime + self.set_time > current_time:
            self.remaining_time = self.startTime + self.set_time - time.time()
            return self.remaining_time
        else:
            return 0



