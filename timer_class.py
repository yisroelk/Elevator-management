import time
class Timer:
    def __init__(self, set_time):
        self.startTime = time.time()
        self.x = 0
        self.set_time = set_time

    def time_remaining(self):
        current_time = time.time()
        if self.startTime + self.set_time > current_time:
            self.x = self.startTime + self.set_time - time.time()
            return self.x
        else:
            return 0

    def time_remaining_str(self):
        return self.x
# a = Timer()
# while a.time_remaining(7) != 0:
#     print(a.time_remaining(7))

